import boto3
import csv
import io
from datetime import datetime
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('ProyDatosPipeline')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    Manejador principal de la función Lambda. Procesa los datos CSV y los inserta o actualiza en DynamoDB.

    Args:
        event (dict): Datos del evento pasados a la función Lambda.
        context (object): Objeto de contexto de Lambda.

    Returns:
        dict: Un mensaje indicando éxito o fallo.
    """
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        response = s3.get_object(Bucket=bucket, Key=key)
        csv_data = response['Body'].read().decode('utf-8')

        csvfile = io.StringIO(csv_data)
        lector = csv.reader(csvfile)
        next(lector)  # Saltar la cabecera

        for fila in lector:
            fecha_str, medias, desviaciones = fila

             # Parsear la fecha y extraer el año y el mes
            fecha_date = datetime.strptime(fecha_str, "%Y/%m/%d")
            mes_anyo = f"{fecha_date.strftime('%Y-%m')}" # Combinar mes y año
            
            item = {
                'MesAnyo': mes_anyo,
                'Fecha': fecha_str,
                'Medias': Decimal(medias),  # Convertir a Decimal
                'Desviaciones': Decimal(desviaciones) # Convertir a Decimal
            }

            # Put (inserta/actualiza) en DynamoDB
            tabla.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': 'Datos CSV procesados y almacenados en DynamoDB exitosamente.'
        }
    except Exception as e:
        print(f"Error al procesar los datos: {e}")
        return {
            'statusCode': 500,
            'body': f'Error al procesar los datos: {str(e)}'
        }
        