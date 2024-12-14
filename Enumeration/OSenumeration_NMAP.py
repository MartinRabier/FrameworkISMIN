import nmap
import subprocess

def OS_enumeration():
    target = input("What is the targeted domain ?")
    try:
        nm = nmap.PortScanner()
        print(f"Scanning OS on {target}...\n")
        # Utilisation de sudo pour exécuter la commande nmap avec des privilèges root et obtenir la sortie en XML
        scan_command = ['sudo', 'nmap', '-O', '-oX', '-', target]
        result = subprocess.run(scan_command, capture_output=True, text=True)
        nm.analyse_nmap_xml_scan(result.stdout)
        for host in nm.all_hosts():
            print(f"Host : {host} ({nm[host].hostname()})")
            print(f"State : {nm[host].state()}")
            if 'osmatch' in nm[host]:
                print("\-- OS Detected --/")
                for os in nm[host]['osmatch']:
                    print(f"Name : {os['name']}")
                    print(f"Accuracy : {os['accuracy']}%")
                    print(f"OS Type :  {os['osclass'][0]['type'] if os['osclass'] else 'Inconnu'}")
            else:
                print("No available data for this OS")
    except Exception as e:
        print(f"Error : {e}")