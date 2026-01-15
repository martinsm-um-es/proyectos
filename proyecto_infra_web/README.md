# Infraestructura Web Escalable en AWS

Este proyecto consiste en el diseño y despliegue automatizado de una infraestructura web altamente disponible y escalable utilizando Infraestructura como Código (IaC).

## Descripción

Se despliega una arquitectura de red completa en AWS que soporta una aplicación web contenerizada. El sistema está diseñado para ser tolerante a fallos y seguro, utilizando subredes públicas y privadas.

## Tecnologías Utilizadas

- **AWS CloudFormation**: Orquestación de toda la infraestructura (VPC, Subnets, EC2, Security Groups).
- **Docker**: Contenerización de la aplicación web (Flask).
- **Python (Flask)**: Aplicación backend ligera para demostración.
- **Redes AWS**:
  - **VPC & Subnetting**: Segmentación de red con zonas públicas (ALB, NatGateway) y privadas (Instancias de aplicación).
  - **Application Load Balancer (ALB)**: Distribución de tráfico.
  - **NAT Gateway**: Acceso seguro a internet para instancias privadas.

## Estructura del Proyecto

- `codigo/`:
  - `proy_infraestructura.yaml`: Plantilla principal de CloudFormation.
  - `Dockerfile`: Definición del contenedor de la aplicación.
  - `application.py`: Código fuente de la app Flask.
- `imgs/`: Diagramas de la arquitectura.
