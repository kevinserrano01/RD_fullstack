# EJERCICIO PRÁCTICO RD

Este proyecto es una aplicación full-stack que utiliza **Svelte** para el frontend y **FastAPI** para el backend y **Docker** como herramienta. El propósito de esta aplicación es proporcionar una solución eficiente y moderna para la visualización de datos a travéz de un sitio web.

## 🟢 REQUISITOS PREVIOS

Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu sistema:

- **Python 3.9+**
- **Node.js 16+** y **npm**
- **Docker** y **Docker Compose** (opcional, para ejecución con contenedores)

## 🟢 INSTALACIÓN

Sigue estos pasos para instalar y configurar el proyecto:

### 1. Clona este repositorio o descarga los archivos.

```bash
git clone https://github.com/kevinserrano01/RD_fullstack.git
cd RD_fullstack
```

### 2. Instalar dependencias

- Frontend.

  ```bash
   cd frontend
   npm install
  ```

- Backend

  ```bash
  cd ../backend
  pip install -r requirements.txt
  ```

## 🟢 EJECUCIÓN

### Modo local

1. iniciar el backend: Desde el directorio backend, ejecuta:

   ```bash
   uvicorn backend.main:app --reload
   ```

2. Iniciar el frontend: Desde el directorio frontend, ejecuta:

   ```bash
   npm run dev
   ```

3. Accede a la aplicación en tu navegador:

- Frontend: http://localhost:5173
- Backend (API): http://localhost:8000

### Modo con Docker

Si prefieres ejecutar la aplicación con Docker, utiliza el siguiente comando desde la raíz del proyecto:

```bash
docker-compose up --build
```

Esto levantará tanto el backend como el frontend en contenedores.

Accede a la aplicación en tu navegador:

- Frontend: http://localhost:3000
- Backend (API): http://localhost:8000

## 🟢 DEPENDENCIAS

**BACKEND**

- **FastAPI**: Framework para construir APIs rápidas y modernas.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI.
- **Otros**: Listados en `requirements.txt`.

**FRONTEND**

- **Svelte**: Framework para construir interfaces de usuario reactivas.
- **eCharts**: Biblioteca para visualizaciones interactivas con gráficos.
- **Otros**: Listados en `package.json`.

## 🟢 INFORMACIÓN ADICIONAL

- Estructura del proyecto:
  - **`frontend/`**: Contiene el código del cliente (Svelte).
  - **`Backend/`**: Contiene el código del servidor (FastAPI).
  - **`docker-compose.yml`**: Configuración para ejecutar el proyecto con Docker.
