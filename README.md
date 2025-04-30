
# **Reto Final Python - Aplicación Flask con PostgreSQL**

Este proyecto es una aplicación **Flask** que interactúa con una base de datos **PostgreSQL**. La aplicación permite agregar, eliminar y listar datos en la base de datos. 

## **Índice**

- [Set Up del Entorno](#set-up-del-entorno)
  - [Clonar el Repositorio](#clonar-el-repositorio)
  - [Instalar Dependencias](#instalar-dependencias)
  - [Configurar Variables de Entorno](#configurar-variables-de-entorno)
  - [Ejecutar la Aplicación](#ejecutar-la-aplicación)
- [Flujo de Funcionamiento de la Aplicación](#flujo-de-funcionamiento-de-la-aplicación)
  - [Puntos de Entrada](#puntos-de-entrada)
  - [Rutas Disponibles](#rutas-disponibles)

---

## **Set Up del Entorno**

Sigue estos pasos para configurar y ejecutar el entorno de desarrollo de esta aplicación.

### **Clonar el Repositorio**

Primero, clona este repositorio en tu máquina local utilizando Git:

```bash
git clone https://github.com/jgueroIT/reto_final_python.git
cd reto_final_python
```

### **Instalar Dependencias**

Este proyecto usa **Python 3.11** y las dependencias especificadas en `requirements.txt`. Asegúrate de tener **Python 3.11** o superior instalado.

1. **Crea un entorno virtual** (recomendado):

   ```bash
   python3 -m venv venv
   ```

2. **Activa el entorno virtual**:

   - En **Linux/Mac**:

     ```bash
     source venv/bin/activate
     ```

   - En **Windows**:

     ```bash
     venv\Scriptsctivate
     ```

3. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

### **Configurar Variables de Entorno**

El proyecto necesita ciertas variables de entorno para conectarse a la base de datos y para configurar la aplicación.

1. **Crea un archivo `.env`** en la raíz del proyecto. Aquí hay un ejemplo de cómo debería lucir:

   ```env
   FLASK_ENV=development
   SECRET_KEY=mysecretkey
   DATABASE_URI=postgresql://reto_user:1234@db:5432/reto_db_utf8
   ```

   - `FLASK_ENV`: Define el entorno de la aplicación (puede ser `development` o `production`).
   - `SECRET_KEY`: Clave secreta utilizada por Flask para sesiones y protección CSRF.
   - `DATABASE_URI`: URI de conexión a la base de datos PostgreSQL.

### **Ejecutar la Aplicación**

Para ejecutar la aplicación en desarrollo:

1. **Usa Docker** (opcional pero recomendado):

   Si prefieres ejecutar todo en contenedores Docker (incluyendo la base de datos PostgreSQL), asegúrate de tener Docker y Docker Compose instalados en tu máquina.

   - **Construir la imagen Docker**:

     ```bash
     docker-compose up --build
     ```

   Esto levantará tanto la aplicación Flask como la base de datos PostgreSQL.

2. **O ejecuta sin Docker**:

   Si prefieres no usar Docker, puedes ejecutar la aplicación directamente en tu máquina local con:

   ```bash
   python run.py
   ```

   Esto iniciará el servidor Flask en el puerto `5000`.

---

## **Flujo de Funcionamiento de la Aplicación**

La aplicación proporciona una API RESTful para interactuar con la base de datos PostgreSQL. A continuación se describen los puntos de entrada y las rutas disponibles.

### **Puntos de Entrada**

- **`run.py`**: Este archivo es el punto de entrada principal para ejecutar la aplicación Flask en un entorno de desarrollo. Al ejecutar `python run.py`, se inicializa la aplicación y comienza a escuchar en el puerto `5000`.
  
- **`docker-compose.yml`**: Si prefieres ejecutar la aplicación en contenedores Docker, este archivo define los servicios necesarios: la aplicación Flask y PostgreSQL.

### **Rutas Disponibles**

La aplicación proporciona tres rutas principales para interactuar con los datos almacenados en la base de datos PostgreSQL.

#### **1. POST /data**
Inserta un nuevo dato en la base de datos.

- **Descripción**: Recibe datos en formato JSON y agrega un nuevo registro a la tabla `Data`. Si el dato ya existe (por ejemplo, el nombre ya está en la base de datos), devuelve un error `409 Conflict`.
  
- **Ejemplo de Request**:

  ```json
  {
    "name": "Nuevo Dato"
  }
  ```

- **Respuesta de éxito**:

  ```json
  {
    "message": "Data inserted successfully"
  }
  ```

- **Respuesta de conflicto (si el dato ya existe)**:

  ```json
  {
    "message": "Data already exists"
  }
  ```

#### **2. GET /data**
Obtiene todos los datos almacenados en la base de datos.

- **Descripción**: Devuelve una lista de todos los registros en la tabla `Data`, cada uno con su `id` y `name`.

- **Ejemplo de Request**: Ninguno.

- **Ejemplo de Respuesta**:

  ```json
  [
    {
      "id": 1,
      "name": "Nuevo Dato"
    },
    {
      "id": 2,
      "name": "Otro Dato"
    }
  ]
  ```

#### **3. DELETE /data/<int:id>**
Elimina un dato específico de la base de datos usando su `id`.

- **Descripción**: Elimina el registro correspondiente al `id` proporcionado en la URL.

- **Ejemplo de Request**:

  ```bash
  DELETE /data/1
  ```

- **Respuesta de éxito**:

  ```json
  {
    "message": "Data deleted successfully"
  }
  ```

- **Respuesta si el dato no existe**:

  ```json
  {
    "message": "Data not found"
  }
  ```

### **Inicialización de la Base de Datos**

Al iniciar la aplicación, las tablas de la base de datos se crean automáticamente si aún no existen, gracias a la instrucción `db.create_all()` en el archivo `manage.py`.

Si necesitas poblar la base de datos con algunos datos de ejemplo, puedes ejecutar el archivo `manage.py` para crear las tablas y agregar registros:

```bash
python manage.py
```

Esto creará las tablas y añadirá un usuario de prueba con el nombre `"SQL Test User"`.

---

## **Estructura del Proyecto**

```
.
├── app/
│   ├── __init__.py         # Configuración y creación de la aplicación
│   ├── config.py           # Configuración general de la aplicación
│   ├── models.py           # Modelos de base de datos (definición de `Data`)
│   ├── routes.py           # Rutas y lógica de la API
├── main.py                 # Punto de entrada para la app (si no usas Docker)
├── Dockerfile              # Dockerfile para la imagen de la aplicación
├── requirements.txt        # Dependencias de la aplicación
├── .env                    # Variables de entorno
├── docker-compose.yml      # Definición de servicios de Docker (Flask + PostgreSQL)
├── manage.py               # Script para inicializar la base de datos
├── manage.sh               # Script para ejecutar el manage.py con variables de entorno
└── run.py                  # Punto de entrada para ejecutar la app
```

---

## **Contribuir**

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. **Haz un Fork** del repositorio.
2. Crea una nueva rama para tu funcionalidad o arreglo.
3. Realiza tus cambios y asegúrate de que el código esté bien probado.
4. Haz un pull request con una descripción clara de lo que has hecho.

---

¡Gracias por usar este repositorio! Si tienes alguna pregunta o problema, no dudes en abrir un **issue** o enviarme un **pull request**.
