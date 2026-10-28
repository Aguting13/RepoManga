import mysql.connector


def conectar_base_datos():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cafe_cult"
    )
    return conexion


def obtener_productos():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre, descripcion, precio FROM productos")
    productos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return productos
