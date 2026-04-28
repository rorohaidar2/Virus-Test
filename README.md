# Windows Security Helper (Prank/Malware Simulation)

A Python-based prank script that simulates malware behavior for testing and educational purposes.

## ⚠️ WARNING

**DO NOT RUN ON YOUR MAIN SYSTEM.** This is designed to be annoying and potentially disruptive.

**USE ONLY IN A CONTROLLED ENVIRONMENT (VM, TEST MACHINE).**

## What It Does

This script simulates malware behavior by:
- Displaying fake virus warning popups
- Consuming CPU and memory resources (causes lag)
- Attempting to copy itself to System32
- Adding itself to Windows startup (registry persistence)

## Requirements

- Python 3.x
- Windows OS (for full functionality)
- Administrator privileges (for System32/registry modifications)

## How to Build

```bash
# Install PyInstaller
pip install pyinstaller

# Build the executable
pyinstaller --onefile --noconsole --name "Windows_Update_Helper" virus_source.py

# The EXE will be in the dist/ folder
