from flask import Flask
from flask_cors import CORS
from routes import routes_bp

app = Flask(__name__)
CORS(app)


app.register_blueprint(routes_bp)


#app.route('/consultar_empleados_hoy', methods = ['GET'])(routes.consultar_empleados_hoy)
#app.route('/registrar_entrada', methods = ['POST'])(routes.registrar_entrada)
#app.route('/test', methods = ['POST'])(routes.test)


if __name__ == '__main__':
    app.run(debug=True)