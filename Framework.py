import Enumeration.BannerGrabbing_NMAP as banner
import Enumeration.OSenumeration_NMAP as OSE
import Enumeration.USERenumeration as USE
import Footprint.footprint_whois as fpwhois
import NetworkScanning.NetworkScan_Ping as NSP
import NetworkScanning.NetworkScanningNMAP as NSN
import GainningAccess.hydra as HY
import GainningAccess.backdoor_exploit as BE
import Footprint.Scrapping as SCR
import GainningAccess.metasploit as MET

def Display():
    print("\--- Framework SRIE Bonnet Panhelleux Rabier ---/\n")
    print("This framework allows you to use easily different kind of cybersecurity tools\n")
    print(" [-1-] Reconnaissance / Footprint")
    print(" [-2-] Network Scanning")
    print(" [-3-] Enumeration")
    print(" [-4-] Gaining Access")
    print(" [-5-] Exit framework")
    choice = int(input("Please select a field above : \n"))
    if(choice == 1):
        print("\-- Bellow are some tools to get data from websites --/\n")
        print(" -1- HTML Scrapping")
        print(" -2- Reconnaissance")
        choice2 = int(input("Please select a subtask : \n"))
        if(choice2 == 1) :
            SCR.html_site()
            Display()
        elif(choice2==2):   
            fpwhois.get_whois()
            Display()
        else :
            print(f"No subtask linked to choice n°{choice2}\n")
            Display()
    elif(choice==2):
        print("\-- Bellow are some tools to get information on a network and its ports --/\n")
        print(" -1- Network Scan")
        print(" -2- Ports Scan")
        print(" -3- Vulnerabilities Scan")
        choice2 = int(input("Please select a subtask : \n"))
        if(choice2 == 1) :
            print("\-- Here are two different ways to perform a network scan --/\n")
            print(" -1- PING")
            print(" -2- NMAP")
            choice3 = int(input("Please select a tool : \n"))
            if(choice3==1):
                NSP.Ping_Network()
                Display()
            elif(choice3==2):
                NSN.scan_network()
                Display() 
            else : 
                print(f"No tool linked to choice n°{choice3}\n")
                Display()
        elif(choice2==2):   
            NSN.scan_ports()
            Display()
        elif(choice2==3):
            NSN.scan_vul()
            Display()
        else :
            print(f"No subtask linked to choice n°{choice2}\n")
            Display()
    elif(choice==3):
        print("\-- Bellow are some tools to grab banners or enumerate information --/\n")
        print(" -1- Banner Grabbing")
        print(" -2- OS Enumeration")
        print(" -3- User enumeration")
        choice2 = int(input("Please select a subtask : \n"))
        if(choice2==1):
            banner.banner_grabbing()
            Display()
        elif(choice2==2):
            OSE.OS_enumeration()
            Display()
        elif(choice2==3):
            USE.All_enumeration()
            Display()
        else :
            print(f"No subtask linked to choice n°{choice2}\n")
            Display()
    elif(choice==4):
        print("\-- Bellow are some tools to gain access on vulnerable ports --/\n")
        print(" -1- Bruteforce Hydra" )
        print(" -2- Manual backdoor exploit")
        print(" -3- Metasploit backdoor exploit")
        choice2 = int(input("Please select a tool : \n"))
        if(choice2==1):
            HY.brute_force()
            Display()
        elif(choice2==2):
            BE.exploit_vsftpd()
            Display()
        elif(choice2==3):
            MET.metasploit()
            Display()
        else :
            print(f"No tool is implementend on choice n°{choice}")
            Display()
    elif(choice==5):
        print("Thanks for using or cybersecurity framework\n")
        print("[*] Exiting Framework [*]\n")
        print(" See U L8er ;)\n")
        return None
    
    else:
        print(f"No field linked to choice n°{choice}\n")
        Display()
    
Display()