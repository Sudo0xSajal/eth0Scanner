# port_scanner.py
import socket

def scan_ports(host, ports):
    """
    Scan TCP ports on a host.
    Returns a list of open ports.
    """
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
        except Exception:
            pass
        finally:
            sock.close()
    return open_ports
