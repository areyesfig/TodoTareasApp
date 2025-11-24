# 🏗️ Documentación Técnica - Arquitectura del Sistema

## TodoTareasApp - Especificaciones Técnicas para Desarrolladores

---

## 📋 Índice

1. [Visión General del Sistema](#visión-general-del-sistema)
2. [Stack Tecnológico](#stack-tecnológico)
3. [Arquitectura de la Aplicación](#arquitectura-de-la-aplicación)
4. [Modelo de Datos](#modelo-de-datos)
5. [API Endpoints](#api-endpoints)
6. [Flujo de Datos](#flujo-de-datos)
7. [Seguridad](#seguridad)
8. [Rendimiento y Escalabilidad](#rendimiento-y-escalabilidad)
9. [Decisiones de Diseño](#decisiones-de-diseño)
10. [Guía de Desarrollo](#guía-de-desarrollo)

---

## 🔍 Visión General del Sistema

**TodoTareasApp** es una aplicación web CRUD (Create, Read, Update, Delete) desarrollada siguiendo el patrón arquitectónico MVC (Model-View-Controller). La aplicación permite la gestión de tareas mediante una interfaz web intuitiva.

### **Características Principales**
- ✅ Operaciones CRUD completas sobre tareas
- 🔄 Persistencia de datos en SQLite
- 🎨 Interfaz responsive sin dependencias de JavaScript
- 🧪 Suite de pruebas unitarias
- 🚀 Lista para despliegue en cloud

---

## 🛠️ Stack Tecnológico

### **Backend**
| Componente | Tecnología | Versión | Propósito |
|------------|-----------|---------|-----------|
| Framework Web | Flask | 3.x | Servidor web y routing |
| ORM | Flask-SQLAlchemy | 3.x | Mapeo objeto-relacional |
| Base de Datos | SQLite | 3.x | Almacenamiento de datos |
| Servidor WSGI | Gunicorn | 21.x | Servidor de producción |
| Testing | unittest | stdlib | Pruebas automatizadas |

### **Frontend**
| Componente | Tecnología | Propósito |
|------------|-----------|-----------|
| Motor de Plantillas | Jinja2 | Renderizado dinámico HTML |
| Estilos | CSS3 | Diseño y presentación |
| Markup | HTML5 | Estructura semántica |

### **Herramientas de Desarrollo**
- **Git**: Control de versiones
- **GitHub**: Repositorio remoto
- **pip**: Gestión de dependencias

---

## 🏛️ Arquitectura de la Aplicación

### **Patrón MVC**

```
┌─────────────────────────────────────────────────────┐
│                   USUARIO / NAVEGADOR               │
└─────────────────────┬───────────────────────────────┘
                      │ HTTP Request
                      ▼
┌─────────────────────────────────────────────────────┐
│                  FLASK APPLICATION                   │
│  ┌──────────────────────────────────────────────┐  │
│  │         CONTROLLER (app.py - Routes)         │  │
│  │  @app.route('/') - index()                   │  │
│  │  @app.route('/add') - add()                  │  │
│  │  @app.route('/update/<id>') - update()       │  │
│  │  @app.route('/delete/<id>') - delete()       │  │
│  └────────┬─────────────────────────┬────────────┘  │
│           │                         │                │
│           ▼                         ▼                │
│  ┌────────────────┐      ┌──────────────────────┐  │
│  │  MODEL         │      │  VIEW                │  │
│  │  (Task class)  │      │  (templates/         │  │
│  │  - id          │◄─────┤   index.html)        │  │
│  │  - title       │      │                      │  │
│  │  - complete    │      └──────────────────────┘  │
│  └────────┬───────┘                                 │
│           │                                          │
│           ▼                                          │
│  ┌────────────────────────────────────────────┐    │
│  │         DATABASE (SQLite)                  │    │
│  │         instance/todo.db                   │    │
│  │         Table: task                        │    │
│  └────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────┘
```

### **Flujo de Peticiones**

1. **Cliente** → Envía solicitud HTTP al servidor
2. **Flask Router** → Identifica la ruta y ejecuta el controlador correspondiente
3. **Controller** → Procesa la lógica de negocio
4. **Model** → Interactúa con la base de datos vía SQLAlchemy
5. **View** → Renderiza la respuesta HTML con Jinja2
6. **Servidor** → Devuelve la respuesta al cliente

---

## 💾 Modelo de Datos

### **Diagrama Entidad-Relación**

```
┌─────────────────────────┐
│        Task             │
├─────────────────────────┤
│ PK  id (INTEGER)        │
│     title (VARCHAR 100) │
│     complete (BOOLEAN)  │
└─────────────────────────┘
```

### **Definición del Modelo (ORM)**

```python
class Task(db.Model):
    """
    Modelo de base de datos para representar una tarea.
    """
    __tablename__ = 'task'
    
    # Clave primaria autoincremental
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # Título de la tarea (obligatorio, máximo 100 caracteres)
    title = db.Column(db.String(100), nullable=False)
    
    # Estado de completitud (por defecto False)
    complete = db.Column(db.Boolean, default=False, nullable=False)
```

### **Esquema SQL Equivalente**

```sql
CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    complete BOOLEAN NOT NULL DEFAULT 0
);
```

### **Restricciones y Validaciones**

| Campo | Tipo | Obligatorio | Valor por Defecto | Validación |
|-------|------|-------------|-------------------|------------|
| id | INTEGER | Sí (auto) | Autoincremental | - |
| title | VARCHAR(100) | Sí | - | Máximo 100 caracteres |
| complete | BOOLEAN | Sí | False | True/False |

---

## 🔌 API Endpoints

### **1. GET /**
**Propósito:** Renderizar la página principal con todas las tareas

**Request:**
```http
GET / HTTP/1.1
Host: localhost:5000
```

**Response:**
```http
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>...
```

**Lógica:**
```python
@app.route('/')
def index():
    tasks = Task.query.all()  # SELECT * FROM task;
    return render_template('index.html', tasks=tasks)
```

---

### **2. POST /add**
**Propósito:** Crear una nueva tarea

**Request:**
```http
POST /add HTTP/1.1
Host: localhost:5000
Content-Type: application/x-www-form-urlencoded

title=Comprar+leche
```

**Response:**
```http
HTTP/1.1 302 Found
Location: /
```

**Lógica:**
```python
@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        new_task = Task(title=title)
        db.session.add(new_task)      # INSERT INTO task
        db.session.commit()
    return redirect(url_for('index'))
```

**SQL Ejecutado:**
```sql
INSERT INTO task (title, complete) VALUES ('Comprar leche', 0);
```

---

### **3. GET /update/<int:task_id>**
**Propósito:** Alternar el estado de completitud de una tarea

**Request:**
```http
GET /update/1 HTTP/1.1
Host: localhost:5000
```

**Response:**
```http
HTTP/1.1 302 Found
Location: /
```

**Lógica:**
```python
@app.route('/update/<int:task_id>')
def update(task_id):
    task = Task.query.get_or_404(task_id)
    task.complete = not task.complete
    db.session.commit()              # UPDATE task
    return redirect(url_for('index'))
```

**SQL Ejecutado:**
```sql
UPDATE task SET complete = NOT complete WHERE id = 1;
```

---

### **4. GET /delete/<int:task_id>**
**Propósito:** Eliminar una tarea

**Request:**
```http
GET /delete/1 HTTP/1.1
Host: localhost:5000
```

**Response:**
```http
HTTP/1.1 302 Found
Location: /
```

**Lógica:**
```python
@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)          # DELETE FROM task
    db.session.commit()
    return redirect(url_for('index'))
```

**SQL Ejecutado:**
```sql
DELETE FROM task WHERE id = 1;
```

---

## 🔄 Flujo de Datos

### **Ejemplo: Agregar una Tarea**

```
┌────────┐     POST /add        ┌──────────┐
│ User   │─────────────────────►│ Flask    │
│ Browser│      title=...       │ App      │
└────────┘                      └────┬─────┘
                                     │
                                     │ 1. Recibir datos del formulario
                                     ▼
                              ┌──────────────┐
                              │ Controller   │
                              │ add()        │
                              └──────┬───────┘
                                     │
                                     │ 2. Crear instancia Task
                                     ▼
                              ┌──────────────┐
                              │ Model        │
                              │ Task(title=.)│
                              └──────┬───────┘
                                     │
                                     │ 3. db.session.add()
                                     ▼
                              ┌──────────────┐
                              │ SQLAlchemy   │
                              │ ORM          │
                              └──────┬───────┘
                                     │
                                     │ 4. INSERT SQL
                                     ▼
                              ┌──────────────┐
                              │ SQLite DB    │
                              │ todo.db      │
                              └──────┬───────┘
                                     │
                                     │ 5. Commit confirmado
                                     ▼
                              ┌──────────────┐
                              │ Redirect     │
                              │ to /         │
                              └──────┬───────┘
                                     │
                                     ▼
┌────────┐    HTTP 302 Redirect   ┌──────────┐
│ Browser│◄──────────────────────│ Response │
└────────┘                        └──────────┘
```

---

## 🔒 Seguridad

### **Medidas Implementadas**

1. **Validación de Entrada**
   - Flask valida automáticamente los tipos de datos en las rutas
   - Ejemplo: `<int:task_id>` rechaza valores no numéricos

2. **Protección contra SQL Injection**
   - SQLAlchemy utiliza consultas parametrizadas
   - Ninguna entrada del usuario se concatena directamente en SQL

3. **Manejo de Errores**
   - `get_or_404()` devuelve 404 si el ID no existe
   - Previene exposición de errores internos

### **Consideraciones Futuras**

⚠️ **Para producción, implementar:**
- CSRF protection (Flask-WTF)
- Rate limiting
- HTTPS/TLS
- Autenticación y autorización
- Sanitización adicional de entradas

---

## 📈 Rendimiento y Escalabilidad

### **Optimizaciones Actuales**

- **SQLite:** Base de datos en archivo, rápida para operaciones pequeñas
- **Índice automático:** La clave primaria `id` está indexada
- **Sin cache innecesaria:** `SQLALCHEMY_TRACK_MODIFICATIONS = False`

### **Limitaciones Conocidas**

| Aspecto | Limitación | Solución Recomendada |
|---------|------------|----------------------|
| Concurrencia | SQLite soporta 1 escritor | Migrar a PostgreSQL/MySQL |
| Tamaño de DB | Máximo ~140TB (teórico) | Suficiente para este caso de uso |
| Sesiones de Usuario | No hay multi-usuario | Implementar autenticación |

### **Escalabilidad Horizontal**

Para escalar la aplicación:
1. Reemplazar SQLite por PostgreSQL
2. Usar Redis para sesiones
3. Implementar load balancer (Nginx)
4. Dockerizar la aplicación

---

## 💡 Decisiones de Diseño

### **¿Por qué Flask?**
✅ Ligero y fácil de aprender  
✅ Ideal para MVPs y aplicaciones pequeñas  
✅ Gran ecosistema de extensiones  

### **¿Por qué SQLite?**
✅ Sin configuración de servidor  
✅ Portátil (archivo único)  
✅ Suficiente para aplicaciones pequeñas  

### **¿Por qué no usar JavaScript en el frontend?**
✅ Mantener la aplicación simple  
✅ Funciona sin dependencias adicionales  
✅ Mejor para aprendizaje  

### **¿Por qué Gunicorn en producción?**
✅ Servidor WSGI robusto y probado  
✅ Maneja múltiples workers  
✅ Compatible con Flask  

---

## 🧑‍💻 Guía de Desarrollo

### **Configurar Entorno de Desarrollo**

```bash
# Clonar repositorio
git clone https://github.com/areyesfig/TodoTareasApp.git
cd TodoTareasApp

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar en modo desarrollo
python app.py
```

### **Ejecutar Pruebas**

```bash
# Ejecutar todas las pruebas
python test_app.py

# Con mayor verbosidad
python -m unittest test_app.py -v

# Ejecutar una prueba específica
python -m unittest test_app.TodoTestCase.test_add_task
```

### **Debugging**

```python
# En app.py, agregar puntos de interrupción
import pdb; pdb.set_trace()

# Revisar logs
print(f"Task: {task.id}, {task.title}, {task.complete}")
```

### **Estructura de Commits**

```
feat: Agregar funcionalidad de categorías
fix: Corregir error al eliminar tarea
docs: Actualizar README con instrucciones de despliegue
test: Agregar pruebas para endpoint /update
refactor: Separar lógica de validación en función auxiliar
```

---

## 📚 Referencias

- [Documentación de Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Python unittest](https://docs.python.org/3/library/unittest.html)

---

**Última actualización:** Noviembre 2025  
**Versión de la aplicación:** 1.0.0  
**Mantenedor:** [Tu nombre/equipo]
