import scapy.all as scapy


class OSDetector:
    def __init__(self, target_ip):
        self.target_ip = target_ip

    def detect_os(self):
        """Intenta identificar el sistema operativo del dispositivo."""
        try:
            response = scapy.sr1(scapy.IP(dst=self.target_ip) / scapy.ICMP(), timeout=1, verbose=False)
            if response:
                ttl = response.ttl
                if ttl <= 64:
                    return "Posible Linux/Unix"
                elif ttl <= 128:
                    return "Posible Windows"
                else:
                    return "Desconocido"
            return "No se recibió respuesta"
        except:
            return "Error al detectar OS"
