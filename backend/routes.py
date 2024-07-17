from flask import app, jsonify, request, Flask
from flask_cors import CORS
from database import Database

# Obtener la instancia única de la base de datos
db = Database()

app = Flask(__name__)
CORS(app)


def formato_fila(row):
    id,cedula, fecha, hora_entrada, hora_salida, nombre, apellido1 = row
    formato_fecha = fecha.strftime("%d-%m-%Y")
    hora_entrada_formato = hora_entrada.strftime("%H:%M")
    hora_salida_formato = hora_salida.strftime("%H:%M")
    return {
        "id": id,
        "cedula": cedula,
        "fecha": formato_fecha,
        "hora_entrada": hora_entrada_formato,
        "hora_salida": hora_salida_formato,
        "nombre": nombre + " " + apellido1
    }


@app.route('/consultar_empleados_hoy', methods=['GET'])
def consultar_empleados_hoy():
    try:
        # Ejemplo de consulta a la base de datos
        cursor = db.cursor()
        cursor.execute("SELECT * FROM ConsultarEmpleadosHoy();")
        data = cursor.fetchall()
        for row in data:
            print(row)
        cursor.close()

        data = [formato_fila(row) for row in data]

        return jsonify(data), 200
    except Exception as e:
        return str(e), 500


@app.route('/registrar_entrada', methods=['POST'])
def registrar_entrada():
    try:
        cursor = db.cursor()
        # Obtener datos de la solicitud JSON
        data = request.get_json()
        print(data)
        # Usar los datos de la solicitud para insertar en la base de datos
        query = "INSERT INTO asistencia (cedula, fecha, hora_entrada, hora_salida) VALUES (%s, %s, %s, %s);"
        values = (data['cedula'], data['fecha'], data['hora_entrada'], data['hora_salida'])
        cursor.execute(query, values)

        
        cursor.close()  # Cerrar el cursor después de hacer commit
        return jsonify({"mensaje": "Entrada registrada correctamente"}), 200
    except Exception as e:
        # Devolver el mensaje de error para facilitar la depuración
        return jsonify({"error": str(e)}), 500
    
@app.route('/test', methods = ['POST'])
def test():
    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO test(nombre) VALUES ('test');")

        cursor.close()
        return jsonify({"mensaje": "Test insertado"}), 200
    except Exception as e:
        return str(e), 500