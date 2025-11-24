# Aplicación de Lista de Tareas (To-Do List)

Esta es una aplicación web simple para gestionar tareas, construida con Python, Flask y SQLite.

## 📋 Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Arquitectura del Proyecto](#arquitectura-del-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos Previos](#requisitos-previos)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Uso de la Aplicación](#uso-de-la-aplicación)
- [Pruebas](#pruebas)
- [Base de Datos](#base-de-datos)
- [Despliegue](#despliegue)
- [Solución de Problemas](#solución-de-problemas)
- [Contribuir al Proyecto](#contribuir-al-proyecto)

---

## 📖 Descripción General

**TodoTareasApp** es una aplicación web desarrollada con el framework Flask de Python que permite a los usuarios gestionar una lista de tareas pendientes. Los usuarios pueden:

- ✅ Agregar nuevas tareas
- ✏️ Marcar tareas como completadas o deshacer completadas
- 🗑️ Eliminar tareas
- 👀 Ver todas las tareas en una interfaz limpia e intuitiva

La aplicación utiliza SQLite como base de datos relacional, lo que la hace ligera y fácil de desplegar sin necesidad de configurar un servidor de base de datos externo.

---

## 🏗️ Arquitectura del Proyecto

La aplicación sigue el patrón **MVC (Model-View-Controller)**:

### **Model (Modelo)** 
- **Archivo:** `app.py` - Clase `Task`
- **Responsabilidad:** Define la estructura de datos de una tarea (id, título, estado)
- **ORM:** SQLAlchemy para interactuar con la base de datos

### **View (Vista)**
- **Archivo:** `templates/index.html`
- **Responsabilidad:** Interfaz de usuario que muestra las tareas y formularios
- **Tecnología:** HTML5 + CSS3 + Jinja2 (motor de plantillas)

### **Controller (Controlador)**
- **Archivo:** `app.py` - Rutas de Flask
- **Responsabilidad:** Maneja las solicitudes HTTP y coordina Model y View
- **Endpoints:**
  - `GET /` - Muestra todas las tareas
  - `POST /add` - Agrega una nueva tarea
  - `GET /update/<id>` - Alterna el estado de una tarea
  - `GET /delete/<id>` - Elimina una tarea

---

## 📂 Estructura del Proyecto

```
AppBdRelacionales/
│
├── app.py                  # Aplicación principal (lógica de backend)
├── requirements.txt        # Dependencias del proyecto
├── Procfile               # Configuración para despliegue (Heroku/Render)
├── test_app.py            # Pruebas unitarias automatizadas
├── README.md              # Documentación del proyecto
├── .gitignore             # Archivos a ignorar en Git
│
├── templates/             # Plantillas HTML
│   └── index.html         # Interfaz de usuario principal
│
└── instance/              # Carpeta generada automáticamente
    └── todo.db            # Base de datos SQLite (se crea al ejecutar)
```

---

## 🔧 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8 o superior** ([Descargar Python](https://www.python.org/downloads/))
- **pip** (gestor de paquetes de Python, generalmente incluido con Python)
- **Git** (opcional, para clonar el repositorio)

---

## 🚀 Instalación y Ejecución

### **Paso 1: Clonar o descargar el repositorio**

```bash
git clone https://github.com/areyesfig/TodoTareasApp.git
cd TodoTareasApp
```

### **Paso 2: Instalar dependencias**

```bash
pip install -r requirements.txt
```

O si estás en macOS/Linux:

```bash
pip3 install -r requirements.txt
```

### **Paso 3: Ejecutar la aplicación**

```bash
python app.py
```

O en macOS/Linux:

```bash
python3 app.py
```

### **Paso 4: Abrir en el navegador**

Visita: **http://127.0.0.1:5000**

¡Listo! La aplicación debería estar funcionando.

---

## 📱 Uso de la Aplicación

### **Agregar una tarea**
1. Escribe el título de la tarea en el campo de texto.
2. Haz clic en el botón **"Agregar"**.
3. La tarea aparecerá en la lista de tareas pendientes.

### **Completar una tarea**
1. Haz clic en **"Completar"** junto a la tarea que deseas marcar.
2. La tarea aparecerá tachada y en color gris.
3. Puedes hacer clic en **"Deshacer"** para marcarla nuevamente como pendiente.

### **Eliminar una tarea**
1. Haz clic en **"Eliminar"** junto a la tarea que deseas borrar.
2. La tarea se eliminará permanentemente de la base de datos.

---

## 🧪 Pruebas

La aplicación incluye pruebas unitarias automatizadas para verificar su correcto funcionamiento.

### **Ejecutar las pruebas**

```bash
python test_app.py
```

### **Pruebas incluidas**
- ✅ Carga de la página principal
- ✅ Agregar una nueva tarea
- ✅ Marcar una tarea como completada
- ✅ Eliminar una tarea

### **Resultado esperado**

```
....
----------------------------------------------------------------------
Ran 4 tests in 0.XXXs

OK
```

---

## 🗄️ Base de Datos

### **Sistema de Gestión**
- **SQLite** - Base de datos relacional ligera sin servidor

### **Ubicación**
- `instance/todo.db` (se crea automáticamente al ejecutar la aplicación)

### **Estructura de la tabla `task`**

| Campo    | Tipo    | Descripción                                    |
|----------|---------|------------------------------------------------|
| id       | INTEGER | Identificador único (clave primaria)           |
| title    | VARCHAR | Título de la tarea (máximo 100 caracteres)     |
| complete | BOOLEAN | Estado: `0` = pendiente, `1` = completada      |

### **Consultar la base de datos manualmente**

Para inspeccionar la base de datos desde la terminal:

```bash
sqlite3 instance/todo.db
```

Comandos útiles dentro de SQLite:

```sql
.tables                    -- Ver las tablas
.schema task              -- Ver la estructura de la tabla
SELECT * FROM task;       -- Ver todas las tareas
.quit                     -- Salir
```

---

## 🌐 Despliegue

La aplicación está lista para ser desplegada en servicios como **Render**, **Railway** o **Heroku**.

### **Despliegue en Render (Recomendado)**

1. **Sube el proyecto a GitHub** (ya completado)
2. Ve a [render.com](https://render.com) y crea una cuenta
3. Crea un nuevo **Web Service**
4. Conecta tu repositorio de GitHub
5. Configura:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. Haz clic en **"Create Web Service"**
7. En unos minutos, tendrás una URL pública como: `https://tu-app.onrender.com`

### **Importante para producción**
- La aplicación usa `debug=True` por defecto (solo para desarrollo)
- En producción, `gunicorn` se encarga de ejecutar la aplicación de forma segura
- SQLite funciona bien para aplicaciones pequeñas, pero considera PostgreSQL para aplicaciones con muchos usuarios

---

## 🛠️ Solución de Problemas

### **Error: "No module named 'flask'"**
**Solución:** Instala las dependencias con `pip install -r requirements.txt`

### **Error: "Address already in use"**
**Solución:** El puerto 5000 ya está en uso. Cambia el puerto en `app.py`:
```python
app.run(debug=True, port=5001)
```

### **La base de datos no se crea**
**Solución:** Asegúrate de que la carpeta `instance/` tenga permisos de escritura

### **Las pruebas fallan**
**Solución:** Ejecuta `pip install -r requirements.txt` para asegurar que todas las dependencias estén instaladas

---

## 🤝 Contribuir al Proyecto

¿Quieres mejorar la aplicación? ¡Las contribuciones son bienvenidas!

1. Haz un fork del repositorio
2. Crea una rama para tu funcionalidad (`git checkout -b nueva-funcionalidad`)
3. Realiza tus cambios y documenta el código
4. Ejecuta las pruebas (`python test_app.py`)
5. Haz commit de tus cambios (`git commit -m "Agregar nueva funcionalidad"`)
6. Sube tu rama (`git push origin nueva-funcionalidad`)
7. Abre un Pull Request

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## 👨‍💻 Autor

Desarrollado como proyecto académico para el curso de Bases de Datos Relacionales.

**Repositorio:** [https://github.com/areyesfig/TodoTareasApp](https://github.com/areyesfig/TodoTareasApp)

---

¡Gracias por usar TodoTareasApp! 🎉
