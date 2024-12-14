import Enumeration.BannerGrabbing_NMAP as banner
import Enumeration.OSenumeration_NMAP as OSE
import Enumeration.USERenumeration as USE
import Footprint.footprint_whois as fpwhois
import NetworkScanning.NetworkScan_Ping as NSP
import NetworkScanning.NetworkScanningNMAP as NSN
import GainningAccess.WebScan_nikto as NIK  # Ajout de l'importation

def Display():
    print("\--- Framework SRIE Bonnet Panhelleux Rabier ---/\n")
    print(" -1- Reconnaissance / Footprint")
    print(" -2- Network Scanning")
    print(" -3- Enumeration")
    print(" -4- Gaining Access")
    choice = int(input("Please select the feature you would like to use : "))
    if(choice == 1):
        print(" -1- Social Engineering")
        print(" -2- Reconnaissance")
        choice2 = int(input("Please select a subtask : "))
        if(choice2 == 1) :
            print("DEV")
            return None
        elif(choice2==2):   
            domain = input("Enter the domain to look up: ")
            fpwhois.get_whois(domain)
            return None
        else :
            print(f"No subtask linked to choice number {choice2}")
            return None
    elif(choice==2):
        print(" -1- Network Scan")
        print(" -2- Ports Scan")
        print(" -3- Vulnerabilities Scan")
        choice2 = int(input("Please select a subtask : "))
        if(choice2 == 1) :
            print(" -1- PING")
            print(" -2- NMAP")
            choice3 = int(input("Please select a tool : "))
            if(choice3==1):
                network_prefix = input("Enter a network prefix (ie. 192.168.90) : ")
                start = int(input("Enter the scan's starting host number : "))
                end = int(input("Enter the scan's ending host number : "))
                NSP.Ping_Network(network_prefix, start, end)
                return None
            elif(choice3==2):
                NSN.main_NetworkScanning()
                return None
            else : 
                print(f"No subtask tools to choice number {choice3}")
            return None
        elif(choice2==2):   
            NSN.scan_ports()
            return None
        elif(choice2==3):
            print("Vulnerability scan takes time, this step may take up to 5 minutes")
            NSN.scan_vul()
            return None
        else :
            print(f"No subtask linked to choice number {choice2}")
    elif(choice==3):
        print(" -1- Banner Grabbing")
        print(" -2- OS Enumeration")
        print(" -3- User enumeration")
        choice2 = int(input("Please select a subtask : "))
        if(choice2==1):
            banner.banner_grabbing()
            return None
        elif(choice2==2):
            OSE.OS_enumeration()
            return None
        elif(choice2==3):
            USE.All_enumeration()
            return None
        else :
            print(f"No subtask linked to choice number {choice2}")
            return None
    elif(choice==4):
        NIK.main()
        return None
    else :
        print(f"No tool is implementend on choice n° {choice}")
        return None
    
Display()
