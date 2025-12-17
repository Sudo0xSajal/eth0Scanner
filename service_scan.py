# service_scan.py
import nmap

def service_scan(host, ports):
    """
    Enumerate services using Nmap.
    Returns a dictionary: {port: {'name': service_name, 'state': open/closed}}
    """
    services = {}
    if not ports:
        return services

    nm = nmap.PortScanner()
    ports_str = ",".join(str(p) for p in ports)
    scan_result = nm.scan(hosts=host, ports=ports_str, arguments='-sV')

    for port in ports:
        try:
            svc = scan_result['scan'][host]['tcp'][port]
            services[port] = {'name': svc.get('name', ''), 'state': svc.get('state', '')}
        except KeyError:
            services[port] = {'name': '', 'state': 'filtered'}
    return services
