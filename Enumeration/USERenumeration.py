import nmap
import subprocess

def SMB_enumeration():
    target = input("What is the targeted domain ?")
    try:
        nm = nmap.PortScanner()
        print(f"Enumerating SMB/Windows users on target : {target}")
        scan_command = ['sudo', 'nmap', '--script=smb-enum-users.nse', '-p', '445', target]
        result = subprocess.run(scan_command, capture_output=True, text=True)
        print(result.stdout)  # Affiche la sortie complète de Nmap pour le débogage
        nm.analyse_nmap_xml_scan(result.stdout)
        for host in nm.all_hosts():
            print(f"Host : {host} ({nm[host].hostname()})")
            print(f"State : {nm[host].state()}")
            if 'script' in nm[host] and 'smb-enum-users' in nm[host]['script']:
                print("SMB/Windows user detected--/")
                print(nm[host]['script']['smb-enum-users'])
            else:
                print("No SMB/Windows users were detected during the scan")
    except Exception as e:
        print(f"Error : {e}")

def SSH_enumeration():
    target = input("What is the targeted domain ?")
    try:
        nm = nmap.PortScanner()
        print(f"Enumerating SSH users on target : {target}")
        scan_command = ['sudo', 'nmap', '--script=ssh-auth-methods', '-p', '22', target]
        result = subprocess.run(scan_command, capture_output=True, text=True)
        print(result.stdout)  # Affiche la sortie complète de Nmap pour le débogage
        nm.analyse_nmap_xml_scan(result.stdout)
        for host in nm.all_hosts():
            print(f"Host : {host} ({nm[host].hostname()})")
            print(f"State : {nm[host].state()}")
            if 'script' in nm[host] and 'ssh-auth-methods' in nm[host]['script']:
                print("SSH authentication methods detected--/")
                print(nm[host]['script']['ssh-auth-methods'])
            else:
                print("No SSH authentication methods were detected during the scan")
    except Exception as e:
        print(f"Error : {e}")

def RDP_enumeration():
    target = input("What is the targeted domain ?")
    try:
        nm = nmap.PortScanner()
        print(f"Enumerating RDP users on target : {target}")
        scan_command = ['sudo', 'nmap', '--script=rdp-enum-encryption', '-p', '3389', target]
        result = subprocess.run(scan_command, capture_output=True, text=True)
        print(result.stdout)  # Affiche la sortie complète de Nmap pour le débogage
        nm.analyse_nmap_xml_scan(result.stdout)
        for host in nm.all_hosts():
            print(f"Host : {host} ({nm[host].hostname()})")
            print(f"State : {nm[host].state()}")
            if 'script' in nm[host] and 'rdp-enum-encryption' in nm[host]['script']:
                print("RDP user detected--/")
                print(nm[host]['script']['rdp-enum-encryption'])
            else:
                print("No RDP users were detected during the scan")
    except Exception as e:
        print(f"Error : {e}")

def All_enumeration():
    print("Select enumeration type:")
    print("1. SMB Enumeration")
    print("2. SSH Enumeration")
    print("3. RDP Enumeration")
    choice = input("Enter your choice: ")
    if choice == "1":
        SMB_enumeration()
    elif choice == "2":
        SSH_enumeration()
    elif choice == "3":
        RDP_enumeration()
    else:
        print("Invalid choice")