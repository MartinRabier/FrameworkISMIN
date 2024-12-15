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
    except Exception as e:
        print(f"Error : {e}")

def SSH_enumeration():
    target = input("What is the targeted domain ?")
    try:
        nm = nmap.PortScanner()
        print(f"Enumerating SSH users on target : {target}")
        scan_command = ['sudo', 'nmap', '--script=smtp-enum-users.nse', '-p', '25', target]
        result = subprocess.run(scan_command, capture_output=True, text=True)
        print(result.stdout)  # Affiche la sortie complète de Nmap pour le débogage
    except Exception as e:
        print(f"Error : {e}")

def RDP_enumeration():
    target = input("What is the targeted domain ?")
    try:
        nm = nmap.PortScanner()
        print(f"Enumerating RDP users on target : {target}")
        scan_command = ['sudo', 'nmap', '--script=rdp-enum-encryption.nse', '-p', '3389', target]
        result = subprocess.run(scan_command, capture_output=True, text=True)
        print(result.stdout)  # Affiche la sortie complète de Nmap pour le débogage
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