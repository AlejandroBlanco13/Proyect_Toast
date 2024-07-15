from flask import Flask
import routes

app = Flask(__name__)

# Registrar la ruta para consultar datos
app.route('/consultar_empleados')(routes.consultar_empleados)


if __name__ == '__main__':
    app.run(debug=True)