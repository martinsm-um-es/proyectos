import json
import boto3
from decimal import Decimal
from datetime import datetime  # Importamos el módulo datetime

def lambda_handler(event, context):
    # Mostramos el evento recibido para depurar
    print("Evento recibido por la función Lambda: " + json.dumps(event, indent=2))

    # Conectamos con SNS
    sns = boto3.client('sns')
    alertTopic = 'proy-alarma-temperatura'
    snsTopicArn = [t['TopicArn'] for t in sns.list_topics()['Topics']
                   if t['TopicArn'].lower().endswith(':' + alertTopic.lower())][0]
    
    # Bandera para saber si se envió al menos una notificación
    alertas_enviadas = False
    
    # Iteramos por los registros en el evento de DynamoDB
    for record in event['Records']:
        newImage = record['dynamodb'].get('NewImage', None)
        
        if newImage:
            # Extraemos la desviación de la nueva imagen
            desviacion = newImage.get('Desviaciones', None)
            fecha = newImage.get('Fecha', None)
            
            if desviacion and fecha:
                desviacion_value = float(desviacion['N'])  # Convertimos la desviación a float
                
                # Aquí verificamos el tipo de valor de 'fecha' 
                # Si es una cadena, obtenemos su valor directamente
                if 'S' in fecha:
                    fecha_value = fecha['S']  # Obtenemos la cadena de fecha si está guardada como un string
                else:
                    fecha_value = str(fecha)  # Si no es 'S', lo convertimos a string de forma estándar
                
                # Verificamos si la desviación supera el umbral de 0.5
                if desviacion_value > 0.5:
                    # Preparamos el mensaje para la alerta con la fecha
                    mensaje = f"¡Alerta! La desviación de temperatura ha superado el umbral de 0.5°C: {desviacion_value}°C el {fecha_value}"
                    print(mensaje)

                    # Enviamos el mensaje a SNS
                    sns.publish(
                        TopicArn=snsTopicArn,
                        Message=mensaje,
                        Subject='Alerta de Desviación de Temperatura',
                        MessageStructure='raw'
                    )

                    # Indicamos que al menos una alerta fue enviada
                    alertas_enviadas = True

    # Verificamos si se envió alguna alerta
    if alertas_enviadas:
        return 'Alertas enviadas: desviación superior a 0.5°C detectada.'
    else:
        return "No se detectaron desviaciones superiores a 0.5°C"
