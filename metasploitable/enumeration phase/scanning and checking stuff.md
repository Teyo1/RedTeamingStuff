```markdown
# Scanning Networks with Nmap

In this section, we will explore network scanning using a tool called Nmap.

## What is Nmap?
Nmap (Network Mapper) is a powerful, open-source tool used for network discovery and security auditing. It helps identify hosts and services on a computer network by sending packets and analyzing the responses. Key functionalities of Nmap include:

### 1. Port Scanning
Determines open ports on a target machine.
- **Example**: `nmap -p 1-65535 [Target IP]`

### 2. Service Detection
Identifies running services and their versions.
- **Example**: `nmap -sV [Target IP]`

### 3. Operating System Detection
Attempts to determine the target's operating system.
- **Example**: `nmap -O [Target IP]`

### 4. Network Mapping
Discovers devices and their network structure.
- **Example**: `nmap -sn [Target IP/Range]`

### 5. Vulnerability Scanning
Uses scripts to detect known vulnerabilities.
- **Example**: `nmap --script vuln [Target IP]`

Nmap is widely used by network administrators and security professionals to assess network security and manage assets.

Now you know, so let's start!

## Scanning My Own LAN (Local Area Network)

```bash
sudo nmap 192.168.1.0/24 -vvvv -sC -O -sV
```
This way we're scanning the whole network and seeing all of the devices and ports so we can focus on something particular.

**Optional**: Save the scan output to a text file.
```bash
sudo nmap 192.168.1.0/24 -vvvv -sC -O -sV > something.txt
```
This creates a text file of the scan results, providing a backup.

## Scan Results

From my scan, I obtained the following data for a device in my network:
- Discovered open port 3306/tcp on 192.168.1.15
- Discovered open port 5900/tcp on 192.168.1.15
- Discovered open port 22/tcp on 192.168.1.15
- Discovered open port 25/tcp on 192.168.1.15
- Discovered open port 445/tcp on 192.168.1.15
- Discovered open port 53/tcp on 192.168.1.15
- Discovered open port 80/tcp on 192.168.1.15
- Discovered open port 139/tcp on 192.168.1.15
- Discovered open port 23/tcp on 192.168.1.15
- Discovered open port 21/tcp on 192.168.1.15
- Discovered open port 111/tcp on 192.168.1.15
- Discovered open port 5432/tcp on 192.168.1.15
- Discovered open port 6000/tcp on 192.168.1.15
- Discovered open port 2121/tcp on 192.168.1.15
- Discovered open port 513/tcp on 192.168.1.15
- Discovered open port 6667/tcp on 192.168.1.15
- Discovered open port 1524/tcp on 192.168.1.15
- Discovered open port 514/tcp on 192.168.1.15
- Discovered open port 512/tcp on 192.168.1.15
- Discovered open port 8009/tcp on 192.168.1.15
- Discovered open port 2049/tcp on 192.168.1.15
- Discovered open port 1099/tcp on 192.168.1.15

If we saw a device like this in my organization's network, I'd instantly ask why this device has so many ports open and whether those ports are open to the internet.

## Focusing on the Device with a Vulnerability Scan
```bash
nmap 192.168.1.15 -sC -sV -vvv
```

**Optional**: Output the results to a text file.
```bash
nmap 192.168.1.15 -sC -sV -vvv > filename.txt

