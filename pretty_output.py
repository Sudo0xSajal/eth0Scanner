# pretty_output.py
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime

console = Console()

def banner():
    console.print(Panel("[bold green]Ethical | Educational | Authorized Use Only[/bold green]", expand=False))

def scan_info(network):
    console.print(Panel(f"[bold blue]Target Network:[/bold blue] {network}\n[bold blue]Scan Type:[/bold blue] ARP + TCP + Service\n[bold blue]Started At:[/bold blue] {datetime.now()}", expand=False))

def host_table(hosts):
    table = Table(title="Live Hosts Discovered")
    table.add_column("No.", justify="center")
    table.add_column("IP Address", justify="center")
    table.add_column("MAC Address", justify="center")

    for i, host in enumerate(hosts, 1):
        table.add_row(str(i), host['ip'], host['mac'])
    console.print(table)

def service_table(ip, services):
    table = Table(title=f"Services on {ip}")
    table.add_column("Port", justify="center")
    table.add_column("Service Name", justify="center")
    table.add_column("State", justify="center")

    for port, svc in services.items():
        table.add_row(str(port), svc['name'], svc['state'])
    console.print(table)

def summary(total_hosts, total_ports):
    console.print(Panel(f"[bold yellow]Scan Completed[/bold yellow]\nTotal Hosts: {total_hosts}\nTotal Open Ports: {total_ports}"))
