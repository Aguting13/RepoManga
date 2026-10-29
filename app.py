from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)
app.secret_key = "cambiar-en-produccion"

# ============================================================
# CONFIGURACIÓN DE LA BASE DE DATOS
# ============================================================

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "cafe_cultural",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor
}


def get_db():
    """
    Abre una conexión a MySQL y la devuelve.

    TODO 1 (ROL 1 — Líder de Base de Datos)
    Debe devolver pymysql.connect(**DB_CONFIG)
    """
    # TODO 1: reemplazar el pass por la conexión real
    pass


# ============================================================
# RUTAS PÚBLICAS
# ============================================================

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/carta")
def carta():
    """
    TODO 2 (ROL 3 — Dev Carta, Lógica)
    SELECT * FROM productos WHERE disponible = 1
    """
    productos = []
    return render_template("carta.html", productos=productos)


@app.route("/eventos")
def eventos():
    """
    TODO 3 (ROL 5 — Dev Eventos, Lógica)
    SELECT * FROM eventos ORDER BY fecha
    """
    eventos = []
    return render_template("eventos.html", eventos=eventos)


@app.route("/eventos/inscribir", methods=["POST"])
def inscribir():
    """
    TODO 4 (ROL 5 — Dev Eventos, Lógica)
    INSERT INTO inscripciones (evento_id, nombre, email)
    VALUES (%s, %s, %s)
    """
    # TODO 4: completar el INSERT y hacer conn.commit()
    pass


@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    """
    TODO 5 (ROL 7 — Dev Contacto)
    INSERT INTO mensajes (nombre, email, mensaje)
    VALUES (%s, %s, %s)
    """
    if request.method == "POST":
        # TODO 5: completar el INSERT, commit y redirect
        pass
    return render_template("contacto.html")


# ============================================================
# PANEL DE ADMINISTRACIÓN
# ============================================================

@app.route("/admin")
def admin():
    """
    TODO 6 (ROL 9): mensajes
    SELECT * FROM mensajes ORDER BY fecha_envio DESC

    TODO 7 (ROL 9): inscripciones + JOIN con eventos
    """
    mensajes = []
    inscripciones = []

    return render_template(
        "admin.html",
        mensajes=mensajes,
        inscripciones=inscripciones
    )


# ============================================================
# ARRANQUE
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)
