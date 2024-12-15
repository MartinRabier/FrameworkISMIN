from django.shortcuts import render
from .utils.NetworkScanning.NetworkScanningNMAP import scan_network, scan_ports, scan_vul
from .utils.GainningAccess.hydra import brute_force
from .utils.GainningAccess.backdoor_exploit import exploit_vsftpd
from .utils.Footprint.Scrapping import html_site
from .utils.Footprint.footprint_whois import get_whois
from .utils.Enumeration.USERenumeration import SMB_enumeration, SSH_enumeration, RDP_enumeration, All_enumeration
from .utils.Enumeration.OSenumeration_NMAP import OS_enumeration
from .utils.Enumeration.BannerGrabbing_NMAP import banner_grabbing
from .templates import function1, function2  # Import your functions

def index(request):
    context = {}
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'scan_network':
            context['result'] = scan_network()
        elif action == 'scan_ports':
            context['result'] = scan_ports()
        elif action == 'scan_vul':
            context['result'] = scan_vul()
        elif action == 'brute_force':
            context['result'] = brute_force()
        elif action == 'exploit_vsftpd':
            context['result'] = exploit_vsftpd()
        elif action == 'html_site':
            context['result'] = html_site()
        elif action == 'get_whois':
            domain = request.POST.get('domain')
            context['result'] = get_whois(domain)
        elif action == 'SMB_enumeration':
            context['result'] = SMB_enumeration()
        elif action == 'SSH_enumeration':
            context['result'] = SSH_enumeration()
        elif action == 'RDP_enumeration':
            context['result'] = RDP_enumeration()
        elif action == 'All_enumeration':
            context['result'] = All_enumeration()
        elif action == 'OS_enumeration':
            context['result'] = OS_enumeration()
        elif action == 'banner_grabbing':
            context['result'] = banner_grabbing()
    return render(request, 'index.html', context)

def function1_view(request):
    result = function1()
    return render(request, 'function1.html', {'result': result})

def function2_view(request):
    result = function2()
    return render(request, 'function2.html', {'result': result})

# Add more views for other functions as needed