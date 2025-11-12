# DevOps Project - System Monitoring

This project contains two system monitoring scripts (one in Bash, one in Python), containerized with Docker and orchestrated with Docker Compose.

## Project Structure

```
.
├── .dockerignore
├── docker-compose.yaml
├── Dockerfile.bash
├── Dockerfile.python
├── README.md
├── requirements.txt
├── system_info.py
└── system_info.sh
```

---

## Part A: Monitoring Scripts

### 1. Bash Script (`system_info.sh`)

This script runs an infinite loop that displays the date, time, and information about the OS, CPU, RAM, and disk every 10 seconds.

**Local execution:**
```bash
# Make sure the script is executable
chmod +x system_info.sh

# Run the script
./system_info.sh
```

**Example Output (truncated):**
```
--- Report at Wed Nov 12 10:00:00 EET 2025 ---
[OS Info]
PRETTY_NAME="Ubuntu 22.04.3 LTS"

[CPU Info]
Model name:          11th Gen Intel(R) Core(TM) i7-1185G7 @ 3.00GHz
CPU(s):              8

[RAM Info]
              total        used        free      shared  buff/cache   available
Mem:           15Gi       7.1Gi       1.5Gi       242Mi       6.8Gi       7.9Gi
Swap:         2.0Gi       1.2Gi       833Mi

[Disk Info]
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2       232G  150G   71G  68% /

---------------------------------
Next report in 10 seconds...
```

### 2. Python Script (`system_info.py`)

This script uses the `psutil` library to collect and display the same types of information.

**Install dependencies and local execution:**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python3 system_info.py
```

**Example Output (truncated):**
```
--- Report at 2025-11-12 10:01:00.123456 ---
[OS Info]
System: Linux
Release: 5.15.0-88-generic
Version: #98-Ubuntu SMP Mon Oct 2 15:18:56 UTC 2023

[CPU Info]
Physical cores: 4
Total cores: 8
CPU Usage: 12.5%

[RAM Info]
Total: 15.45GB
Available: 8.45GB
Used: 7.00GB
Percentage: 52.1%

[Disk Info - Root Partition]
Total: 231.82GB
Used: 149.50GB
Free: 70.25GB
Percentage: 68.1%

---------------------------------
Next report in 10 seconds...
```

---

## Part B: Containerization with Docker

Two Dockerfile files have been created to containerize each script.

### 1. Bash Container

**Build:**
```bash
docker build -t bash-monitor -f Dockerfile.bash .
```

**Run:**
```bash
# Start the container in the background
docker run -d --name bash_container bash-monitor
```

**View logs:**
```bash
docker logs -f bash_container
```
*The output will be identical to the local execution of the bash script.*

### 2. Python Container

**Build:**
```bash
docker build -t python-monitor -f Dockerfile.python .
```

**Run:**
```bash
# Start the container in the background
docker run -d --name python_container python-monitor
```

**View logs:**
```bash
docker logs -f python_container
```
*The output will be identical to the local execution of the python script. The `-u` option in `CMD` ensures real-time log display.*

---

## Part C: Orchestration with Docker Compose

The `docker-compose.yaml` file defines and runs both services simultaneously.

**Start services:**
```bash
# The command will build images (if they don't exist) and start the containers
docker-compose up -d
```

**View logs (aggregated):**
```bash
# View logs for both services in real-time
docker-compose logs -f
```

**Example Docker Compose Logs Output:**
```
bash_monitor_container    | --- Report at Wed Nov 12 10:05:00 UTC 2025 ---
bash_monitor_container    | [OS Info]
bash_monitor_container    | PRETTY_NAME="Ubuntu 22.04"
...
python_monitor_container  | --- Report at 2025-11-12 10:05:05.543210 ---
python_monitor_container  | [OS Info]
python_monitor_container  | System: Linux
...
```

**Stop and remove containers:**
```bash
docker-compose down
```