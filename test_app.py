"""
Pruebas Unitarias para la Aplicación de Lista de Tareas

Este archivo contiene todas las pruebas automatizadas para verificar
el correcto funcionamiento de la aplicación.

Framework de pruebas: unittest (biblioteca estándar de Python)

Para ejecutar las pruebas:
    python test_app.py
    
Para ejecutar con más detalle:
    python -m unittest test_app.py -v
"""

import unittest
from app import app, db, Task

class TodoTestCase(unittest.TestCase):
    """
    Suite de pruebas para la aplicación de Lista de Tareas.
    
    Cada método de prueba verifica una funcionalidad específica:
    - Carga de la página principal
    - Agregar tareas
    - Marcar tareas como completadas
    - Eliminar tareas
    """
    
    def setUp(self):
        """
        Método ejecutado ANTES de cada prueba.
        
        Configuración:
        - Activa el modo de pruebas de Flask
        - Usa una base de datos en memoria (más rápida, se borra al terminar)
        - Crea un cliente de prueba para simular solicitudes HTTP
        - Crea todas las tablas necesarias
        """
        # Configurar la aplicación para pruebas
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Base de datos en memoria
        self.app = app.test_client()
        
        with app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Método ejecutado DESPUÉS de cada prueba.
        
        Limpieza:
        - Elimina la sesión de la base de datos
        - Borra todas las tablas
        - Garantiza que cada prueba comience con un estado limpio
        """
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index_page(self):
        """
        Prueba 1: Verificar que la página principal carga correctamente.
        
        Verifica:
        - El endpoint '/' responde con código HTTP 200 (OK)
        - La página se renderiza sin errores
        """
        # Probar que la página de inicio carga correctamente
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        """
        Prueba 2: Verificar que se puede agregar una nueva tarea.
        
        Verifica:
        - El endpoint '/add' acepta solicitudes POST
        - La tarea se guarda correctamente en la base de datos
        - La tarea aparece en la página después de agregarla
        """
        # Probar agregar una tarea
        response = self.app.post('/add', data=dict(title='Tarea de prueba'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tarea de prueba', response.data)

    def test_complete_task(self):
        """
        Prueba 3: Verificar que se puede marcar una tarea como completada.
        
        Proceso:
        1. Crea una tarea en la base de datos
        2. Llama al endpoint '/update/<id>' para cambiar su estado
        3. Verifica que el campo 'complete' sea True
        
        Verifica:
        - El estado de la tarea se actualiza correctamente
        - El endpoint '/update' funciona como se espera
        """
        # Agregar una tarea primero
        with app.app_context():
            task = Task(title='Tarea a completar')
            db.session.add(task)
            db.session.commit()
            task_id = task.id

        # Marcar como completada
        response = self.app.get(f'/update/{task_id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        # Verificar en la base de datos
        with app.app_context():
            task = Task.query.get(task_id)
            self.assertTrue(task.complete)

    def test_delete_task(self):
        """
        Prueba 4: Verificar que se puede eliminar una tarea.
        
        Proceso:
        1. Crea una tarea en la base de datos
        2. Llama al endpoint '/delete/<id>'
        3. Verifica que la tarea ya no aparece en la página
        
        Verifica:
        - La tarea se elimina correctamente de la base de datos
        - El endpoint '/delete' funciona como se espera
        """
        # Agregar una tarea primero
        with app.app_context():
            task = Task(title='Tarea a eliminar')
            db.session.add(task)
            db.session.commit()
            task_id = task.id

        # Eliminar la tarea
        response = self.app.get(f'/delete/{task_id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Tarea a eliminar', response.data)

# Punto de entrada para ejecutar las pruebas directamente
if __name__ == '__main__':
    """
    Ejecuta todas las pruebas cuando se ejecuta este archivo directamente.
    
    Uso:
        python test_app.py
    
    Resultado esperado:
        Ran 4 tests in X.XXXs
        OK
    """
    unittest.main()
