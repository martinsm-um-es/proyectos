from flask import Flask, jsonify, request
import boto3
from datetime import datetime

# Crear la aplicación Flask
app = Flask(__name__)

# Conexión a DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabla = dynamodb.Table('ProyDatosPipeline')

# Endpoint /maxdiff: Obtener la diferencia máxima de temperatura de un mes y año especificados
@app.route('/maxdiff', methods=['GET'])
def get_maxdiff():
    # Obtener los parámetros de mes y año desde la solicitud
    month = request.args.get('month', type=int)
    year = request.args.get('year', type=int)

    if not month or not year:
        return jsonify({"error": "Faltan parámetros 'month' y 'year'"}), 400

    try:
        # Calcular el Mes-Año
        mes_anyo = f"{year}-{month:02d}"

        # Realizar una consulta en DynamoDB para obtener las diferencias máximas de temperatura
        response = tabla.query(
            KeyConditionExpression="MesAnyo = :mes_anyo",
            ExpressionAttributeValues={":mes_anyo": mes_anyo}
        )

        items = response.get('Items', [])

        if not items:
            return jsonify({"message": "No se encontraron datos para ese mes y año"}), 404

        # Calcular la diferencia máxima de temperatura
        max_diff = max([item['Medias'] for item in items]) - min([item['Medias'] for item in items])
        
        return jsonify({
            "MesAnyo": mes_anyo,
            "MaxDiff": float(max_diff)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint /sd: Obtener la máxima desviación de temperatura calculadas de forma mensual.
@app.route('/sd', methods=['GET'])
def get_sd():
    month = request.args.get('month', type=int)
    year = request.args.get('year', type=int)

    if not month or not year:
        return jsonify({"error": "Faltan parámetros 'month' y 'year'"}), 400

    try:
        # Calcular el Mes-Año
        mes_anyo = f"{year}-{month:02d}"

        # Realizar una consulta en DynamoDB para obtener las desviaciones de temperatura
        response = tabla.query(
            KeyConditionExpression="MesAnyo = :mes_anyo",
            ExpressionAttributeValues={":mes_anyo": mes_anyo}
        )

        items = response.get('Items', [])

        if not items:
            return jsonify({"message": "No se encontraron datos para ese mes y año"}), 404

        # Calcular la máxima desviación de temperatura
        max_sd = max(item['Desviaciones'] for item in items)
        
        return jsonify({"max_sd": float(max_sd)}), 200 # Convertimos de tipo 'Decimal' a float para que se pueda 'jsonizar'

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint /temp: Obtener la media de las temperaturas para un mes y año especificados
@app.route('/temp', methods=['GET'])
def get_temp():
    month = request.args.get('month', type=int)
    year = request.args.get('year', type=int)

    if not month or not year:
        return jsonify({"error": "Faltan parámetros 'month' y 'year'"}), 400

    try:
        # Calcular el Mes-Año
        mes_anyo = f"{year}-{month:02d}"

        # Realizar una consulta en DynamoDB para obtener las medias de temperatura
        response = tabla.query(
            KeyConditionExpression="MesAnyo = :mes_anyo",
            ExpressionAttributeValues={":mes_anyo": mes_anyo}
        )

        items = response.get('Items', [])

        if not items:
            return jsonify({"message": "No se encontraron datos para ese mes y año"}), 404

        # Calcular la media de temperatura
        medias = [item['Medias'] for item in items]
        promedio = sum(medias) / len(medias)

        return jsonify({
            "MesAnyo": mes_anyo,
            "MediaTemperatura": float(promedio)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Endpoint /health: Endpoint para el Health Check
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
