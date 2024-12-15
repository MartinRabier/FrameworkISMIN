#faire un pip install python-whois

import whois

def get_whois():
    print("This function will get whois information from a domain.")
    print("\nWhois is a widely used Internet record listing that identifies who owns a domain and how to get in contact with them. \n Whois information may include the domain's owner, address, phone number, and email address.")
    print(" \n Please enter the domain you want to get whois information from. Example: emse.fr")
    domain = input("Enter the domain you want to get whois information: ")
    try : 
        info = whois.whois(domain)
        print(info)
        return info
    except Exception as e :
        print(f"Impossible to fetch data from domain : {domain}")
        return None
