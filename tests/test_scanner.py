import unittest
from src.network_scanner import NetworkScanner


class TestNetworkScanner(unittest.TestCase):
    def test_scan(self):
        """Prueba básica del escaneo de red."""
        scanner = NetworkScanner("192.168.1.0/24")
        devices = scanner.scan()

        # Verifica que la salida sea una lista
        self.assertIsInstance(devices, list)

        # Si hay dispositivos en la red, deben tener IP y MAC
        if devices:
            self.assertIn("IP", devices[0])
            self.assertIn("MAC", devices[0])


if __name__ == "__main__":
    unittest.main()
