
# 📄 FacturaYa — API de Facturación Electrónica (Python · FastAPI)

[![Build Status](https://github.com/alejoved/FacturaYa-Python-FastAPI/actions/workflows/ci.yml/badge.svg)](https://github.com/alejoved/FacturaYa-Python-FastAPI/actions)
[![License](https://img.shields.io/github/license/alejoved/FacturaYa-Python-FastAPI)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/alejoved/FacturaYa-Python-FastAPI)](https://github.com/alejoved/FacturaYa-Python-FastAPI/commits)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)](https://fastapi.tiangolo.com/)
[![Dockerized](https://img.shields.io/badge/docker-ready-blue)](#docker)

---

API backend para gestión de facturas electrónicas, clientes y productos. Diseñada con **FastAPI**, enfocada en rendimiento, escalabilidad y buenas prácticas backend modernas con tipado fuerte, validaciones, tests y documentación automática.

---

## 🚀 Funcionalidades

- 🧾 **Facturas**: crear, listar, cancelar, calcular totales  
- 👤 **Clientes**: CRUD completo (`nombre`, `documento`, `email`, etc.)  
- 📦 **Productos**: CRUD completo (`nombre`, `precio`, `stock`, etc.)  
- 📚 Documentación Swagger y ReDoc automática  
- 🧠 Validaciones de negocio con `pydantic`  
- 🔐 Seguridad (JWT, control de usuarios opcional)

---

## 🧩 Reglas de Negocio

- ✅ Cada factura contiene cliente, productos, y cantidades  
- ✅ Cálculo automático de subtotal, impuestos y total  
- ⛔ No se permite facturar productos sin stock disponible  
- 📆 Las facturas llevan sello de tiempo y estado (`emitida`, `cancelada`)  
- 🧾 Soporte para múltiples tasas de IVA por producto

---

## ⚙️ Tecnologías

| Área           | Herramienta           |
|----------------|------------------------|
| Backend        | Python 3.10+, FastAPI  |
| Base de Datos  | PostgreSQL, SQLAlchemy |
| Validaciones   | Pydantic               |
| Testing        | Pytest + HTTPX         |
| Docs API       | Swagger + ReDoc        |
| Contenedores   | Docker + Compose       |
| CI/CD          | GitHub Actions         |

---

## 📁 Estructura

```
app/
├── api/              # Rutas y controladores
├── core/             # Configuración y utilidades
├── models/           # Modelos ORM (SQLAlchemy)
├── schemas/          # Esquemas de entrada/salida (Pydantic)
├── services/         # Lógica de negocio
├── db/               # Conexión y repositorios
tests/                # Tests unitarios y de integración
```

---

## 🧪 Instalación local

```bash
# Clonar el repositorio
git clone https://github.com/alejoved/FacturaYa-Python-FastAPI.git
cd FacturaYa-Python-FastAPI

# Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Correr la aplicación
uvicorn app.main:app --reload

# Ver la documentación
http://localhost:8000/docs
```

---

## 🐳 Docker

```bash
# Construir imagen
docker build -t facturaya-app:latest .

# Levantar con Docker Compose
docker-compose up
```

---

## 🧪 Tests

```bash
# Ejecutar pruebas con cobertura
pytest --cov=app tests/
```
---

## ☸️ Despliegue en Kubernetes con Minikube

### ✅ Requisitos
- [x] Minikube instalado
- [x] Podman (o Docker)
- [x] Manifiestos en `k8s/`

### 🚀 Pasos de Despliegue
```bash
minikube delete
minikube start
minikube addons enable metrics-server

# Crear y exportar imagen
podman build -t facturaya-app:latest .
podman save -o facturaya-app.tar doctorya-app:latest

# Cargar imagen en Minikube
minikube image load facturaya-app.tar

# Aplicar manifiestos K8s
kubectl apply -f k8s/

# Ver logs o exponer servicio
kubectl logs <pod-name>
minikube service facturaya-app
```

---

## 📌 Qué demuestra este proyecto

| Área                      | Habilidad demostrada                     |
|---------------------------|------------------------------------------|
| Arquitectura moderna      | Separación de capas y responsabilidades  |
| Backend Python profesional| Uso de FastAPI + SQLAlchemy + Pydantic  |
| Reglas de negocio         | Validaciones personalizadas por entidad  |
| API RESTful               | Documentación automática + buenas rutas  |
| CI/CD y Docker            | Flujo Dev completo y reproducible        |

---

## 👤 Autor

Alejandro J. (`alejoved`)  
[GitHub](https://github.com/alejoved) • Backend Engineer

---

## 📄 Licencia

Distribuido bajo la licencia **Apache‑2.0**