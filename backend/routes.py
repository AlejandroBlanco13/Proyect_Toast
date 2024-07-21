from flask import Blueprint, jsonify, request
from database import Database

# Obtener la instancia única de la base de datos


routes_bp = Blueprint('routes',__name__)
db = Database()

def formato_fila(row):
    id,cedula, fecha, hora_entrada, hora_salida, nombre, apellido1 = row
    formato_fecha = fecha.strftime("%d-%m-%Y")
    hora_entrada_formato = hora_entrada.strftime("%H:%M")

    if hora_salida is None:
        hora_salida_formato = "En trabajo"
    else:
        hora_salida_formato = hora_salida.strftime("%H:%M")
    return {
        "id": id,
        "cedula": cedula,
        "fecha": formato_fecha,
        "hora_entrada": hora_entrada_formato,
        "hora_salida": hora_salida_formato,
        "nombre": nombre + " " + apellido1
    }

@routes_bp.route('/consultar_empleados_hoy', methods=['GET'])
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
        cursor.close()
        return str(e), 500


@routes_bp.route('/registrar_entrada', methods=['POST'])
def registrar_entrada():
    try:
        cursor = db.cursor()
        # Obtener datos de la solicitud JSON
        data = request.get_json()
        print(data)
        cedula = str(data["cedula"])
        fecha = str(data["fecha"])
        hora_entrada = str(data["hora_entrada"])

        print(cedula, fecha, hora_entrada)
        query = "INSERT INTO asistencia (cedula, fecha, hora_entrada) VALUES (%s, %s, %s);"
        values = (cedula, fecha, hora_entrada)
        cursor.execute(query, values)

        db.commit()  # Hacer commit para guardar los cambios        
        cursor.close()  # Cerrar el cursor después de hacer commit
        return jsonify({"mensaje": "Entrada registrada correctamente"}), 200
    except Exception as e:
        # Devolver el mensaje de error para facilitar la depuración
        db.rollback()
        
        cursor.close()
        return jsonify({"error": str(e)}), 500



@routes_bp.route('/marcar_salida', methods=['PUT'])
def registrar_salida():
    try:
        cursor = db.cursor()
        # Obtener datos de la solicitud JSON
        data = request.get_json()
        print("penesito",data)
        cedula = str(data["cedula"])
        fecha = str(data["fecha"])
        hora_salida = str(data["hora_salida"])

        print(cedula, fecha, hora_salida)
        query = "UPDATE asistencia SET hora_salida = %s WHERE cedula = %s AND fecha = %s;"
        values = (hora_salida, cedula, fecha)
        cursor.execute(query, values)

        db.commit()  # Hacer commit para guardar los cambios        
        cursor.close()  # Cerrar el cursor después de hacer commit
        return jsonify({"mensaje": "Salida registrada correctamente"}), 200
    except Exception as e:
        # Devolver el mensaje de error para facilitar la depuración
        
        db.rollback()
        cursor.close()
        return jsonify({"error": str(e)}), 500



@routes_bp.route('/test', methods = ['POST'])
def test():
    try:
        cursor = db.cursor()
        data = request.get_json()
        cursor.execute("INSERT INTO asistencia (cedula, fecha, hora_entrada, hora_salida) VALUES ('123456789', '2024/10/10', '3:00', '3:00');")
        db.commit()
        cursor.close()
        return jsonify({"mensaje": "Test insertado"}), 200
    except Exception as e:
        cursor.close()
        return str(e), 500