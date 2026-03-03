# paquete-prueba-audit/__init__.py
import os
import datetime
import socket
from fastapi import Request
from datetime import datetime
from typing import Optional
import logging

# Este es un paquete "pip" para mostrar los riesgos de las dependencias de software.

# Ahora función de utilidad para "loggear" la información de la petición

audit_logs: list[dict] = []
logger = logging.getLogger("audit_log")
logger.setLevel(logging.INFO)

def log_audit(action: str, user_id: Optional[int] = None, details: str = "", extra: dict = None):
    
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "accion": action,
        "usuario_id": user_id,
        "detalles": details,
        "extra": extra or {},
    }
    audit_logs.append(log_entry)
    logger.info(f"[{log_entry['timestamp']}] Accion: {log_entry['accion']}, Usuario ID: {log_entry['usuario_id']}, Detalles: {log_entry['detalles']}, Extra: {log_entry['extra']}")

def captura():
    # Captura información del entorno para mostrar el riesgo de esta dependencia
    info = {
        "timestamp": datetime.utcnow().isoformat(),
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "env_vars": {key: os.getenv(key) for key in ["PATH", "HOME", "USER"]},  # Solo algunas variables de entorno comunes
        "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD", "No definido"),  # Ejemplo de variable de entorno sensible, que fueron declaradas en el docker-compose.yml, para mostrar el riesgo de esta dependencia
        "platform": os.name,
        "cwd": os.getcwd(),
    }
    print(f"Captura de entorno: {info}")  # También imprimimos en consola para mostrar el riesgo
    
def get_logs():
    captura()  # Captura información del entorno cada vez que se solicitan los logs, para mostrar el riesgo de esta dependencia
    return audit_logs