# 📘 Manual de Usuario - TodoTareasApp

## Guía Completa para Usuarios Finales

---

## 🎯 ¿Qué es TodoTareasApp?

**TodoTareasApp** es una aplicación web sencilla que te ayuda a organizar tus tareas diarias. No necesitas instalar ningún programa en tu computadora, solo necesitas un navegador web (Chrome, Firefox, Safari, etc.).

---

## 🚀 Cómo Acceder a la Aplicación

### **Opción 1: Versión en Internet (Producción)**
Si tu aplicación ya está desplegada en internet:
1. Abre tu navegador web favorito
2. Visita la dirección proporcionada (ej: `https://tu-app.onrender.com`)
3. ¡Listo! Ya puedes empezar a usar la aplicación

### **Opción 2: Versión Local (En tu computadora)**
Si estás ejecutando la aplicación en tu propia computadora:
1. Asegúrate de que la aplicación esté corriendo (deberías ver un mensaje en la terminal)
2. Abre tu navegador web
3. Visita: `http://127.0.0.1:5000`

---

## 📖 Instrucciones de Uso

### **1. Agregar una Nueva Tarea**

![Paso 1: Agregar tarea]

1. **Localiza el cuadro de texto** en la parte superior de la página que dice: *"¿Qué tienes que hacer hoy?"*

2. **Escribe el nombre de tu tarea**
   - Ejemplos: 
     - "Comprar leche"
     - "Llamar al doctor"
     - "Estudiar para el examen de matemáticas"

3. **Haz clic en el botón azul "Agregar"** o presiona la tecla Enter

4. **Verás tu tarea aparecer** en la lista debajo del formulario

> **💡 Consejo:** Intenta ser específico con el nombre de tus tareas para recordar exactamente qué tienes que hacer.

---

### **2. Marcar una Tarea como Completada**

![Paso 2: Completar tarea]

1. **Encuentra la tarea** que ya terminaste en la lista

2. **Haz clic en el enlace verde "Completar"** que aparece al lado derecho de la tarea

3. **Verás que la tarea ahora:**
   - Tiene una línea que la tacha
   - Aparece en color gris
   - El enlace cambió a "Deshacer"

4. **¿Te equivocaste?** Simplemente haz clic en "Deshacer" y la tarea volverá a estar pendiente

> **💡 Consejo:** Marcar tareas como completadas te da una sensación de logro y te ayuda a ver tu progreso.

---

### **3. Eliminar una Tarea**

![Paso 3: Eliminar tarea]

1. **Localiza la tarea** que deseas eliminar

2. **Haz clic en el enlace rojo "Eliminar"** que aparece al lado derecho

3. **La tarea desaparecerá** inmediatamente de tu lista

> **⚠️ Advertencia:** Una vez que elimines una tarea, no podrás recuperarla. Asegúrate de que realmente quieres borrarla.

---

### **4. Ver Todas tus Tareas**

La aplicación muestra automáticamente todas tus tareas en la página principal:

- **Tareas pendientes:** Aparecen en texto normal negro
- **Tareas completadas:** Aparecen tachadas y en color gris

Si no tienes ninguna tarea, verás el mensaje:
> *"No hay tareas pendientes. ¡Agrega una!"*

---

## 🎨 Interfaz de Usuario

### **Elementos de la Pantalla**

```
┌─────────────────────────────────────────┐
│           Mis Tareas                     │
├─────────────────────────────────────────┤
│ [¿Qué tienes que hacer hoy?] [Agregar]  │ ← Formulario para agregar
├─────────────────────────────────────────┤
│ ☐ Comprar leche    [Completar] [Eliminar]│ ← Tarea pendiente
│ ☑ Estudiar Python  [Deshacer]  [Eliminar]│ ← Tarea completada
│ ☐ Hacer ejercicio  [Completar] [Eliminar]│ ← Tarea pendiente
└─────────────────────────────────────────┘
```

---

## ❓ Preguntas Frecuentes (FAQ)

### **¿Cuántas tareas puedo agregar?**
No hay límite. Puedes agregar tantas tareas como necesites.

### **¿Las tareas se guardan cuando cierro el navegador?**
Sí, todas tus tareas se guardan en una base de datos y estarán ahí cuando vuelvas a abrir la aplicación.

### **¿Puedo cambiar el nombre de una tarea?**
En la versión actual, no puedes editar tareas existentes. Pero puedes eliminar la tarea y crear una nueva con el nombre correcto.

### **¿Puedo organizar las tareas por fecha o prioridad?**
La versión actual no incluye esta funcionalidad, pero es una mejora que se puede implementar en el futuro.

### **¿Necesito crear una cuenta?**
No, la aplicación no requiere registro ni inicio de sesión. Todas las tareas se guardan localmente.

### **¿Funciona en mi teléfono móvil?**
Sí, la aplicación está diseñada para funcionar en cualquier dispositivo con navegador web (computadoras, tablets, teléfonos).

---

## 🔒 Privacidad y Seguridad

- **Tus datos son privados:** Nadie más puede ver tus tareas
- **No compartimos información:** La aplicación no envía tus datos a terceros
- **Almacenamiento local:** Todas las tareas se guardan en la base de datos local de la aplicación

---

## 📞 Soporte y Ayuda

Si encuentras algún problema o tienes sugerencias:

1. **Reporta un problema:** Abre un "Issue" en el repositorio de GitHub
2. **Contacta al desarrollador:** [Incluir email o método de contacto]
3. **Consulta la documentación técnica:** Lee el archivo `README.md` para información más detallada

---

## 🎓 Consejos para Usar la Aplicación Efectivamente

### **Mejores Prácticas**

✅ **Sé específico:** En lugar de "Hacer tarea", escribe "Completar ejercicios de matemáticas del capítulo 5"

✅ **Revisa diariamente:** Abre la aplicación cada mañana para planificar tu día

✅ **Marca como completadas:** No olvides marcar las tareas cuando las termines para mantenerte motivado

✅ **Elimina lo innecesario:** Si una tarea ya no es relevante, elimínala para mantener tu lista limpia

❌ **Evita listas muy largas:** Si tienes demasiadas tareas, prioriza y enfócate en las más importantes

---

## 🆘 Problemas Comunes y Soluciones

### **Problema: "No puedo acceder a la aplicación"**
**Solución:**
- Verifica que estés usando la URL correcta
- Asegúrate de tener conexión a internet (si es versión en línea)
- Intenta con otro navegador

### **Problema: "Las tareas no se guardan"**
**Solución:**
- Verifica que JavaScript esté habilitado en tu navegador
- Borra la caché y las cookies del navegador
- Contacta al administrador si el problema persiste

### **Problema: "La página tarda mucho en cargar"**
**Solución:**
- Verifica tu conexión a internet
- Cierra otras pestañas del navegador
- Intenta más tarde si el servidor está sobrecargado

---

## 📅 Actualizaciones Futuras

Funcionalidades planeadas para próximas versiones:

- 📝 Editar tareas existentes
- 🗓️ Agregar fechas de vencimiento
- 🎨 Categorías y etiquetas de colores
- 🔔 Notificaciones y recordatorios
- 📊 Estadísticas de productividad

---

**¡Gracias por usar TodoTareasApp!**

*Mantente organizado y productivo* 🚀
