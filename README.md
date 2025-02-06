# **NetScannerPro - Herramienta Avanzada de Escaneo de Red y Puertos**

**NetScannerPro** es una herramienta poderosa y flexible para el escaneo de redes, diseñada para identificar dispositivos activos, puertos abiertos y posibles vulnerabilidades en una red. Desarrollada en Python, esta herramienta integra varias técnicas de escaneo para proporcionar información detallada sobre la configuración de la red y los riesgos de seguridad.

### **Características:**
- **Escaneo de Red**: Descubre todos los dispositivos activos dentro de un rango de red específico utilizando solicitudes ARP.
- **Escaneo de Puertos**: Escanea los 65,535 puertos en los dispositivos objetivo para detectar servicios abiertos.
- **Detección de Sistema Operativo**: Identifica el sistema operativo de los dispositivos utilizando el análisis del TTL (Time-to-Live).
- **Detección de Vulnerabilidades**: Analiza los puertos abiertos para detectar vulnerabilidades comunes como FTP, Telnet y SMB.

### **Tecnologías Utilizadas:**
- **Scapy** para descubrimiento de red y solicitudes ARP.
- **Socket** para escaneo de puertos y comprobaciones de vulnerabilidad.

### **Cómo Usar:**
1. Clona el repositorio:
   ```bash
   git clone https://github.com/SisaRoot/NetScannerPro.git
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el script principal:
   ```bash
   sudo python3 main.py
   ```
4. Ingresa el rango de red objetivo cuando se te solicite (por ejemplo, `192.168.1.0/24`).

### **Notas Importantes:**
- La herramienta escanea todos los puertos TCP de 65,535 puertos por defecto.
- El escáner de vulnerabilidades revisa configuraciones incorrectas comunes y vulnerabilidades asociadas con los puertos abiertos.

### **Descargo de Responsabilidad:**
Esta herramienta está destinada solo para su uso ético, para probar y asegurar redes para las cuales se tiene permiso explícito para escanear. El acceso no autorizado a redes es ilegal y no ético.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
