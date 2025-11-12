import time
import datetime
import platform
import psutil
import sys

# Script to display system information in an infinite loop.

# Set the interval in seconds
INTERVAL = 10

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format e.g:
    1253656 => '1.20MB'
    1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_system_info():
    """Gathers and prints system information."""
    print(f"--- Report at {datetime.datetime.now()} ---")

    # 1. OS Information
    print("[OS Info]")
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print()

    # 2. CPU Information
    print("[CPU Info]")
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print()

    # 3. RAM Information
    print("[RAM Info]")
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print()

    # 4. Disk Information
    print("[Disk Info - Root Partition]")
    disk_usage = psutil.disk_usage('/')
    print(f"Total: {get_size(disk_usage.total)}")
    print(f"Used: {get_size(disk_usage.used)}")
    print(f"Free: {get_size(disk_usage.free)}")
    print(f"Percentage: {disk_usage.percent}%")
    print()

if __name__ == "__main__":
    print("Starting Python System Monitor...")
    print("---------------------------------")
    # Ensure output is unbuffered
    sys.stdout.reconfigure(line_buffering=True)
    
    while True:
        get_system_info()
        print("---------------------------------")
        print(f"Next report in {INTERVAL} seconds...")
        time.sleep(INTERVAL)
