# pretty_output.py
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
from datetime import datetime

console = Console()

# ───────────────────── BANNER ─────────────────────
def banner():
    banner_text = Text("""
 ███████╗████████╗██╗  ██╗ ██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗
 ██╔════╝╚══██╔══╝██║  ██║██╔═══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
 █████╗     ██║   ███████║██║   ██║███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
 ██╔══╝     ██║   ██╔══██║██║   ██║╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
 ███████╗   ██║   ██║  ██║╚██████╔╝███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
 ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
""", style="bold cyan")

    console.print(
        Panel(
            banner_text,
            box=box.DOUBLE,
            title="[bold white]⚡ eth0Scanner ⚡[/bold white]",
            subtitle="[bold green]☠ Sajal Haldar | @Sudo0xSajal | Authorized Use Only ☠[/bold green]"
        )
    )

# ───────────────────── SCAN INFO ─────────────────────
def scan_info(network):
    console.print(
        Panel(
            f"[bold green]➜ TARGET[/bold green]  [bold cyan]{network}[/bold cyan]\n"
            f"[bold green]➜ MODE[/bold green]    ARP + TCP + SERVICE ENUM\n"
            f"[bold green]➜ STARTED[/bold green] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            box=box.HEAVY,
            title="[bold magenta]⚙ SCAN INITIALIZED[/bold magenta]"
        )
    )

# ───────────────────── HOST TABLE ─────────────────────
def host_table(hosts):
    table = Table(
        title="[bold green]☠ LIVE HOSTS DISCOVERED ☠[/bold green]",
        box=box.HEAVY_EDGE,
        header_style="bold cyan"
    )
    table.add_column("#", justify="center", style="bold white")
    table.add_column("IP ADDRESS", style="bold green")
    table.add_column("MAC ADDRESS", style="bold yellow")

    for i, host in enumerate(hosts, 1):
        table.add_row(f"[cyan]{i}[/cyan]", host['ip'], host['mac'])

    console.print(table)

# ───────────────────── SERVICE TABLE ─────────────────────
def service_table(ip, services):
    table = Table(
        title=f"[bold red]⚡ SERVICES ON {ip} ⚡[/bold red]",
        box=box.DOUBLE_EDGE,
        header_style="bold magenta"
    )
    table.add_column("PORT", justify="center", style="bold cyan")
    table.add_column("SERVICE", style="bold green")
    table.add_column("STATE", style="bold red")

    for port, svc in services.items():
        state_color = "green" if svc['state'] == "open" else "red"
        table.add_row(
            str(port),
            svc['name'],
            f"[bold {state_color}]{svc['state']}[/bold {state_color}]"
        )

    console.print(table)

# ───────────────────── SUMMARY ─────────────────────
def summary(total_hosts, total_ports):
    console.print(
        Panel(
            f"[bold green]✔ OPERATION COMPLETE[/bold green]\n\n"
            f"[bold cyan]➜ HOSTS COMPROMISED:[/bold cyan] {total_hosts}\n"
            f"[bold magenta]➜ OPEN PORTS FOUND:[/bold magenta] {total_ports}",
            box=box.DOUBLE,
            title="[bold green]☠ MISSION STATUS ☠[/bold green]"
        )
    )
