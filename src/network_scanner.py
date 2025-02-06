import scapy.all as scapy


class NetworkScanner:
    def __init__(self, target_ip):
        self.target_ip = target_ip

    def scan(self):
        """Escanea la red en busca de dispositivos activos."""
        arp_request = scapy.ARP(pdst=self.target_ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        devices = []
        for answer in answered_list:
            devices.append({"IP": answer[1].psrc, "MAC": answer[1].hwsrc})

        return devices
