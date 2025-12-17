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
<img width="1895" height="487" alt="image" src="https://github.com/user-attachments/assets/84d732ff-b2e6-4134-b6e5-1fb512f1eed7" />


### Installation

```bash
git clone https://github.com/Sudo0xSajal/eth0Scanner.git
cd eth0Scanner
pip install -r requirements.txt
```

### Note: Nmap must be available on the system. The tool can auto-install it on Linux/macOS if missing.

### Usage

**Run the scanner with Python 3:**
```bash
python3 scanner.py
```
### The tool will:

- **Display an ethical usage banner.**

- **Prompt you to enter the target network (e.g., 192.168.1.0/24 or 172.31.0.0/24).**

- **Automatically discover live hosts, scan common ports, enumerate services, and generate reports.**

- **Reports will be saved as ```scan_report.json``` and ```scan_report.csv``` in the current directory.**

### Example:
```bash
python3 scanner.py
Enter Target Network (e.g., 192.168.1.0/24): 172.31.0.0/24
```
## Project Structure

```text
eth0Scanner/
│
├── scanner.py              # Main scanner script
├── host_discovery.py       # Live host discovery (ARP/Ping)
├── port_scanner.py         # TCP port scanning
├── service_scan.py         # Service enumeration via Nmap
├── report.py               # Generate JSON and CSV reports
├── pretty_output.py        # Pretty CLI output (banners, tables)
├── requirements.txt        # Python dependencies
└── README.md               # Instructions
```

### Disclaimer

- **For authorized testing and educational purposes only.**
- **Do not scan networks without explicit permission.**

## Author

**Sajal Haldar**  

- GitHub: [@Sudo0xSajal](https://github.com/Sudo0xSajal)  
- LinkedIn: [linkedin.com/in/sajalhaldar16](https://www.linkedin.com/in/sajalhaldar16)


