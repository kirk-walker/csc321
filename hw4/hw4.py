
import socket
import pandas as pd

domain = pd.read_csv('domains.tsv', sep = '\t')['domain']


dict = {}
ip = {}
fwd_dict = {}
plot_dict = {}

#Foward DNS lookup
try:
    for domain in domain:
        dict[domain] = socket.getaddrinfo(domain, 443, type = socket.SOCK_STREAM)
        clean_ips = []

        for ip in dict[domain]:
        
            clean_ips.append(ip[4][0])
            fwd_dict[domain] = clean_ips
        

except:
    print("n/a")
    pass

#Reverse DNS lookup
for key in fwd_dict:
    rev_dns = []

    for ip in fwd_dict[key]:
        try:
            
            rev_dns.append(socket.gethostbyaddr(str(ip))[0]) 
            plot_dict[key] = rev_dns
            print(plot_dict)

        except:
            print('n/a')
            pass        


print(plot_dict)