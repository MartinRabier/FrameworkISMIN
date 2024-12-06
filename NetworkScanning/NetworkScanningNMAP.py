import subprocess
import socket
import ipaddress
import psutil
import requests

def get_private_ip_and_subnet():
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                return addr.address, addr.netmask
    return None, None

def scan_network(ip, subnet):

    network = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False)
    print(network)
    scan_command = ["C:\\Program Files (x86)\\Nmap\\nmap.exe", "-sn", str(network)]
    result = subprocess.run(scan_command, capture_output=True, text=True,shell=True)
    return result.stdout

def scan_ports(ip):
    
    scan_command = ["C:\\Program Files (x86)\\Nmap\\nmap.exe","-sV", ip]
    result = subprocess.run(scan_command, capture_output=True, text=True,shell=True)
    return result.stdout

def scan_ports_Vulscan(ip):
    
    scan_command = ["C:\\Program Files (x86)\\Nmap\\nmap.exe","-sV","--script=vulscan", ip]
    result = subprocess.run(scan_command, capture_output=True, text=True,shell=True,timeout = 60)
    if result.stderr:
        print(f"Error running Nmap: {result.stderr}")
    return result.stdout



def main_NetworkScanning():
    ip, subnet = get_private_ip_and_subnet()
    if not ip or not subnet:
        print("Could not determine IP or subnet.")
        return
    print(f"Private IP: {ip}")
    print(f"Subnet Mask: {subnet}")

    print("\nScanning network for active devices...")
    devices = scan_network("192.168.31.0", subnet)
    print(devices)

    print("\nScanning ports for detected devices...")
    for line in devices.splitlines():
        if "Nmap scan report for" in line:
            detected_ip = line.split()[-1]
            print(f"\nScanning ports on {detected_ip}...")
            ports = scan_ports(detected_ip)
            ports_vuln = scan_ports_Vulscan(detected_ip)
            print("Flag getter")
            print(ports)
            print("Vulnerability Check")
            print(ports_vuln)
            
main_NetworkScanning()
