from flask import Flask, render_template, request

app = Flask(__name__)

# Usuarios registrados
users = {
    "juan": "admin",
    "pepe": "user"
}

# Ruta principal con los botones
@app.route('/')
def index():
    return render_template('index.html')

def format_currency(value):
    # Formato tipo moneda CLP
    return f"${value:,.0f}".replace(",", ".")

# Ejercicio 1: Formulario
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        precio_tarros = 9000 * tarros
        descuento = 0

        # Cálculo del descuento
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = precio_tarros * (1 - descuento)

        resultado = {
            'nombre': nombre,
            'precio_tarros': format_currency(precio_tarros),
            'total_con_descuento': format_currency(total_con_descuento)
        }

    return render_template('ejercicio1.html', resultado=resultado)

# Ejercicio 2: Formulario
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario in users and users[usuario] == contrasena:
            mensaje = f"Bienvenido {'administrador' if usuario == 'juan' else 'usuario'} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

# Ejecuta la aplicación
if __name__ == "__main__":
    app.run(debug=True)
