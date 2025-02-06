from src.network_scanner import NetworkScanner
from src.port_scanner import PortScanner
from src.os_detector import OSDetector
from src.vulnerability_scan import VulnerabilityScanner


def main():
    target_network = input("Introduce el rango de red a escanear (Ej. 192.168.1.0/24): ")

    print("[*] Escaneando la red...")
    scanner = NetworkScanner(target_network)
    devices = scanner.scan()

    for device in devices:
        ip = device["IP"]
        mac = device["MAC"]
        print(f"\nDispositivo encontrado: {ip} - {mac}")

        print("[*] Escaneando puertos abiertos...")
        port_scanner = PortScanner(ip)
        open_ports = port_scanner.scan_ports()
        print(f"Puertos abiertos: {open_ports}")

        print("[*] Detectando sistema operativo...")
        os_detector = OSDetector(ip)
        os_name = os_detector.detect_os()
        print(f"Sistema operativo: {os_name}")

        print("[*] Analizando posibles vulnerabilidades...")
        vulnerability_scanner = VulnerabilityScanner(open_ports)
        vulnerabilities = vulnerability_scanner.check_vulnerabilities()
        for port, vuln in vulnerabilities.items():
            print(f"[!] Vulnerabilidad detectada en el puerto {port}: {vuln}")


if __name__ == "__main__":
    main()
