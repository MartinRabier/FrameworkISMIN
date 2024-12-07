# faire pip install python-nmap

import nmap

def OS_enumeration():
    target = input("What is the targeted domain ?")
    try :
        nm = nmap.PortScanner()
        print(f"Scanning OS on {target}...\n")
        nm.scan(hosts=target,arguments ="-O")
        for host in nmap.all_hosts():
            print(f"Host : {host} ({nm[host].hostname()})")
            print(f"State : {nm[host].state}")
            if 'osmatch' in nm[host] :
                print("\-- OS Detected --/")
                for os in nm[host]['osmatch']:
                    print(f"Name : {os['name']}")
                    print(f"Accuracy : {os['accuracy']}%")
                    print(f"OS Type :  {os['osclass'][0]['type'] if os['osclass'] else 'Inconnu'}")
            else : 
                print("No availables data for this OS")
    except Exception as e :
        print(f"Error : {e}")

