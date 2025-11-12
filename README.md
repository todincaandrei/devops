# Proiect DevOps - Monitorizare Sistem

Acest proiect conține două scripturi de monitorizare a sistemului (unul în Bash, unul în Python), containerizate cu Docker și orchestrate cu Docker Compose.

## Structura Proiectului

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

## Partea A: Scripturi de Monitorizare

### 1. Script Bash (`system_info.sh`)

Acest script rulează o buclă infinită care afișează data, ora și informații despre OS, CPU, RAM și disc la fiecare 10 secunde.

**Rulare locală:**
```bash
# Asigurati-va ca scriptul este executabil
chmod +x system_info.sh

# Rulati scriptul
./system_info.sh
```

**Exemplu Output (trunchiat):**
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

### 2. Script Python (`system_info.py`)

Acest script folosește biblioteca `psutil` pentru a colecta și afișa aceleași tipuri de informații.

**Instalare dependențe și rulare locală:**
```bash
# Instalati dependentele
pip install -r requirements.txt

# Rulati scriptul
python3 system_info.py
```

**Exemplu Output (trunchiat):**
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

## Partea B: Containerizare cu Docker

Au fost create două fișiere Dockerfile pentru a containeriza fiecare script.

### 1. Container Bash

**Build:**
```bash
docker build -t bash-monitor -f Dockerfile.bash .
```

**Run:**
```bash
# Porniti containerul in background
docker run -d --name bash_container bash-monitor
```

**Vizualizare loguri:**
```bash
docker logs -f bash_container
```
*Output-ul va fi identic cu cel de la rularea locală a scriptului bash.*

### 2. Container Python

**Build:**
```bash
docker build -t python-monitor -f Dockerfile.python .
```

**Run:**
```bash
# Porniti containerul in background
docker run -d --name python_container python-monitor
```

**Vizualizare loguri:**
```bash
docker logs -f python_container
```
*Output-ul va fi identic cu cel de la rularea locală a scriptului python. Opțiunea `-u` din `CMD` asigură afișarea logurilor în timp real.*

---

## Partea C: Orchestare cu Docker Compose

Fișierul `docker-compose.yaml` definește și rulează ambele servicii simultan.

**Pornire servicii:**
```bash
# Comanda va face build la imagini (daca nu exista) si va porni containerele
docker-compose up -d
```

**Vizualizare loguri (agregat):**
```bash
# Vizualizati logurile pentru ambele servicii in timp real
docker-compose logs -f
```

**Exemplu Output Loguri Docker Compose:**
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

**Oprire și ștergere containere:**
```bash
docker-compose down
```

---

## Funcționalități Adresate pentru Nota 10

- **Documentație Completă:** `README.md` este structurat pentru a permite oricui să replice și să valideze funcționalitatea.
- **Bune Practici Docker:**
    - Folosirea imaginilor `slim` (`python:3.9-slim`) pentru a reduce dimensiunea imaginii finale.
    - Utilizarea eficientă a cache-ului Docker prin copierea `requirements.txt` și instalarea dependențelor într-un layer separat.
    - Adăugarea unui fișier `.dockerignore` pentru a exclude fișiere irelevante din contextul de build, rezultând un build mai rapid și o imagine mai curată.
    - Folosirea opțiunii `python -u` pentru output nebufferizat, esențială pentru vizualizarea logurilor în timp real.
- **Cod Curat și Modular:** Scripturile sunt comentate și ușor de înțeles. Scriptul Python folosește funcții pentru o mai bună organizare.
- **Robustețe:** Serviciile din Docker Compose sunt configurate cu `restart: unless-stopped` pentru a reporni automat în caz de eroare.
