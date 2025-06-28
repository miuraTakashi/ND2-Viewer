# GitHub Repository Setup Guide

## 📋 Repository Information

**Repository Name:** `ND2-Viewer`  
**Description:** Web-based viewer for Nikon ND2 microscopy files with advanced scientific imaging features  
**Topics:** `microscopy`, `nd2`, `scientific-imaging`, `web-viewer`, `python`, `flask`, `time-lapse`, `multi-channel`, `bioimage-analysis`, `nikon`, `confocal`, `fluorescence`

## 🚀 Steps to Push to GitHub

### 1. Create Repository on GitHub
1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon → "New repository"
3. Repository name: `ND2-Viewer`
4. Description: `Web-based viewer for Nikon ND2 microscopy files with advanced scientific imaging features`
5. Choose **Public** (recommended for open source scientific software)
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

### 2. Connect Local Repository to GitHub
```bash
# Add GitHub as remote origin (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ND2-Viewer.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Configure Repository Settings (Optional)
After pushing, go to your repository on GitHub:

#### Topics & Keywords
- Go to repository → Click ⚙️ gear icon next to "About"
- Add topics: `microscopy`, `nd2`, `scientific-imaging`, `web-viewer`, `python`, `flask`, `time-lapse`, `multi-channel`, `bioimage-analysis`, `nikon`, `confocal`, `fluorescence`

#### Enable Pages (Optional)
- Go to Settings → Pages
- Source: Deploy from a branch
- Branch: main → / (root)
- This creates a demo page at: `https://YOUR_USERNAME.github.io/ND2-Viewer`

#### Add License (Recommended)
- Go to repository main page
- Click "Add file" → "Create new file"
- Name: `LICENSE`
- Choose a template (recommended: MIT or Apache 2.0 for scientific software)

## 📝 Repository Features

This repository includes:
- ✅ **Clean project structure** - Only essential files
- ✅ **Comprehensive README** - Full documentation
- ✅ **Python .gitignore** - Proper exclusions
- ✅ **Production-ready code** - Fully functional viewer
- ✅ **macOS app** - Native desktop integration
- ✅ **Scientific documentation** - Usage examples and technical details

## 🎯 Perfect for Scientific Community

Your ND2 Viewer is ideal for:
- **Research labs** using Nikon microscopes
- **Bioimage analysis** workflows
- **Educational** microscopy courses
- **Open science** initiatives
- **Collaborative** research projects

## 🔬 Citation-Ready

Consider adding a `CITATION.cff` file for academic citations:
```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
authors:
  - family-names: "Your Last Name"
    given-names: "Your First Name"
title: "ND2 Viewer: Web-based Microscopy Image Viewer"
version: 1.0.0
url: "https://github.com/YOUR_USERNAME/ND2-Viewer"
``` 