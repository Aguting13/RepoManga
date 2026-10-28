from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/menu')
def menu():
    productos = [
        {'nombre': 'Café Espresso', 'descripcion': 'Café intenso y aromático.', 'precio': 1800},
        {'nombre': 'Cappuccino', 'descripcion': 'Espresso con leche y espuma.', 'precio': 2500},
        {'nombre': 'Tostado', 'descripcion': 'Pan tostado con jamón y queso.', 'precio': 3200},
        {'nombre': 'Cheesecake', 'descripcion': 'Porción de cheesecake casero.', 'precio': 2800}
    ]
    return render_template('menu.html', productos=productos)


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    mensaje = ''

    if request.method == 'POST':
        nombre = request.form['nombre']
        mensaje = '¡Gracias, ' + nombre + '! Recibimos tu mensaje.'

    return render_template('contacto.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
