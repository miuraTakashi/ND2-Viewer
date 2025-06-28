-- ND2 Viewer Launcher AppleScript
-- Simplified version to prevent hanging

on run
    try
        -- Show immediate notification to confirm the app is running
        display notification "ND2 Viewer starting..." with title "ND2 Viewer" sound name "Glass"
        
        -- Simple approach: get project directory by going up from app bundle
        set appPath to (path to me) as string
        set appPosixPath to POSIX path of appPath
        
        -- Remove "/app/ND2 Viewer.app" from the end to get project directory
        -- First remove the app name, then remove the app directory
        set appDirectory to (do shell script "dirname " & quoted form of appPosixPath)
        set projectDirectory to (do shell script "dirname " & quoted form of appDirectory)
        
        -- Define paths
        set pythonPath to "/Users/miura/.pyenv/versions/3.11.5/envs/LatestStable/bin/python"
        set scriptPath to projectDirectory & "/web_nd2_viewer_simple.py"
        
        -- Show what we found (for debugging)
        display notification "Project: " & projectDirectory with title "ND2 Viewer Debug"
        
        -- Quick file existence check (non-blocking)
        try
            do shell script "test -f " & quoted form of pythonPath & " && test -f " & quoted form of scriptPath
        on error
            display dialog "Cannot find required files:" & return & return & ¬
                "Python: " & pythonPath & return & ¬
                "Script: " & scriptPath & return & return & ¬
                "Please check your installation." buttons {"OK"} default button "OK" with icon stop
            return
        end try
        
        -- Kill any existing server (quick timeout)
        try
            with timeout of 3 seconds
                do shell script "pkill -f 'python.*web_nd2_viewer' 2>/dev/null || true"
            end timeout
        end try
        
        -- Show launching notification
        display notification "Launching web server..." with title "ND2 Viewer"
        
        -- Launch server in background (simplified command)
        set launchCmd to "cd " & quoted form of projectDirectory & " && " & ¬
            quoted form of pythonPath & " " & quoted form of scriptPath & " > /tmp/nd2viewer.log 2>&1 &"
        
        do shell script launchCmd
        
        -- Wait a moment for server to start
        delay 3
        
        -- Open browser
        display notification "Opening browser..." with title "ND2 Viewer"
        do shell script "open 'http://127.0.0.1:5001'"
        
        -- Final success notification
        delay 1
        display notification "ND2 Viewer ready! Check your browser." with title "ND2 Viewer" sound name "Hero"
        
    on error errorMsg
        -- Show any error that occurs
        display notification "Error: " & errorMsg with title "ND2 Viewer Error" sound name "Basso"
        
        display dialog "ND2 Viewer Error:" & return & return & ¬
            errorMsg & return & return & ¬
            "App Path: " & (POSIX path of (path to me)) buttons {"OK"} default button "OK" with icon stop
    end try
end run 