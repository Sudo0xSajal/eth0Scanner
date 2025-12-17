# host_discovery.py
from scapy.all import ARP, Ether, srp

def discover_hosts(network):
    """
    Discover live hosts on the given network using ARP requests.
    Returns a list of dictionaries: [{'ip': ip, 'mac': mac}, ...]
    """
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=0)[0]

    hosts = []
    for sent, received in result:
        hosts.append({"ip": received.psrc, "mac": received.hwsrc})
    return hosts
