from flask import jsonify
from database import Database

# Obtener la instancia única de la base de datos
db = Database()

def consultar_empleados():
    try:
        # Ejemplo de consulta a la base de datos
        cursor = db.cursor()
        cursor.execute("SELECT * FROM asistencia;")
        data = cursor.fetchall()
        cursor.close()

        return jsonify(data), 200
    except Exception as e:
        return str(e), 500
