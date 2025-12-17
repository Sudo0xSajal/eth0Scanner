# eth0Scanner – Ethernet-Layer Local Network Scanner

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Stars](https://img.shields.io/github/stars/Sudo0xSajal/eth0Scanner?style=social)](https://github.com/Sudo0xSajal/eth0Scanner)

A fast, modular, and ethical local network reconnaissance tool built with **Scapy**, **socket programming**, and **Nmap**. Designed for penetration testing labs, CTF challenges, and authorized network assessments.

### Features
- **Lightning-fast ARP host discovery** using Scapy (Ethernet-layer scanning)
- **Custom TCP connect scan** on common ports
- **Accurate service & version detection** with Nmap (`-sV`)
- **Automatic Nmap installation** if missing (Linux/macOS support)
- **Beautiful terminal UI** powered by Rich (tables, panels, colors)
- **Multi-format reports**: JSON and CSV export
- Ethical usage banner and timestamp

### Demo Screenshot
<img width="626" height="422" alt="image" src="https://github.com/user-attachments/assets/81036f88-b2a6-497c-9f7f-6437c86ecf62" />


### Installation

```bash
git clone https://github.com/Sudo0xSajal/eth0Scanner.git
cd eth0Scanner
pip install -r requirements.txt
