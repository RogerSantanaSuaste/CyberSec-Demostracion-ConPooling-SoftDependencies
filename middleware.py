from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime
import paquetepruebaaudit as audit_log  # Importamos el paquete de auditoría que muestra riesgos de dependencias

class AuditLogMiddleware(BaseHTTPMiddleware):
    """
Middleware para registrar acciones de los usuarios en un sistema de auditoría.
    """
    async def dispatch(self, request: Request, call_next):
        start_time = datetime.utcnow()
        client_host = request.client.host
        
        # Log de inicio de la petición
        audit_log.log_audit(
            action="Inicio de petición",
            user_id=None,  # Aquí podrías extraer el ID del usuario si tienes autenticación
            details=f"Endpoint: {request.url.path}, Método: {request.method}, Cliente: {client_host}"
        )
        try:
            response = await call_next(request)
        except Exception as e:
            audit_log.log_audit(
                action="Error en petición",
                user_id=None,
                details=f"Endpoint: {request.url.path}, Método: {request.method}, Cliente: {client_host}, Error: {str(e)}"
            )
            raise # Re-lanza la excepción para que FastAPI maneje el error
        duration = (datetime.utcnow() - start_time).total_seconds()
        
        # Log de finalización de la petición
        audit_log.log_audit(
            action="Fin de petición",
            user_id=None,
            details=f"Endpoint: {request.url.path}, Método: {request.method}, Cliente: {client_host}, Duración: {duration:.2f} segundos"
        )
        return response