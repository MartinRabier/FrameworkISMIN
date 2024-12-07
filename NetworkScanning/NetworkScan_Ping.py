import subprocess
import platform
from multiprocessing import Pool

def Ping_single():
    ip = input("Specifiy an IP adress to ping : ")
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping',param,1,ip]
    try :
        subprocess.run(command,stdout=subprocess.DEVNULL,stderr = subprocess.DEVNULL, check = True)
        return ip
    except subprocess.CalledProcessError :
        return None
    
def Ping_Network():
    network_prefix = input("Enter a network prefix (ie. 198.35.1) : ")
    start = input("Enter the scan's starting host number : ")
    end = input("Enter the scan's ending host number : ")
    ips = [f"{network_prefix}.{i}" for i in range(start,end+1)]
    print(f"Scanning Network {network_prefix}.0/24 in parallel ...\n")
    with Pool(processes=10) as pool:
        results = pool.map(Ping_single,ips)
    active_hosts = [ip for ip in results if ip]
    print("Scans completed")
    print("Active hosts : ")
    for host in active_hosts :
        print(f"- {host}")
    return active_hosts