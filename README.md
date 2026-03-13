[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ezLsxraL)
# Repositorio Unidad \#
## Información del estudiante
Nombre:  Miguel Santiago Lopez Motta
ID.:  000530940
## Descripción del repositorio
### Sistema de Monitoreo de Combustible y Seguridad en Ruta (SMCS)

####  Descripción del Proyecto
Este repositorio contiene el código y la documentación del **Reto de la Unidad 3**, el cual consiste en el desarrollo de un Sistema de Monitoreo de Combustible y Seguridad en Ruta (SMCS) básico para un avión bimotor comercial. 

El objetivo principal del programa es simular un vuelo a través de una ruta programada de 5 waypoints, prediciendo el consumo de combustible en tiempo real y tomando decisiones de desvío automático basadas en la reserva legal y las condiciones meteorológicas.

####  Características Principales
* **Cálculo Dinámico de Consumo:** 
* **Análisis Meteorológico en Ruta:** 
    * **Headwind:** 
    * **Tailwind:** 
    * **Viento cruzado/nulo:** Mantiene el consumo base.
* **Sistema de Alerta Crítica:** Monitorea constantemente el tanque frente a una Reserva Legal. Si el sistema proyecta que un tramo comprometerá esta reserva, aborta la ruta automáticamente y ordena el desvío al aeropuerto alterno más cercano.

####  Estructura del Repositorio
* `smcs_vuelo.py`: Archivo principal con el código fuente en Python.
* `Bitácora`: Documentación de las Fases 1 (Tablas) y Fase 2 (Pseudocódigo).
* `Capturas/`: Evidencias de ejecución mostrando un escenario de vuelo exitoso y un escenario de misión abortada por viento en contra.

##  Declaración de Uso de IA
Para el desarrollo de este reto, se utilizó asistencia de Inteligencia Artificial como herramienta de apoyo para estructurar y dar un acabado profesional al repositorio. Los detalles específicos sobre cómo se implementó esta ayuda y las modificaciones realizadas para adaptar el código a los requerimientos exactos del reto se encuentran documentados en cada seccion.