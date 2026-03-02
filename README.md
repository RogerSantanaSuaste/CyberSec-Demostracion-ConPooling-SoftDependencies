# FastAPI audit.
Este es un proyecto de ejemplo, vulnerable por diseño en el que se busca demostrar dos conceptos:
- Dependecias de Software inseguras. (El rol de pip y socksio).
- Agrupación de Conexiones (Connection Pooling).

# Requisitos (requirements.txt)
- fastapi
- uvicorn
- pip-audit

# Como iniciar el proyecto (usando docker)
1. Clonar el repositorio.
2. Navegar a la carpeta del proyecto.
3. Ejecutar el siguiente comando para construir la imagen de docker:
   ```bash
   docker build -t fastapi-audit:latest .
   ```
4. Ejecutar el siguiente comando para iniciar el contenedor:
   ```bash
    docker run -d -p 8000:8000 --name fastapi-audit fastapi-audit:latest
    ```
5. Acceder a la aplicación en el navegador web o usando curl:
   ```bash
    curl http://localhost:8000
    ```

