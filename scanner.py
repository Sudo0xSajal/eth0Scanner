# scanner.py
from host_discovery import discover_hosts
from port_scanner import scan_ports
from service_scan import service_scan
from report import generate_reports
from pretty_output import banner, scan_info, host_table, service_table, summary

import shutil
import subprocess
import platform
import sys

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389]

def ensure_nmap():
    """Check if Nmap exists, install if missing (Linux/macOS)"""
    if shutil.which("nmap"):
        print("[✔] Nmap is installed and available in PATH.")
        return

    print("[-] Nmap is not installed or not found in PATH.")
    system = platform.system()

    if system == "Linux":
        print("[+] Attempting to install Nmap via apt...")
        try:
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "nmap"], check=True)
            print("[✔] Nmap installed successfully.")
        except subprocess.CalledProcessError:
            print("[-] Failed to install Nmap automatically. Please install it manually: https://nmap.org/download.html")
            sys.exit(1)

    elif system == "Darwin":
        print("[+] Attempting to install Nmap via Homebrew...")
        if shutil.which("brew") is None:
            print("[-] Homebrew not found. Please install Homebrew first: https://brew.sh/")
            sys.exit(1)
        try:
            subprocess.run(["brew", "install", "nmap"], check=True)
            print("[✔] Nmap installed successfully.")
        except subprocess.CalledProcessError:
            print("[-] Failed to install Nmap via Homebrew. Please install manually: https://nmap.org/download.html")
            sys.exit(1)

    elif system == "Windows":
        print("[!] Automatic installation not supported on Windows.")
        print("    Please download and install Nmap manually: https://nmap.org/download.html")
        sys.exit(1)
    else:
        print(f"[-] Unsupported OS: {system}. Please install Nmap manually.")
        sys.exit(1)

    if shutil.which("nmap") is None:
        print("[-] Nmap still not found. Please check manually.")
        sys.exit(1)

def main():
    ensure_nmap()
    banner()

    network = input("\nEnter Target Network (e.g., 192.168.1.0/24): ")
    scan_info(network)

    print("\n[+] Discovering live hosts...\n")
    hosts = discover_hosts(network)

    if not hosts:
        print("[-] No live hosts found.")
        return

    host_table(hosts)

    final_data = []
    total_open_ports = 0

    for host in hosts:
        ip = host.get("ip")
        print(f"\n[+] Scanning Host: {ip}")

        try:
            ports = scan_ports(ip, COMMON_PORTS)
            if not ports:
                print(f"[-] No open ports found on {ip}.")
                services = {}
            else:
                services = service_scan(ip, ports)
                total_open_ports += len(ports)
                service_table(ip, services)

            final_data.append({
                "ip": ip,
                "mac": host.get("mac"),
                "services": services
            })
        except Exception as e:
            print(f"[!] Error scanning {ip}: {e}")
            continue

    generate_reports(final_data)
    summary(len(hosts), total_open_ports)

    print("\n[✔] Detailed reports saved as scan_report.json and scan_report.csv\n")

if __name__ == "__main__":
    main()
