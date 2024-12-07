import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

import Enumeration.BannerGrabbing_NMAP as banner
import Enumeration.OSenumeration_NMAP as OSE
import Enumeration.USERenumeration as USE
import Footprint.footprint_whois as fpwhois
import NetworkScanning.NetworkScan_Ping as NSP
import NetworkScanning.NetworkScanningNMAP as NSN
import GainningAccess.WebScan_nikto as NIK

class FrameworkInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Framework SRIE Bonnet Panhelleux Rabier")
        self.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        self.clear_frame()
        tk.Label(self, text="Framework SRIE Bonnet Panhelleux Rabier", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(self, text="Reconnaissance / Footprint", command=self.reconnaissance_menu).pack(pady=5)
        tk.Button(self, text="Network Scanning", command=self.network_scanning_menu).pack(pady=5)
        tk.Button(self, text="Enumeration", command=self.enumeration_menu).pack(pady=5)
        tk.Button(self, text="Gaining Access", command=self.gaining_access_menu).pack(pady=5)
        self.output_text = tk.Text(self, wrap=tk.WORD, height=10)
        self.output_text.pack(pady=10)

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def display_output(self, text):
        self.output_text.insert(tk.END, text + "\n")
        self.output_text.see(tk.END)

    def reconnaissance_menu(self):
        self.clear_frame()
        tk.Label(self, text="Reconnaissance / Footprint", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Whois Lookup", command=self.whois_lookup).pack(pady=5)
        tk.Button(self, text="Back", command=self.create_widgets).pack(pady=5)

    def whois_lookup(self):
        domain = tk.simpledialog.askstring("Input", "What website would you like to know more about?")
        if domain:
            info = fpwhois.get_whois(domain)
            self.display_output(str(info))

    def network_scanning_menu(self):
        self.clear_frame()
        tk.Label(self, text="Network Scanning", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Ping Network", command=self.ping_network).pack(pady=5)
        tk.Button(self, text="Nmap Network Scan", command=self.nmap_network_scan).pack(pady=5)
        tk.Button(self, text="Ports Scan", command=self.ports_scan).pack(pady=5)
        tk.Button(self, text="Vulnerabilities Scan", command=self.vulnerabilities_scan).pack(pady=5)
        tk.Button(self, text="Back", command=self.create_widgets).pack(pady=5)

    def ping_network(self):
        network_prefix = tk.simpledialog.askstring("Input", "Enter a network prefix (ie. 198.35.1):")
        start = tk.simpledialog.askinteger("Input", "Enter the scan's starting host number:")
        end = tk.simpledialog.askinteger("Input", "Enter the scan's ending host number:")
        if network_prefix and start is not None and end is not None:
            active_hosts = NSP.Ping_Network(network_prefix, start, end)
            self.display_output(f"Active hosts: {', '.join(active_hosts)}")

    def nmap_network_scan(self):
        ip = tk.simpledialog.askstring("Input", "Enter the IP address to scan:")
        subnet = tk.simpledialog.askstring("Input", "Enter the subnet mask:")
        if ip and subnet:
            result = NSN.scan_network(ip, subnet)
            self.display_output(result)

    def ports_scan(self):
        ip = tk.simpledialog.askstring("Input", "Enter the IP address to scan:")
        if ip:
            result = NSN.scan_ports(ip)
            self.display_output(result)

    def vulnerabilities_scan(self):
        ip = tk.simpledialog.askstring("Input", "Enter the IP address to scan:")
        if ip:
            result = NSN.scan_ports_Vulscan(ip)
            self.display_output(result)

    def enumeration_menu(self):
        self.clear_frame()
        tk.Label(self, text="Enumeration", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Banner Grabbing", command=self.banner_grabbing).pack(pady=5)
        tk.Button(self, text="OS Enumeration", command=self.os_enumeration).pack(pady=5)
        tk.Button(self, text="User Enumeration", command=self.user_enumeration).pack(pady=5)
        tk.Button(self, text="Back", command=self.create_widgets).pack(pady=5)

    def banner_grabbing(self):
        target = tk.simpledialog.askstring("Input", "What is the targeted domain?")
        if target:
            result = banner.banner_grabbing(target)
            self.display_output(result)

    def os_enumeration(self):
        target = tk.simpledialog.askstring("Input", "What is the targeted domain?")
        if target:
            result = OSE.OS_enumeration(target)
            self.display_output(result)

    def user_enumeration(self):
        result = USE.All_enumeration()
        self.display_output(result)

    def gaining_access_menu(self):
        self.clear_frame()
        tk.Label(self, text="Gaining Access", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Web Scan (Nikto)", command=self.web_scan_nikto).pack(pady=5)
        tk.Button(self, text="Back", command=self.create_widgets).pack(pady=5)

    def web_scan_nikto(self):
        target_url = tk.simpledialog.askstring("Input", "Enter the target URL:")
        if target_url:
            result = NIK.nikto_scan(target_url)
            self.display_output(result)

if __name__ == "__main__":
    app = FrameworkInterface()
    app.mainloop()