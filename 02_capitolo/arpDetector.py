from scapy.all import sniff
IP_MAC_Map = {}     # dizionario che contiene le coppie MAC IP fino ad ora intercettate


def processPacket(packet):
    src_IP = packet['ARP'].psrc
    src_MAC = packet['Ether'].src
    if src_MAC in IP_MAC_Map.keys():            # abbiamo già intercettato un pacchetto con questo indirizzo MAC?
        if IP_MAC_Map[src_MAC] != src_IP:       # gli indirizzi IP sono diversi?
            try:
                old_IP = IP_MAC_Map[src_MAC]
            except:
                old_IP = 'unknown'
            message = ("\n Possible ARP attack detected \n"
                        + "It is possible that the machine with IP address \n"
                        + str(old_IP) + " is pretending to be " + str(src_IP)
                        + "\n")

            return message
    else:                                       # mappiamo l'indirizzo MAC con corrispondente indirizzo IP
        IP_MAC_Map[src_MAC] = src_IP

# count=0 indica di sniffare tutti i pacchetti
sniff(count=0, filter="arp", store = 0, prn = processPacket)