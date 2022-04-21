Initially I started both nodes 00 and 01, I then opened another node00
and ran tcpdump -ni 1 to see if I got the correct information.

For writing the .pcap files I used the command

    tcpdump -ni 1 -w hwserver.pcap

For full-take.pcap, I used

    mergecap -w full-take.pcap hwserver.pcap hwclient.pcap taskwork.pcap taskvent.pcap tasksink.pcap

To get the information from the specific servers I used

    tcpdump -n -r full-take.pcap port 5558 or port 5557 -w task.pcap
    tcpdump -n -r full-take.pcap port 5555 -w weather.pcap