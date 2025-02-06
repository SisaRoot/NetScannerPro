import socket


class PortScanner:
    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.ports = range(1, 65536)  # Escanear todos los puertos del 1 al 65535

    def scan_ports(self):
        """Escanea todos los puertos posibles en un dispositivo."""
        open_ports = []
        for port in self.ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((self.target_ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()

        return open_ports
