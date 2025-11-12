#!/bin/bash

# Script to display system information in an infinite loop.

# Set the interval in seconds
INTERVAL=10

echo "Starting Bash System Monitor..."
echo "---------------------------------"

while true; do
    echo "--- Report at $(date) ---"
    
    # 1. OS Information
    echo "[OS Info]"
    if [ -f /etc/os-release ]; then
        # Use os-release for modern systems
        cat /etc/os-release | grep PRETTY_NAME
    else
        # Fallback for older systems
        uname -a
    fi
    echo ""

    # 2. CPU Information
    echo "[CPU Info]"
    # Using lscpu for a concise summary
    lscpu | grep "Model name"
    lscpu | grep "CPU(s):" | head -n 1
    echo ""

    # 3. RAM Information
    echo "[RAM Info]"
    # Using free with human-readable output
    free -h
    echo ""

    # 4. Disk Information
    echo "[Disk Info]"
    # Using df with human-readable output for the root filesystem
    df -h /
    echo ""
    
    echo "---------------------------------"
    echo "Next report in $INTERVAL seconds..."
    sleep $INTERVAL
done
