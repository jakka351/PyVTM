#!/bin/bash
# Vehicle Traffic Monitor Launcher
# Ford Motor Company CAN Bus Monitor

echo "========================================"
echo " Vehicle Traffic Monitor v7.81.6"
echo " Ford Motor Company"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.7 or higher"
    exit 1
fi

echo "Python detected..."
echo ""

# Check if j2534.py exists
if [ ! -f "j2534.py" ]; then
    echo "WARNING: j2534.py not found"
    echo "The application will run in demo mode"
    echo ""
fi

# Check if vtm_main.py exists
if [ ! -f "vtm_main.py" ]; then
    echo "ERROR: vtm_main.py not found"
    echo "Please ensure all project files are in the same directory"
    exit 1
fi

echo "Launching Vehicle Traffic Monitor..."
echo ""
echo "TIP: Connect your J2534 device before starting"
echo "     Go to Setup -> Device Selection to select device"
echo ""

# Launch the application
python3 vtm_main.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Application exited with error"
    read -p "Press Enter to continue..."
fi
