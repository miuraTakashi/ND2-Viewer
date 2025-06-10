#!/bin/bash

# ND2 Viewer Stop Script
# This script completely shuts down all ND2 Viewer processes

echo "🛑 Stopping ND2 Viewer..."

# Kill all Python processes running the ND2 viewer
PROCESSES=$(pgrep -f "web_nd2_viewer")

if [ -n "$PROCESSES" ]; then
    echo "📍 Found ND2 Viewer processes: $PROCESSES"
    pkill -f "python.*web_nd2_viewer"
    
    # Wait a moment for processes to stop
    sleep 2
    
    # Check if any processes are still running
    REMAINING=$(pgrep -f "web_nd2_viewer")
    if [ -n "$REMAINING" ]; then
        echo "⚠️  Some processes still running, force killing..."
        pkill -9 -f "web_nd2_viewer"
    fi
    
    echo "✅ ND2 Viewer stopped successfully!"
else
    echo "ℹ️  No ND2 Viewer processes found running"
fi

# Also check for any processes using port 5001
PORT_PROCESS=$(lsof -ti:5001 2>/dev/null)
if [ -n "$PORT_PROCESS" ]; then
    echo "🔌 Stopping process using port 5001: $PORT_PROCESS"
    kill -9 $PORT_PROCESS 2>/dev/null
fi

echo "🎉 ND2 Viewer shutdown complete!" 