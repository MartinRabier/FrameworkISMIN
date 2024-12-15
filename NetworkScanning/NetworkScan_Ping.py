import subprocess
#à modifier donnees dans le display
def Ping_Network():
    print("Ping is a simple tool to verify the connectivity between two devices.")
    print("\nYou have to provide the network prefix which is the first three octets of the IP address.")
    print("\nThen you have to provide the starting and ending IP addresses to scan.\n Usually starting IP address is 1 and ending IP address is 255 if you want to scan the whole network.")
    network_prefix = input("Enter a network prefix (ie. 192.168.90) : ")
    start = int(input("Enter the starting IP address (ie. 1) : "))
    end = int(input("Enter the ending IP address (ie. 254) : "))
    start_ip = f"{network_prefix}.{start}"
    end_ip = f"{network_prefix}.{end}"
    
    print(f"Scanning Network {network_prefix}.0/24 with fping from {start_ip} to {end_ip}...\n")
    
    command = ['fping', '-a', '-q', '-g', start_ip, end_ip]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        active_hosts = result.stdout.splitlines()
        print("Scans completed")
        print("Active hosts : ")
        for host in active_hosts:
            print(f"- {host}")
        return active_hosts
    except subprocess.CalledProcessError as e:
        # Handle the case where fping returns a non-zero exit status
        active_hosts = e.stdout.splitlines()
        if active_hosts:
            print("Active hosts : ")
            for host in active_hosts:
                print(f"- {host}")
            return active_hosts
        else:
            print(f"Error running fping: {e}")
            print(f"Standard Output: {e.stdout}")
            print(f"Standard Error: {e.stderr}")
            return []

