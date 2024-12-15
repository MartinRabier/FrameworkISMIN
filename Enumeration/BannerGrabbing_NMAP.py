import nmap

def banner_grabbing(port_range="1-1000"):
    print("This feature uses Nmap to grab banners thanks to the command \"-Sv\" which scans open ports and try to determine running services")
    target = input("What is the targeted domain ?")
    try:
        nm = nmap.PortScanner()
        print(f"Scanning {target} on ports {port_range}...\n")
        nm.scan(hosts=target, ports=port_range, arguments="-sV")
        for host in nm.all_hosts():
            print(f"Host : {host} ({nm[host].hostname()})")
            print(f"State : {nm[host].state()}")
            for proto in nm[host].all_protocols():
                print(f"Protocol : {proto}")
                ports = nm[host][proto].keys()
                for port in sorted(ports):
                    service = nm[host][proto][port]
                    print(f"Port : {port} | State : {service['state']} | Service : {service.get('name')} | Version : {service.get('version')}")
    except Exception as e:
        print(f"Error : {e}")