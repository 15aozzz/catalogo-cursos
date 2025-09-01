📚 Catálogo de Cursos

Proyecto desarrollado en **Django** para gestionar un catálogo de cursos con operaciones CRUD (Crear, Leer, Actualizar y Eliminar).
Permite registrar cursos con información básica, listarlos, editarlos y eliminarlos desde una interfaz web sencilla.

---

📌 Autor

Proyecto realizado por:
-Joan Valdiviezo -> (dev)
-Luis Cajacurio  -> (dev)

---

📝 Descripción

Este sistema fue creado con el objetivo de administrar cursos online de manera eficiente.
Incluye:

- Registro de cursos con nombre, duración, plataforma y dificultad.
- Listado de cursos registrados en el sistema.
- Edición de información de un curso existente.
- Eliminación de cursos que ya no estén vigentes.
- Plantillas HTML con CSS para un diseño simple y funcional.

Estructura principal del proyecto:

catalogo-cursos-master
├── crud_cursos/        # Configuración principal del proyecto Django
├── cursos/             # Aplicación encargada de la gestión de cursos
│   ├── models.py       # Definición del modelo de Curso
│   ├── views.py        # Lógica de negocio (controladores)
│   ├── urls.py         # Rutas de la app
│   ├── templates/      # Vistas en HTML (listar, registrar, editar)
│   └── static/css/     # Archivos de estilo
└── manage.py           # Script de administración de Django

---

⚙️ Instalación

1. Clonar el repositorio
   git clone https://github.com/15aozzz/catalogo-cursos.git
   cd catalogo-cursos

2. Crear y activar entorno virtual
   python -m venv venv
   # En Windows
   venv\Scripts\activate
   # En Linux / Mac
   source venv/bin/activate

3. Instalar dependencias
   pip install django

4. Realizar migraciones
   python manage.py makemigrations
   python manage.py migrate


5. Ejecutar el servidor
   python manage.py runserver

---

🚀 Uso

1. Accede a la aplicación desde tu navegador en  
   http://127.0.0.1:8000/cursos/

2. Funcionalidades disponibles:
   - Registrar un curso nuevo.
   - Listar los cursos existentes.
   - Editar información de un curso.
   - Eliminar cursos.


---

👨‍💻 Tecnologías utilizadas

- Python 3
- Django
- HTML5 / CSS3

