# faire pip install python-nmap

import nmap

def SMB_enumeration():
    target = input("What is the targeted domain ?")
    try :
        nm = nmap.PortScanner()
        print(f"Enumerating SMB/Windows users on target : {target}")
        nm.scan(hosts=target,arguments="--script=smb-enum-users -p 445")
        for host in nm.all_hosts() :
            print(f"Host : {host} ({nm[host].hostname()})")
            print(f"State : {nm[host].state}")
            if 'script' in nm[host] and 'smb-enum-users' in nm[host]['script']:
                print("SMB/Windows user detected--/")
                print(nm[host]['script']['smb-enum_users'])
            else :
                print("No SMB/Windows users were detected during the scan")
    except Exception as e:
        print(f"Error : {e}")

def SSH_enumeration():
    target = input("What is the targeted domain ?")
    try :
        nm = nmap.PortScanner()
        print(f"Enumerating SSH users on target : {target}")
        nm.scan(hosts=target,arguments="--script=ssh2-enum-users -p 22")
        for host in nm.all_hosts() :
            print(f"Host : {host} ({nm[host].hostname()})")
            print(f"State : {nm[host].state}")
            if 'script' in nm[host] and 'ssh2-enum-users' in nm[host]['script']:
                print("SSH user detected--/")
                print(nm[host]['script']['ssh2-enum_users'])
            else :
                print("No SSH users were detected during the scan")
    except Exception as e:
        print(f"Error : {e}")

def RDP_enumeration():
    target = input("What is the targeted domain ?")
    try :
        nm = nmap.PortScanner()
        print(f"Enumerating RDP users on target : {target}")
        nm.scan(hosts=target,arguments="--script=rdp-enum_encryption -p 3389")
        for host in nm.all_hosts() :
            print(f"Host : {host} ({nm[host].hostname()})")
            print(f"State : {nm[host].state}")
            if 'script' in nm[host] and 'rdp-enum-encryption' in nm[host]['script']:
                print("RDP user detected--/")
                print(nm[host]['script']['rdp-enum-encryption'])
            else :
                print("No RDP users were detected during the scan")
    except Exception as e:
        print(f"Error : {e}")

def HTTP_enumeration():
    target = input("What is the targeted domain ?")
    try :
        nm = nmap.PortScanner()
        print(f"Enumerating HTTP users on target : {target}")
        nm.scan(hosts=target,arguments="--script=http-enum -p 80,443")
        for host in nm.all_hosts() :
            print(f"Host : {host} ({nm[host].hostname()})")
            print(f"State : {nm[host].state}")
            if 'script' in nm[host] and 'http-enum' in nm[host]['script']:
                print("HTTP user detected--/")
                print(nm[host]['script']['http-enum'])
            else :
                print("No HTTP users were detected during the scan")
    except Exception as e:
        print(f"Error : {e}")

def All_enumeration():
    print("Proceeding to all sort of users enumeration")
    SMB_enumeration()

    