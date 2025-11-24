import unittest
from app import app, db, Task

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        # Configurar la aplicación para pruebas
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Base de datos en memoria
        self.app = app.test_client()
        
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index_page(self):
        # Probar que la página de inicio carga correctamente
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        # Probar agregar una tarea
        response = self.app.post('/add', data=dict(title='Tarea de prueba'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tarea de prueba', response.data)

    def test_complete_task(self):
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

if __name__ == '__main__':
    unittest.main()
