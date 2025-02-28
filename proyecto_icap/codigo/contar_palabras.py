
if __name__ == "__main__":
    text = """Planteamiento general
El proyecto pretende ser un ejercicio práctico donde los estudiantes puedan poner en
marcha y evaluar de manera conjunta las tecnologías que han sido presentadas en la
asignatura Infraestructuras para la Computación de Altas Prestaciones. Para ello, el
proyecto plantea un supuesto práctico sencillo con un esquema general y una serie de
requisitos. Adicionalmente, se plantean algunas ideas adicionales y opcionales para
proporcionar una solución más avanzada.
Supuesto práctico
se necesita conocer los datos de la
temperatura de la laguna de forma periódica para obtener los siguientes datos
relevantes:
1) Necesitan saber cuándo la desviación de la temperatura semanal del agua del
Mar Menor es superior a 0.5.
2) Necesitan almacenar datos acumulativos de la temperatura del agua del Mar
Menor durante cada mes. El valor que se asocia a cada mes es:
a. La máxima desviación del conjunto de datos obtenidos durante el mes.
b. La diferencia de la máxima temperatura del mes respecto a la máxima
temperatura del mes anterior. Este valor será positivo o negativo
dependiendo de si la temperatura máxima del agua durante el mes ha
aumentado o ha disminuido, respectivamente, desde el mes anterior.
Para ello, cuentan con un servicio (ver Figura 1) que proporciona estadísticas del Mar
Menor con datos agregados de forma semanal aproximadamente. Estos datos tienen el
siguiente formato:
Fecha Medias Desviaciones
22/03/2017 16.7841 2.8715
30/03/2017 17.3299 4.0372
La columna Medias indica la temperatura en grados centígrados (ºC) media del agua en
la laguna durante los 7 días anteriores a la fecha del registro (columna Fecha) y la
columna Desviaciones muestra la desviación estándar del conjunto de muestras
durante esa semana. Las medidas de temperatura son recogidas mediante 12 puntos
(balizas verticales) distribuidas en la laguna. Posteriormente, el servicio preprocesa
estos datos en crudo y los publica en forma de media y desviación semanal.
Figura 1 - Servicio de Datos Científicos del Mar Menor
Figura 2 - Puntos de medida para la recogida de muestras en el Mar Menor
La startup cuenta con un equipo de ingenieros de datos que tienen que diseñar e
implementar una arquitectura de datos que almacene los datos necesitados de forma
permanente, incremental y accesible.
Es recomendable que la solución proporcionada sea confiable y tolerante a fallos.
Además, el cliente que ha contrato este desarrollo tiene diferentes áreas de trabajo y
prevén que la solución proporcionada crecerá adaptándose a nuevos temas de estudio,
por lo que la solución debe ser escalable y fácilmente extensible.
En particular, se necesita una solución con los siguientes componentes principales:
- Base de datos que implemente la permanencia de datos de la solución.
- Servicio Web que permita a los analistas de datos del cliente recuperar los datos
mediante llamadas GET RESTful (solución accesible). Este servicio debe tener la
siguiente API REST:
o /maxdiff: esta URI identifica las diferencias de máxima temperatura
asociadas a cada mes. Se debe incluir los parámetros month y year que
indica el mes y año del cuál se está solicitando este valor.
o /sd: esta URI identifica las máximas desviaciones de temperatura
calculadas de forma mensual. Tiene como parámetros obligatorios month
y year que indican el mes y año del cuál se está solicitando la desviación.
o /temp: esta URI identifica las medias de temperatura calculadas de forma
mensual. Tiene como parámetros month y year que indican el mes y año
del cuál se está solicitando la media de temperatura.
Un ejemplo de petición a este servicio Web sería:
GET http://[IP-address] /maxdiff?month=3&year =2017
- La solución tendrá una dirección de email preconfigurada a la cual se enviará una
alarma en el caso de que la desviación semanal de la temperatura del agua
supere el valor 0.5.
- La ingesta de datos se hará de forma manual. Una persona del equipo de análisis
de datos del cliente se encargará de subir un fichero CSV en el formato
anteriormente especificado. Para este proyecto, asumimos que esta persona
tiene tus credenciales y podrá subir el fichero de la misma forma que lo subes tú
en tu área de trabajo (no hace falta desarrollar un frontend gráfico o API para subir
el fichero).
- La solución debe soportar el crecimiento incremental de la base de datos. Se
debe soportar que se incorporen nuevos datos.
- No hace falta considerar ningún aspecto de gestión de usuarios para tu solución. 
TU Y TUS COMPAÑEROS DE EQUIPO SOIS LOS INGENIEROS DE DATOS DE LA
STARTUP:
Para hacer pruebas, este fichero lo deberéis dividir y generar varios ficheros CSV, cada
uno con un subconjunto de datos del fichero Temperatura.csv. Vuestra solución debe ser
capaz de incorporar al pipeline de datos estos ficheros CSV, sin importar si están
ordenados en el tiempo o no.
Hay que tener en cuenta que dos ficheros diferentes podrían tener medidas semanales
del mismo mes. Por ejemplo, un fichero podría tener la primera semana de un mes y otro
fichero el resto de las semanas. Además, el sistema no tiene que tratar de forma especial
que se suban ficheros con medidas repetidas (o incluso diferentes) con la misma fecha.
En caso de que esto ocurra, se debe tomar como valor correcto el del último fichero CSV
incorporado.
A continuación, se describe en más detalle la solución que tenéis que diseñar y
desplegar:
Esquema general de la solución en el cloud

El servicio Web está disponible mediante una dirección IP pública. Esta dirección no es
permanente, es la dirección asignada de forma automática por AWS a la infraestructura
que da soporte a tu servicio Web. La arquitectura de datos debe ser capaz de consumir
ficheros CSV con el formato especificado y automáticamente calcular y almacenar de
forma permanente y escalable los datos solicitados. Estos datos tienen que estar
accesibles por el servicio Web, para que éste pueda responder a las solicitudes GET.
Recuerda que es preferible que el servicio Web sea escalable y tolerante a fallos. Así
mismo, el pipeline de datos se recomienda que sea escalable y “real time” (los datos
deberían estar disponibles tan pronto como son incorporados en el pipeline, para que el
servicio Web los tenga disponibles). 
Requisitos del proyecto
Los requisitos mínimos establecidos para el proyecto son:
- Creación y configuración de la infraestructura necesaria que da soporte a los
distintos elementos de la solución.
- Creación y configuración de los métodos de seguridad necesarios a nivel de
comunicación.
- Implementación del servicio Web descrito en lenguaje Python.
- Implementación de un pipeline de datos que permita ingerir, almacenar y
procesar los datos de forma escalable, eficiente a nivel de costos y automatizada.
- Implementación de un sistema de alarma como se ha descrito.
- Automatización de la infraestructura mínima mediante AWS CLI y/o plantillas
CloudFormation. En el caso de comandos de AWS CLI se deben dar en un único
shell script. Como “infraestructura mínima” se refiere a los componentes de red
subyacentes y a máquinas virtuales.
Los requisitos opcionales para el proyecto son:
- Automatización de infraestructura y servicios de alto nivel mediante AWS CLI y/o
plantillas CloudFormation. En el caso de comandos de AWS CLI se deben dar en
un único shell script. Esta infraestructura incluye servicios AWS (e.g., de
almacenamiento) o componentes de red avanzados (e.g., balanceo de carga).
- Diseño e implementación de capacidades de escalabilidad y tolerancia a fallos,
basadas en las tecnologías vistas en clase como microservicios y/o
contenedores, balanceadores de carga, escalabilidad automática (e.g., escalado
vertical cuando se alcanza un número de peticiones HTTP por segundo), etc.
- Otros servicios AWS que se consideren oportunos para mejorar algún aspecto de
la solución propuesta. En este caso se deberá discutir previamente sobre las
posibles mejoras con el profesor o profesora. 
Entrega del proyecto
El proyecto debe estar bien documentado y contener obligatoriamente lo siguiente:
- Plan de trabajo del grupo: cronograma con distribución de tareas por persona y
resultados esperados.
- Arquitectura de la solución: diagrama representativo de la solución diseñada y
desplegada con todos los elementos principales y la comunicación entre ellos.
- Razonamiento sobre las decisiones de diseño tomadas para esta arquitectura.
- Listado de recursos y servicios involucrados en cada aspecto de la solución: para
cada recurso/servicio se indicará su ID, tipo AWS y función en la solución.
- Explicación clara y concisa de los pasos seguidos para implementar la solución y
de la automatización que se ha llevado a cabo.
- Ejemplos que demuestren la correcta ejecución de cada funcionalidad incluida
en la solución.
- Anexo de replicación: listado de pasos en orden para replicar la solución. Estos
pasos serán seguidos por el profesor para montar la solución en su espacio de
AWS y comprobar su funcionamiento.
- Anexo de automatización: Las plantillas CloudFormation y/o shell scripts de AWS
CLI se deben incluir como anexos en la documentación. Además, estas plantillas
y scripts se adjuntarán en la entrega como ficheros independientes.
La entrega consiste en el envío por AulaVirtual de la documentación del proyecto por
parte de todos los miembros del grupo antes de la fecha límite indicada a continuación.
Esta documentación deber ser un documento PDF, con formato libre. Además, en la
entrega de AulaVirtual se adjuntarán todos los ficheros de automatización necesarios
para replicar la solución (plantillas CloudFormation y shell scripts).
Antes de entregar el proyecto, hay que tener en cuenta que:
- Se debe añadir como email de notificación de la alarma solicitada en el
enunciado la dirección de email del profesor.
- Todos los miembros del grupo deben tener la misma solución desplegada en sus
áreas de trabajo de AWS Academy. Para evitar el consumo innecesario de créditos
de AWS, se recomienda eliminar los recursos al finalizar el proyecto. Un día antes
de la entrega, se debe volver a desplegar el proyecto en cada área de trabajo de
AWS, de modo que esté disponible para la corrección del profesor.
- Todos los recursos y servicios que forman parte de la solución deben tener el
prefijo “proy” en su nombre. 
"""
    
    print(len(text.strip().split(" ")))
