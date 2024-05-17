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

Let's scan my own LAN (Local Area Network)

sudo nmap 192.168.1.0/24 -vvvv -sC -O -sV
This way we're scanning the whole network and seeing all of the devices and ports so we can focus on something particular.

optional: sudo nmap 192.168.1.0/24 -vvvv -sC -O -sV > something.txt
this makes a text file of the scan, this way you have a backup.



