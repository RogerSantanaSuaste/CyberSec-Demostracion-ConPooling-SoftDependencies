"""""
Previamente código de audit_log.py, ahora forma parte de "paquete" prueba para mostrar riesgos de dependencias de software. Este módulo se mantiene para mostrar cómo se podría implementar un sistema de auditoría simple, pero ahora es parte del paquete "paquete-prueba-audit" para ilustrar los riesgos de las dependencias.
from datetime import datetime
from typing import Optional
import logging

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
    
def get_logs():
    return audit_logs
"""""