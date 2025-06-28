#!/usr/bin/env python3
"""
Web-based ND2 File Viewer - Simplified Version
A minimal ND2 file viewer with web interface for opening, viewing, and exporting ND2 files.
"""

import os
import io
import base64
import json
from pathlib import Path
import numpy as np
from PIL import Image
import nd2
import tifffile
from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
import tempfile
import threading
import webbrowser
from functools import wraps

app = Flask(__name__)
app.secret_key = 'nd2_viewer_secret_key'

# Global state
current_nd2_file = None
current_file_path = None
current_metadata = {}
last_heartbeat_time = None

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def apply_channel_color_mapping(image_array, channel, custom_color=None):
    """
    Apply color mapping to grayscale image based on channel
    If custom_color is provided (hex format like #ff0000), use that color
    Otherwise use default mapping:
    Channel 0 (1): Blue
    Channel 1 (2): Green  
    Channel 2 (3): Red
    Channel 3 (4): Far red (Magenta)
    Channel 4+ (5+): Grayscale
    """
    # Ensure image is uint8 for display
    if image_array.dtype != np.uint8:
        # Normalize to 0-255 range if needed
        if image_array.max() > 255:
            image_array = ((image_array.astype(np.float32) / image_array.max()) * 255).astype(np.uint8)
        else:
            image_array = image_array.astype(np.uint8)
    
    # Create RGB image
    height, width = image_array.shape
    rgb_image = np.zeros((height, width, 3), dtype=np.uint8)
    
    if custom_color:
        # Use custom color
        try:
            r, g, b = hex_to_rgb(custom_color)
            # Apply the color by scaling each channel by the normalized grayscale values
            norm_image = image_array.astype(np.float32) / 255.0
            rgb_image[:, :, 0] = (norm_image * r).astype(np.uint8)  # Red
            rgb_image[:, :, 1] = (norm_image * g).astype(np.uint8)  # Green
            rgb_image[:, :, 2] = (norm_image * b).astype(np.uint8)  # Blue
            print(f"Debug: Applied custom color {custom_color} for channel {channel}")
        except:
            print(f"Debug: Failed to parse custom color {custom_color}, using default")
            custom_color = None
    
    if not custom_color:
        # Use default color mapping
        if channel == 0:  # Channel 1 -> Blue
            rgb_image[:, :, 2] = image_array  # Blue channel
            print(f"Debug: Applied blue color mapping for channel {channel}")
        elif channel == 1:  # Channel 2 -> Green
            rgb_image[:, :, 1] = image_array  # Green channel
            print(f"Debug: Applied green color mapping for channel {channel}")
        elif channel == 2:  # Channel 3 -> Red
            rgb_image[:, :, 0] = image_array  # Red channel
            print(f"Debug: Applied red color mapping for channel {channel}")
        elif channel == 3:  # Channel 4 -> Far red (Magenta)
            rgb_image[:, :, 0] = image_array  # Red channel
            rgb_image[:, :, 2] = image_array  # Blue channel (Red + Blue = Magenta)
            print(f"Debug: Applied magenta color mapping for channel {channel}")
        else:  # Channel 5+ -> Grayscale
            rgb_image[:, :, 0] = image_array  # Red channel
            rgb_image[:, :, 1] = image_array  # Green channel  
            rgb_image[:, :, 2] = image_array  # Blue channel
            print(f"Debug: Applied grayscale color mapping for channel {channel}")
    
    return rgb_image

def extract_metadata_simple(nd2_file):
    """Extract comprehensive metadata from ND2 file with enhanced spatial calibration support"""
    metadata = {}
    
    try:
        # Basic information that's always available
        metadata['filename'] = os.path.basename(nd2_file.path) if hasattr(nd2_file, 'path') else 'Unknown'
        metadata['shape'] = list(nd2_file.shape) if hasattr(nd2_file, 'shape') else []
        metadata['dtype'] = str(nd2_file.dtype) if hasattr(nd2_file, 'dtype') else 'Unknown'
        metadata['sizes'] = dict(nd2_file.sizes) if hasattr(nd2_file, 'sizes') else {}
        metadata['ndim'] = nd2_file.ndim if hasattr(nd2_file, 'ndim') else 0
        
        # File size
        try:
            if hasattr(nd2_file, 'path') and nd2_file.path:
                metadata['file_size_mb'] = round(os.path.getsize(nd2_file.path) / (1024 * 1024), 2)
        except:
            metadata['file_size_mb'] = 'Unknown'
        
        # Calculate memory usage
        if metadata['shape']:
            total_pixels = 1
            for dim in metadata['shape']:
                total_pixels *= dim
            bytes_per_pixel = 2 if '16' in metadata['dtype'] else 1
            memory_mb = round((total_pixels * bytes_per_pixel) / (1024 * 1024), 2)
            metadata['estimated_memory_mb'] = memory_mb
            metadata['total_pixels'] = total_pixels
        
        # Enhanced spatial calibration extraction
        spatial_calibration = {}
        pixel_size_um = None
        
        # Method 1: Try the direct voxel_size() method (most reliable)
        try:
            if hasattr(nd2_file, 'voxel_size') and callable(nd2_file.voxel_size):
                voxel_size = nd2_file.voxel_size()
                if voxel_size is not None:
                    spatial_calibration['voxel_size_method'] = 'voxel_size() function'
                    if hasattr(voxel_size, 'x') and voxel_size.x > 0:
                        pixel_size_um = float(voxel_size.x)
                        spatial_calibration['pixel_size_x_um'] = round(pixel_size_um, 6)
                    if hasattr(voxel_size, 'y') and voxel_size.y > 0:
                        spatial_calibration['pixel_size_y_um'] = round(float(voxel_size.y), 6)
                    if hasattr(voxel_size, 'z') and voxel_size.z > 0:
                        spatial_calibration['pixel_size_z_um'] = round(float(voxel_size.z), 6)
                    spatial_calibration['units'] = 'micrometers (µm)'
                    spatial_calibration['calibration_source'] = 'ND2 voxel_size method'
        except Exception as e:
            spatial_calibration['voxel_size_error'] = str(e)
        
        # Method 2: Check metadata channels for volume calibration info
        if not pixel_size_um and hasattr(nd2_file, 'metadata') and nd2_file.metadata:
            try:
                file_metadata = nd2_file.metadata
                
                # Look for channel volume information
                if hasattr(file_metadata, 'channels') and file_metadata.channels:
                    for i, channel in enumerate(file_metadata.channels):
                        if hasattr(channel, 'volume') and channel.volume:
                            volume = channel.volume
                            if hasattr(volume, 'axesCalibration') and volume.axesCalibration:
                                calibrations = volume.axesCalibration
                                if len(calibrations) >= 2:
                                    pixel_size_um = float(calibrations[0])  # X calibration
                                    spatial_calibration['pixel_size_x_um'] = round(pixel_size_um, 6)
                                    spatial_calibration['pixel_size_y_um'] = round(float(calibrations[1]), 6)
                                    if len(calibrations) >= 3:
                                        spatial_calibration['pixel_size_z_um'] = round(float(calibrations[2]), 6)
                                    spatial_calibration['units'] = 'micrometers (µm)'
                                    spatial_calibration['calibration_source'] = f'Channel {i} volume.axesCalibration'
                                    
                                    # Check if axes are calibrated
                                    if hasattr(volume, 'axesCalibrated'):
                                        spatial_calibration['axes_calibrated'] = list(volume.axesCalibrated)
                                    
                                    # Check axis interpretation
                                    if hasattr(volume, 'axesInterpretation'):
                                        try:
                                            spatial_calibration['axes_interpretation'] = [str(interp) for interp in volume.axesInterpretation]
                                        except:
                                            spatial_calibration['axes_interpretation'] = str(volume.axesInterpretation)
                                    break
                
                # Method 3: Try other pixel size attributes
                if not pixel_size_um:
                    pixel_size_attrs = ['pixel_microns', 'pixelSizeUm', 'pixel_size_um', 'pixelSize']
                    for attr in pixel_size_attrs:
                        if hasattr(file_metadata, attr):
                            try:
                                value = getattr(file_metadata, attr)
                                if value and float(value) > 0:
                                    pixel_size_um = float(value)
                                    spatial_calibration['pixel_size_x_um'] = round(pixel_size_um, 6)
                                    spatial_calibration['pixel_size_y_um'] = round(pixel_size_um, 6)
                                    spatial_calibration['units'] = 'micrometers (µm)'
                                    spatial_calibration['calibration_source'] = f'metadata.{attr}'
                                    break
                            except:
                                continue
                
                # Extract microscope and objective information for ImageJ-like display
                if hasattr(file_metadata, 'channels') and file_metadata.channels:
                    microscope_info = {}
                    objective_info = {}
                    
                    for channel in file_metadata.channels:
                        if hasattr(channel, 'microscope') and channel.microscope:
                            microscope = channel.microscope
                            if hasattr(microscope, 'objectiveMagnification'):
                                objective_info['magnification'] = float(microscope.objectiveMagnification)
                            if hasattr(microscope, 'objectiveName'):
                                objective_info['name'] = str(microscope.objectiveName)
                            if hasattr(microscope, 'objectiveNumericalAperture'):
                                objective_info['numerical_aperture'] = float(microscope.objectiveNumericalAperture)
                            if hasattr(microscope, 'zoomMagnification'):
                                objective_info['zoom_magnification'] = float(microscope.zoomMagnification)
                            if hasattr(microscope, 'immersionRefractiveIndex'):
                                objective_info['immersion_refractive_index'] = float(microscope.immersionRefractiveIndex)
                            if hasattr(microscope, 'modalityFlags'):
                                objective_info['modality'] = list(microscope.modalityFlags)
                            break
                    
                    if objective_info:
                        spatial_calibration['objective'] = objective_info
                
                # Basic information
                if hasattr(file_metadata, 'contents'):
                    contents = file_metadata.contents
                    try:
                        metadata['channels'] = getattr(contents, 'channelCount', 'Unknown')
                        metadata['frames'] = getattr(contents, 'frameCount', 'Unknown')
                    except:
                        pass
                
                # Date info
                try:
                    if hasattr(file_metadata, 'date'):
                        metadata['acquisition_date'] = str(file_metadata.date)
                except:
                    pass
                
            except Exception as meta_error:
                spatial_calibration['metadata_warning'] = f'Some spatial metadata could not be extracted: {str(meta_error)}'
        
        # Store spatial calibration info
        if spatial_calibration:
            metadata['spatial_calibration'] = spatial_calibration
            
            # Also set the legacy pixel_size_um for backward compatibility
            if 'pixel_size_x_um' in spatial_calibration:
                metadata['pixel_size_um'] = spatial_calibration['pixel_size_x_um']
        
        # Calculate spatial dimensions if pixel size is available
        sizes = metadata.get('sizes', {})
        
        # Always provide spatial dimensions when pixel size is available (2D, 3D, time-lapse, etc.)
        if pixel_size_um and sizes:
            spatial_dims = {}
            
            # X dimension (width) - always calculate if available
            if 'X' in sizes:
                width_um = sizes['X'] * pixel_size_um
                spatial_dims['width_um'] = round(width_um, 2)
                spatial_dims['width_mm'] = round(width_um / 1000, 3)
                spatial_dims['width_pixels'] = sizes['X']
            
            # Y dimension (height) - always calculate if available
            if 'Y' in sizes:
                height_um = sizes['Y'] * pixel_size_um
                spatial_dims['height_um'] = round(height_um, 2)
                spatial_dims['height_mm'] = round(height_um / 1000, 3)
                spatial_dims['height_pixels'] = sizes['Y']
            
            # Z dimension (depth) - only if it's a true 3D stack with multiple Z-slices
            if 'Z' in sizes and sizes['Z'] > 1:
                # Use Z pixel size if available, otherwise default to XY pixel size
                z_step_um = spatial_calibration.get('pixel_size_z_um', pixel_size_um)
                
                depth_um = sizes['Z'] * z_step_um
                spatial_dims['depth_um'] = round(depth_um, 2)
                spatial_dims['depth_mm'] = round(depth_um / 1000, 3)
                spatial_dims['depth_slices'] = sizes['Z']
                spatial_dims['z_step_um'] = round(z_step_um, 6)
            
            # Add ImageJ-style calibration summary
            calibration_summary = []
            if 'width_um' in spatial_dims:
                calibration_summary.append(f"Width: {spatial_dims['width_pixels']} pixels = {spatial_dims['width_um']} µm")
            if 'height_um' in spatial_dims:
                calibration_summary.append(f"Height: {spatial_dims['height_pixels']} pixels = {spatial_dims['height_um']} µm")
            if 'depth_um' in spatial_dims:
                calibration_summary.append(f"Depth: {spatial_dims['depth_slices']} slices = {spatial_dims['depth_um']} µm")
            if pixel_size_um:
                calibration_summary.append(f"Pixel size: {round(pixel_size_um, 6)} µm/pixel")
            
            spatial_dims['calibration_summary'] = calibration_summary
            
            # Add image type information
            if 'T' in sizes and sizes['T'] > 1:
                if 'Z' in sizes and sizes['Z'] > 1:
                    spatial_dims['image_type'] = '4D Time-lapse Z-stack'
                else:
                    spatial_dims['image_type'] = '3D Time-lapse (Movie)'
            elif 'Z' in sizes and sizes['Z'] > 1:
                spatial_dims['image_type'] = '3D Z-stack'
            else:
                spatial_dims['image_type'] = '2D Image'
            
            metadata['spatial_dimensions'] = spatial_dims
        
        # Also provide basic pixel dimensions even without pixel size
        elif sizes and ('X' in sizes or 'Y' in sizes):
            spatial_dims = {}
            if 'X' in sizes:
                spatial_dims['width_pixels'] = sizes['X']
            if 'Y' in sizes:
                spatial_dims['height_pixels'] = sizes['Y']
            if 'Z' in sizes and sizes['Z'] > 1:
                spatial_dims['depth_slices'] = sizes['Z']
            
            # Determine image type
            if 'T' in sizes and sizes['T'] > 1:
                if 'Z' in sizes and sizes['Z'] > 1:
                    spatial_dims['image_type'] = '4D Time-lapse Z-stack'
                else:
                    spatial_dims['image_type'] = '3D Time-lapse (Movie)'
            elif 'Z' in sizes and sizes['Z'] > 1:
                spatial_dims['image_type'] = '3D Z-stack'
            else:
                spatial_dims['image_type'] = '2D Image'
            
            spatial_dims['pixel_size_available'] = False
            spatial_dims['calibration_note'] = 'Physical size unavailable - no pixel calibration found in file'
            metadata['spatial_dimensions'] = spatial_dims
        
        # Calculate time duration for time-lapse movies
        if 'T' in sizes and sizes['T'] > 1:
            time_interval_s = None
            
            # Try to get time interval from experiment info
            try:
                if hasattr(nd2_file, 'experiment') and nd2_file.experiment:
                    for exp in nd2_file.experiment:
                        if hasattr(exp, 'parameters') and exp.parameters:
                            params = exp.parameters
                            # Try different parameter names for time interval
                            for param_name in ['periodMs', 'period', 'timeIntervalMs', 'interval']:
                                try:
                                    if hasattr(params, 'get') and callable(getattr(params, 'get')):
                                        interval_ms = params.get(param_name)
                                    else:
                                        interval_ms = getattr(params, param_name, None)
                                    
                                    if interval_ms is not None:
                                        time_interval_s = float(interval_ms) / 1000.0  # Convert ms to seconds
                                        break
                                except:
                                    continue
                            if time_interval_s:
                                break
            except:
                pass
            
            # If we found time interval, calculate duration
            if time_interval_s:
                total_duration_s = (sizes['T'] - 1) * time_interval_s  # N-1 intervals for N timepoints
                temporal_info = {
                    'total_timepoints': sizes['T'],
                    'time_interval_s': round(time_interval_s, 3),
                    'total_duration_s': round(total_duration_s, 2),
                    'total_duration_min': round(total_duration_s / 60, 2),
                    'total_duration_hr': round(total_duration_s / 3600, 3)
                }
                metadata['temporal_info'] = temporal_info
            else:
                # Provide basic temporal info even without time interval
                metadata['temporal_info'] = {
                    'total_timepoints': sizes['T'],
                    'time_interval_s': 'Unknown',
                    'total_duration_s': 'Unknown'
                }
        
        # Try to get text info safely
        try:
            if hasattr(nd2_file, 'text_info') and nd2_file.text_info:
                text_info = nd2_file.text_info
                metadata['text_info'] = {}
                
                # Handle both dict and object types
                for key in ['date', 'description', 'capturing_software', 'capture_software_version', 'optics']:
                    try:
                        if hasattr(text_info, 'get') and callable(getattr(text_info, 'get')):
                            metadata['text_info'][key] = text_info.get(key, 'Unknown')
                        else:
                            metadata['text_info'][key] = getattr(text_info, key, 'Unknown')
                    except:
                        metadata['text_info'][key] = 'Unknown'
        except Exception as text_error:
            metadata['text_info_error'] = str(text_error)
    
    except Exception as e:
        metadata['metadata_error'] = str(e)
        import traceback
        metadata['metadata_traceback'] = traceback.format_exc()
    
    return metadata

def ensure_nd2_file(f):
    """Decorator to ensure an ND2 file is loaded"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_nd2_file is None:
            return jsonify({'error': 'No ND2 file loaded'}), 400
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    """Main viewer page"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload"""
    global current_nd2_file, current_file_path, current_metadata
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not file.filename.lower().endswith('.nd2'):
        return jsonify({'error': 'Please upload an ND2 file'}), 400
    
    try:
        # Save uploaded file temporarily
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, file.filename)
        file.save(temp_path)
        
        # Close existing file if open
        if current_nd2_file is not None:
            current_nd2_file.close()
        
        # Open new file
        current_nd2_file = nd2.ND2File(temp_path)
        current_file_path = temp_path
        
        # Extract metadata using simplified function
        current_metadata = extract_metadata_simple(current_nd2_file)
        
        return jsonify({
            'success': True,
            'filename': file.filename,
            'metadata': current_metadata
        })
        
    except Exception as e:
        return jsonify({'error': f'Failed to load ND2 file: {str(e)}'}), 500

@app.route('/get_frame')
@ensure_nd2_file
def get_frame():
    """Get a specific frame as base64 encoded image"""
    try:
        # Get parameters
        channel = int(request.args.get('channel', 0))
        timepoint = int(request.args.get('timepoint', 0))
        z_slice = int(request.args.get('z_slice', 0))
        contrast_min = float(request.args.get('contrast_min', 0))
        contrast_max = float(request.args.get('contrast_max', 255))
        custom_color = request.args.get('custom_color')  # Optional custom color
        
        # Debug: Print file information
        print(f"Debug: ND2 file sizes: {current_nd2_file.sizes}")
        print(f"Debug: Requested - channel: {channel}, timepoint: {timepoint}, z_slice: {z_slice}")
        
        # Get the image array using a simple approach
        full_array = np.asarray(current_nd2_file)
        print(f"Debug: Full array shape: {full_array.shape}, dtype: {full_array.dtype}")
        
        # Handle different dimensionalities
        if full_array.ndim == 2:  # Y, X
            image_array = full_array
            print("Debug: Using 2D array directly")
        elif full_array.ndim == 3:  # One of: T,Y,X or Z,Y,X or C,Y,X
            sizes = current_nd2_file.sizes
            if 'C' in sizes and sizes['C'] > 1:
                idx = min(channel, sizes['C'] - 1)
                image_array = full_array[idx]
                print(f"Debug: Using channel {idx} from 3D array")
            elif 'Z' in sizes and sizes['Z'] > 1:
                idx = min(z_slice, sizes['Z'] - 1)
                image_array = full_array[idx]
                print(f"Debug: Using Z-slice {idx} from 3D array")
            elif 'T' in sizes and sizes['T'] > 1:
                idx = min(timepoint, sizes['T'] - 1)
                image_array = full_array[idx]
                print(f"Debug: Using timepoint {idx} from 3D array")
            else:
                image_array = full_array[0]  # Safe fallback
                print("Debug: Using first slice of 3D array")
        elif full_array.ndim == 4:  # Two dimensions + Y,X
            sizes = current_nd2_file.sizes
            if 'T' in sizes and 'C' in sizes and sizes['T'] > 1 and sizes['C'] > 1:
                # Time-lapse with channels: T,C,Y,X
                t_idx = min(timepoint, sizes['T'] - 1)
                c_idx = min(channel, sizes['C'] - 1)
                image_array = full_array[t_idx, c_idx]
                print(f"Debug: Using T={t_idx}, C={c_idx} from 4D T,C,Y,X array")
            elif 'Z' in sizes and 'C' in sizes and sizes['Z'] > 1 and sizes['C'] > 1:
                # Z-stack with channels: Z,C,Y,X
                z_idx = min(z_slice, sizes['Z'] - 1)
                c_idx = min(channel, sizes['C'] - 1)
                image_array = full_array[z_idx, c_idx]
                print(f"Debug: Using Z={z_idx}, C={c_idx} from 4D Z,C,Y,X array")
            elif 'T' in sizes and 'Z' in sizes and sizes['T'] > 1 and sizes['Z'] > 1:
                # Time-lapse with z-stacks: T,Z,Y,X
                t_idx = min(timepoint, sizes['T'] - 1)
                z_idx = min(z_slice, sizes['Z'] - 1)
                image_array = full_array[t_idx, z_idx]
                print(f"Debug: Using T={t_idx}, Z={z_idx} from 4D T,Z,Y,X array")
            else:
                # Safe fallback for unknown 4D arrangements
                image_array = full_array[0, 0]
                print("Debug: Using [0,0] from 4D array as fallback")
        elif full_array.ndim == 5:  # Three dimensions + Y,X
            sizes = current_nd2_file.sizes
            if 'T' in sizes and 'Z' in sizes and 'C' in sizes:
                # Time-lapse with z-stacks and channels: T,Z,C,Y,X
                t_idx = min(timepoint, sizes['T'] - 1)
                z_idx = min(z_slice, sizes['Z'] - 1)
                c_idx = min(channel, sizes['C'] - 1)
                image_array = full_array[t_idx, z_idx, c_idx]
                print(f"Debug: Using T={t_idx}, Z={z_idx}, C={c_idx} from 5D T,Z,C,Y,X array")
            else:
                # Safe fallback
                image_array = full_array[0, 0, 0]
                print("Debug: Using [0,0,0] from 5D array as fallback")
        else:
            # Fallback for unexpected dimensions
            idx = [0] * (full_array.ndim - 2) + [slice(None), slice(None)]
            image_array = full_array[tuple(idx)]
            print(f"Debug: Using fallback indexing for {full_array.ndim}D array")
        
        print(f"Debug: Selected image shape: {image_array.shape}, dtype: {image_array.dtype}")
        
        # Store original array for auto-contrast calculation
        original_array = image_array.copy()
        
        # Apply contrast adjustment
        if contrast_max > contrast_min:
            image_array = np.clip(image_array, contrast_min, contrast_max)
            image_array = ((image_array - contrast_min) / (contrast_max - contrast_min) * 255).astype(np.uint8)
        else:
            image_array = np.zeros_like(image_array, dtype=np.uint8)
        
        # Apply color mapping based on channel
        colored_image = apply_channel_color_mapping(image_array, channel, custom_color)
        
        # Convert to PIL Image
        pil_image = Image.fromarray(colored_image, mode='RGB')
        
        # Convert to base64 for web display
        buffer = io.BytesIO()
        pil_image.save(buffer, format='PNG')
        img_data = base64.b64encode(buffer.getvalue()).decode()
        
        # Calculate auto-contrast values from original data
        p1, p99 = np.percentile(original_array, [1, 99])
        
        return jsonify({
            'image_data': f'data:image/png;base64,{img_data}',
            'auto_contrast_min': float(p1),
            'auto_contrast_max': float(p99),
            'image_shape': list(image_array.shape)
        })
        
    except Exception as e:
        import traceback
        error_details = {
            'error': f'Failed to get frame: {str(e)}',
            'type': type(e).__name__,
            'traceback': traceback.format_exc()
        }
        print(f"Error in get_frame: {error_details}")
        return jsonify(error_details), 500

@app.route('/metadata')
@ensure_nd2_file
def get_metadata():
    """Get comprehensive metadata"""
    try:
        return jsonify(current_metadata)
    except Exception as e:
        return jsonify({'error': f'Failed to get metadata: {str(e)}'}), 500

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    """Heartbeat endpoint to keep the server alive while browser is active"""
    global last_heartbeat_time
    import time
    last_heartbeat_time = time.time()
    return jsonify({'status': 'alive'}), 200

@app.route('/shutdown', methods=['POST'])
def shutdown_server():
    """Shutdown the Flask server"""
    try:
        # Close any open ND2 file
        global current_nd2_file
        if current_nd2_file is not None:
            current_nd2_file.close()
            current_nd2_file = None
        
        # Check if this is an auto-shutdown from browser closing
        is_auto_shutdown = (request.content_type and 'multipart/form-data' in request.content_type) or \
                          request.headers.get('User-Agent', '').startswith('Mozilla') and not request.is_json
        
        if is_auto_shutdown:
            print("🛑 Browser window closed - auto-shutting down ND2 Viewer...")
        else:
            print("🛑 Shutdown requested from web interface...")
        
        print("✅ ND2 Viewer shutting down gracefully.")
        
        # For development server, we can use this approach
        import os
        import signal
        
        def delayed_shutdown():
            """Shutdown after a small delay to allow response to be sent"""
            import time
            time.sleep(0.5)  # Allow response to be sent
            os.kill(os.getpid(), signal.SIGTERM)
        
        # Start shutdown in a separate thread
        import threading
        shutdown_thread = threading.Thread(target=delayed_shutdown)
        shutdown_thread.daemon = True
        shutdown_thread.start()
        
        return jsonify({'message': 'Server shutting down...'}), 200
        
    except Exception as e:
        print(f"Error during shutdown: {e}")
        return jsonify({'error': f'Shutdown failed: {str(e)}'}), 500

def monitor_heartbeat():
    """Monitor heartbeat and shutdown if browser disconnects"""
    global last_heartbeat_time
    import time
    import os
    import signal
    
    # Wait for initial connection
    time.sleep(5)
    
    while True:
        time.sleep(10)  # Check every 10 seconds
        
        if last_heartbeat_time is not None:
            current_time = time.time()
            # If no heartbeat for 30 seconds, assume browser is closed
            if current_time - last_heartbeat_time > 30:
                print("🛑 No heartbeat from browser for 30 seconds - shutting down ND2 Viewer...")
                
                # Close any open ND2 file
                global current_nd2_file
                if current_nd2_file is not None:
                    current_nd2_file.close()
                    current_nd2_file = None
                
                print("✅ ND2 Viewer shutting down due to browser disconnect.")
                os.kill(os.getpid(), signal.SIGTERM)
                break

def main():
    """Main entry point"""
    print("🔬 Starting ND2 Web Viewer...")
    print("📱 The viewer will open in your web browser at http://127.0.0.1:5001")
    print("✨ Auto-shutdown enabled: Server will stop when you close the browser window")
    print("⌨️  Press Ctrl+C to stop the server manually")
    
    # Start heartbeat monitor in a separate thread
    heartbeat_thread = threading.Thread(target=monitor_heartbeat)
    heartbeat_thread.daemon = True
    heartbeat_thread.start()
    
    # Start browser in a separate thread
    def open_browser():
        import time
        time.sleep(1.5)  # Give server time to start
        webbrowser.open('http://127.0.0.1:5001')
    
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Run Flask app
    try:
        app.run(host='127.0.0.1', port=5001, debug=False)
    except OSError as e:
        if "Address already in use" in str(e):
            print("Address already in use")
            print("Port 5001 is in use by another program. Either identify and stop that program, or start the server with a different port.")
        else:
            raise

if __name__ == '__main__':
    main() 