# Café Cult

Proyecto de sitio web para un café, pensado para practicar los temas del curso.

## Tecnologías

- Python: programa principal y servidor local sencillo.
- HTML: páginas del sitio.
- MySQL: base de datos de productos y categorías.
- No se usa Flask.
- No se usa CSS.

## Páginas

- Inicio
- Carta
- Eventos
- Nosotros
- Galería
- Contacto

## Cómo verlo

1. Instalar Python.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Ejecutar:

```bash
python main.py
```

4. El programa abre el sitio en `http://localhost:8000/index.html`.

## Base de datos

El archivo `cafe_cult.sql` crea la base de datos, las tablas, la relación entre categorías y productos y algunos datos de ejemplo.

Para trabajar con MySQL desde Python se usa `mysql-connector-python`.
