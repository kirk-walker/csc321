#imports
import netifaces
import ipaddress

interface = netifaces.interfaces()

# Get IP configuration with 'ipconfig'
# get interfaces on machine

def get_interfaces():
    print('Interfaces: \n')
    return netifaces.interfaces()


# get mac address for given interface

def get_mac(interface):
    my_interface = netifaces.ifaddresses(interface)
    mac_address = my_interface[netifaces.AF_LINK][0]['addr']
    return mac_address


#get ip for given interface

def get_ips(interface):
    interface = netifaces.interfaces()
    ip_dict = {}

    try: 
        ipv6 = netifaces.ifaddresses(interface)[netifaces.AF_INET6][0]['addr']
        ip_dict["ipv6"] = ipv6
    except: 
        print('no ipv6')
    try:
        ipv4 = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
        ip_dict["ipv4"] = ipv4
    except: 
        print('no ipv4')

    return ip_dict

# get netmask for given interface

def get_netmask(interface):
    interface = netifaces.interfaces()
    netmask_dict = {}

    try: 
        ipv6 = netifaces.ifaddresses(interface)[netifaces.AF_INET6][0]['netmask']
        netmask_dict["ipv6"] = ipv6
    except: 
        print('no ipv6 netmask')
    try:
        ipv4 = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
        netmask_dict["ipv4"] = ipv4
    except: 
        print('no ipv4')

    return netmask_dict