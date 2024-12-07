#faire un pip install python-whois

import whois

def get_whois():
    domain = input("What website would you like to know more about ?")
    try : 
        info = whois.whois(domain)
        print(info)
        return info
    except Exception as e :
        print(f"Impossible to fetch data from domain : {domain}")
        return None
