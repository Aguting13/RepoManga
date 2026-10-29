# Café Cultural Escobar — Proyecto grupal

Proyecto web grupal realizado con **Python, Flask, HTML, CSS y MySQL**.

## Estructura

```text
cafe-cultural-esqueleto/
├── app.py
├── schema.sql
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── carta.html
│   ├── eventos.html
│   ├── nosotros.html
│   ├── contacto.html
│   └── admin.html
└── static/
    └── css/
        └── style.css
```

## Cómo arrancar el sitio

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Verificar que XAMPP tenga **Apache y MySQL en verde**.

3. Verificar que la base `cafe_cultural` exista en phpMyAdmin con las tablas cargadas. Si hace falta crearla desde cero, ejecutar `schema.sql`.

4. Ejecutar el servidor:

```bash
python app.py
```

5. Abrir en el navegador:

```text
http://localhost:5000
```

## Qué vas a ver al arrancar

El sitio carga con el menú funcionando y todas las páginas navegables, pero las secciones de datos (**Carta, Eventos y Admin**) aparecen vacías. Eso es porque los `# TODO` todavía no están completados.

Cada integrante del equipo tiene TODOs asignados según su rol.

## Roles y TODOs

- **Rol 1:** conexión Python + MySQL.
- **Rol 2:** `base.html` y `style.css`.
- **Rol 3:** lógica de Carta en Python.
- **Rol 4:** diseño/frontend de `carta.html` (TODO 8).
- **Rol 5:** lógica de Eventos e inscripciones en Python.
- **Rol 6:** diseño/frontend de `eventos.html` (TODO 9).
- **Rol 7:** lógica del formulario de Contacto.
- **Rol 8:** páginas estáticas Inicio y Nosotros.
- **Rol 9:** lógica y presentación del panel Admin (TODOs 6, 7 y 10).

> La guía oficial de TODOs entregada por el instructor es la referencia para completar cada rol.
