"""
Aplicación de Lista de Tareas (To-Do List)

Esta aplicación web permite a los usuarios gestionar sus tareas diarias.
Desarrollada con Flask (framework web de Python) y SQLite (base de datos).

Arquitectura:
- Patrón MVC (Model-View-Controller)
- Model: Clase Task (modelo de datos)
- View: templates/index.html (interfaz de usuario)
- Controller: Rutas/endpoints de Flask (lógica de negocio)

Autor: [Tu nombre]
Fecha: Noviembre 2025
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos SQLite
# La base de datos se creará en la carpeta 'instance' como 'todo.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

# Desactivar el seguimiento de modificaciones para mejorar el rendimiento
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy con la aplicación Flask
db = SQLAlchemy(app)

# Modelo de datos para las tareas
class Task(db.Model):
    """
    Modelo de base de datos para representar una tarea.
    
    Atributos:
        id (int): Identificador único de la tarea (clave primaria, autoincremental)
        title (str): Título o descripción de la tarea (máximo 100 caracteres)
        complete (bool): Estado de la tarea (True=completada, False=pendiente)
    
    Ejemplo:
        nueva_tarea = Task(title="Comprar leche")
        # Por defecto, complete será False
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean, default=False)

# Crear todas las tablas en la base de datos al iniciar la aplicación
# Este bloque se ejecuta automáticamente cuando se importa o ejecuta el módulo
with app.app_context():
    db.create_all()  # Crea la tabla 'task' si no existe

# ============== RUTAS / ENDPOINTS ==============

@app.route('/')
def index():
    """
    Ruta principal de la aplicación.
    
    Método HTTP: GET
    
    Funcionalidad:
        - Obtiene todas las tareas de la base de datos
        - Renderiza la plantilla HTML con la lista de tareas
    
    Returns:
        HTML: Página principal con todas las tareas
    """
    # Consultar todas las tareas en la base de datos
    tasks = Task.query.all()
    
    # Renderizar la plantilla y pasar las tareas como variable
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    """
    Endpoint para agregar una nueva tarea.
    
    Método HTTP: POST
    
    Parámetros (formulario):
        title (str): Título de la nueva tarea
    
    Funcionalidad:
        - Recibe el título de la tarea desde el formulario HTML
        - Valida que el título no esté vacío
        - Crea una nueva tarea en la base de datos
        - Redirige a la página principal
    
    Returns:
        Redirect: Redirige a la ruta principal '/'
    """
    # Obtener el título del formulario enviado por el usuario
    title = request.form.get('title')
    
    # Validar que el título no esté vacío
    if title:
        # Crear una nueva instancia de Task
        new_task = Task(title=title)
        
        # Agregar la tarea a la sesión de la base de datos
        db.session.add(new_task)
        
        # Guardar los cambios en la base de datos
        db.session.commit()
    
    # Redirigir a la página principal para ver la lista actualizada
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>')
def update(task_id):
    """
    Endpoint para alternar el estado de una tarea (completar/deshacer).
    
    Método HTTP: GET
    
    Parámetros (URL):
        task_id (int): ID de la tarea a actualizar
    
    Funcionalidad:
        - Busca la tarea por su ID
        - Invierte su estado (pendiente ↔ completada)
        - Guarda los cambios en la base de datos
        - Redirige a la página principal
    
    Returns:
        Redirect: Redirige a la ruta principal '/'
    
    Raises:
        404: Si no se encuentra la tarea con el ID especificado
    """
    # Buscar la tarea por ID, retorna 404 si no existe
    task = Task.query.get_or_404(task_id)
    
    # Alternar el estado: si estaba completada, marcarla como pendiente y viceversa
    task.complete = not task.complete
    
    # Guardar los cambios en la base de datos
    db.session.commit()
    
    # Redirigir a la página principal
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    """
    Endpoint para eliminar una tarea.
    
    Método HTTP: GET
    
    Parámetros (URL):
        task_id (int): ID de la tarea a eliminar
    
    Funcionalidad:
        - Busca la tarea por su ID
        - Elimina la tarea de la base de datos
        - Redirige a la página principal
    
    Returns:
        Redirect: Redirige a la ruta principal '/'
    
    Raises:
        404: Si no se encuentra la tarea con el ID especificado
    """
    # Buscar la tarea por ID, retorna 404 si no existe
    task = Task.query.get_or_404(task_id)
    
    # Eliminar la tarea de la sesión de la base de datos
    db.session.delete(task)
    
    # Confirmar la eliminación en la base de datos
    db.session.commit()
    
    # Redirigir a la página principal
    return redirect(url_for('index'))

# Punto de entrada de la aplicación
if __name__ == '__main__':
    """
    Ejecuta la aplicación Flask en modo desarrollo.
    
    Configuración:
        debug=True: Activa el modo de depuración
            - Recarga automática al detectar cambios en el código
            - Muestra errores detallados en el navegador
            - NO USAR en producción (usar gunicorn en su lugar)
    
    Para ejecutar:
        python app.py
    
    La aplicación estará disponible en: http://127.0.0.1:5000
    """
    app.run(debug=True)
