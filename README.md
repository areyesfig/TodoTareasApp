# Aplicación de Lista de Tareas (To-Do List)

Esta es una aplicación web simple para gestionar tareas, construida con Python, Flask y SQLite.

## Estructura del Proyecto

*   **app.py**: Archivo principal de la aplicación y configuración de la base de datos.
*   **templates/index.html**: Interfaz de usuario.
*   **requirements.txt**: Dependencias del proyecto.
*   **Procfile**: Archivo de configuración para despliegue (ej. Heroku).
*   **test_app.py**: Pruebas unitarias automatizadas.

## Instalación y Ejecución

1.  Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```

2.  Ejecutar la aplicación:
    ```bash
    python app.py
    ```

3.  Abrir en el navegador: `http://127.0.0.1:5000`

## Pruebas

Para ejecutar las pruebas automatizadas y verificar que todo funciona correctamente:

```bash
python test_app.py
```

## Despliegue

La aplicación está lista para ser desplegada en plataformas como Heroku o Render usando `gunicorn` como servidor de producción.
