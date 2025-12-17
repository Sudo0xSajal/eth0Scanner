# report.py
import json
import csv

def generate_reports(data):
    """
    Generate JSON and CSV reports from scan results.
    """
    # JSON
    with open("scan_report.json", "w") as f:
        json.dump(data, f, indent=4)

    # CSV
    with open("scan_report.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["IP", "MAC", "Port", "Service", "State"])
        for host in data:
            ip = host['ip']
            mac = host['mac']
            for port, svc in host['services'].items():
                writer.writerow([ip, mac, port, svc['name'], svc['state']])
