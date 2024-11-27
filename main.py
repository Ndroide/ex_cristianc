from flask import Flask, render_template

# Crear una instancia de Flask
app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')  # Esta página se renderizará desde templates/index.html

# Ruta para el Ejercicio 1
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')  # Esta página se renderizará desde templates/ejercicio1.html

# Ruta para el Ejercicio 2
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')  # Esta página se renderizará desde templates/ejercicio2.html

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)