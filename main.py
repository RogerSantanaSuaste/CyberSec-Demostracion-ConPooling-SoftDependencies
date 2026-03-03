from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
import paquetepruebaaudit as audit_log
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from db.database import SessionLocal
from middleware import AuditLogMiddleware

app = FastAPI()

app.add_middleware(AuditLogMiddleware)

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/docs")
def read_docs():
    return {"message": "This is the documentation endpoint."}

@app.get("/query-lenta")
async def query_lenta(db: AsyncSession = Depends(get_db)):
    # Simula una query lenta para probar el connection pooling
    await asyncio.sleep(20)  # Simula una operación lenta
    return {"status": "Listo!"}

@app.get("/audit-logs", response_class=HTMLResponse)
async def show_audit_logs():
    if not audit_log.get_logs():
        return "<h1>No hay logs aún.</h1>"

    rows = ""
    for log in sorted(audit_log.get_logs(), key=lambda x: x["timestamp"], reverse=True):  # más nuevos primero
        extra_str = str(log["extra"]) if log["extra"] else ""
        rows += f"""
        <tr>
            <td>{log['timestamp']}</td>
            <td>{log['accion']}</td>
            <td>{log['detalles']}</td>
            <td>{extra_str}</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Demo Audit Logs</title>
        <style>
            table {{ border-collapse: collapse; width: 100%; font-family: Arial; }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
            th {{ background-color: #4CAF50; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
            tr:hover {{ background-color: #ddd; }}
        </style>
    </head>
    <body>
        <h1>Audit Logs en Vivo</h1>
        <table>
            <tr>
                <th>Timestamp</th>
                <th>Acción</th>
                <th>Detalles</th>
                <th>Extras</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """
    return html