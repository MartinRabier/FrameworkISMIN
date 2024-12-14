import subprocess
import socket
import ipaddress
import psutil

def get_private_ip_and_subnet():
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                return addr.address, addr.netmask
    return None, None

def scan_network():
    ip = input("Enter the IP you want to scan (example: 192.168.34.0) : ")
    subnet = "255.255.255.0"
    network = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False)
    print(network)
    scan_command = ['sudo', 'nmap', '-sn', str(network)]
    result = subprocess.run(scan_command, capture_output=True, text=True)
    print(result.stdout)
    return ip,result.stdout

#scan_network()

def scan_ports():
    ip = input("Enter the IP you want to scan (example: 192.168.34.0) : ")
    subnet = "255.255.255.0"
    network = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False)
    print(network)
    scan_command = ['sudo', 'nmap', '-sn', str(network)]
    devices = subprocess.run(scan_command, capture_output=True, text=True)
    for line in devices.stdout.splitlines():
        if "Nmap scan report for" in line:
            detected_ip = line.split()[-1]
            print(f"\nScanning ports on {detected_ip}...")
            scan_command = ['sudo','nmap', '-sV', detected_ip]
            ports = subprocess.run(scan_command, capture_output=True, text=True)
            print("Ports scan results:")
            print(ports.stdout)
    return None

#scan_ports()

def scan_vul():
    """
    Fonction pour scanner les vulnérabilités sur les appareils actifs du réseau.
    """
    ip = input("Enter the IP you want to scan (example: 192.168.34.0) : ")
    subnet = "255.255.255.0"
    network = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False)
    print(f"Scanning network: {network}")

    # Scan réseau pour détecter les appareils actifs
    scan_command = ['sudo', 'nmap', '-sn', str(network)]
    devices = subprocess.run(scan_command, capture_output=True, text=True)

    if devices.returncode != 0:
        print(f"Error during network scan: {devices.stderr}")
        return

    # Extraction des IP actives
    active_ips = []
    for line in devices.stdout.splitlines():
        if "Nmap scan report for" in line:
            detected_ip = line.split()[-1]
            active_ips.append(detected_ip)

    # Scan des vulnérabilités pour chaque IP détectée
    for detected_ip in active_ips:
        print(f"\nScanning vulnerabilities on {detected_ip}...")
        scan_command = ['sudo', 'nmap', '-sV', '--script=vulscan', detected_ip]
        ports = subprocess.run(scan_command, capture_output=True, text=True)

        if ports.returncode != 0:
            print(f"Error during vulnerability scan on {detected_ip}: {ports.stderr}")
            continue

        print("Vulnerability scan results:")
        print(ports.stdout)

