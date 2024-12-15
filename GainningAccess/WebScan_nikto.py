import subprocess
import time

def nikto_scan():
    target_url = input("Enter the target URL: ")
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        print("Invalid URL format. Please include 'http://' or 'https://'.")
        return
    nikto_command = ["nikto", "-h", target_url]
    try:
        print("Starting Nikto scan. This may take a while...")
        result = subprocess.run(nikto_command, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error running Nikto scan: {e}")


