# Fase 1: Análisis del Problema y Tabla de Datos

En esta fase, definimos la arquitectura de la información del Sistema de Monitoreo de Combustible y Seguridad en Ruta (SMCS). Antes de programar, es crucial establecer qué datos entran al sistema, qué información debe procesar y cuáles serán los resultados que el piloto visualizará.

## 1. Tabla de Entradas (Inputs)

Esta tabla define los datos dinámicos que el sistema necesitará recibir en cada iteración (es decir, en cada tramo del vuelo) para poder calcular el consumo actualizado.

| Dato a solicitar | Tipo de Dato | Descripción según el reto |
| :--- | :--- | :--- |
| distancia | Float | La longitud en kilómetros del tramo actual que la aeronave va a recorrer. |
| viento | String | La condición meteorológica del viento en el tramo. Opciones válidas: "contra", "favor", "cruzado" o "nulo". |

## 2. Tabla de Salidas (Outputs)

Aquí se detalla la información crítica que el SMCS debe devolver al usuario (el piloto) como resultado del procesamiento de los datos de entrada y el estado del tanque.

| Información a mostrar | Condición de activación | Descripción |
| :--- | :--- | :--- |
| **Alerta Crítica** | combustible_actual | Mensaje de emergencia que indica que el combustible caerá por debajo del límite legal. Instruye abortar la ruta y desviar al alterno. |
| **Estado del Vuelo** | combustible_actual | Confirmación de que el tramo se puede completar con seguridad. |
| **Combustible Restante** | En cada tramo seguro | El valor actualizado del combustible disponible en el tanque tras restar el consumo del tramo. |

## 3. Tabla de Constantes y Variables de Control

Esta sección clasifica los valores fijos que rigen la física del vuelo (los cuales deben ser investigados y justificados) y las variables que controlan el flujo del programa, como el bucle principal.

| Nombre sugerido | Tipo | Descripción y justificación |
| :--- | :--- | :--- |
| CONSUMO_BASE | Constante | Consumo estándar de la aeronave en kg/km. *(Pendiente por investigar).* |
| FACTOR_CONTRA | Constante | Porcentaje de aumento de consumo por viento en contra. *(Pendiente por investigar).* |
| FACTOR_FAVOR | Constante | Porcentaje de reducción de consumo por viento a favor. *(Pendiente por investigar).* |
| RESERVA_LEGAL | Constante | Límite mínimo legal de combustible en kg para emergencias. *(Pendiente por investigar).* |
| capacidad_inicial | Variable | Cantidad inicial de combustible en el tanque al momento del despegue (kg). |
| combustible_actual | Variable | **Variable de control de seguridad:** Se actualiza restando el consumo en cada tramo. Si rompe el límite de reserva, detiene la ejecución. |
| tramo_actual | Variable | **Variable de control de bucle:** Contador que va del 1 al 5. Finaliza el programa cuando llega a 5 tramos completados. |

---

# Fase 2: Diseño de la Solución (Algoritmia)

Esta fase traduce las reglas de negocio del SMCS en una estructura lógica computacional. El siguiente pseudocódigo detalla el flujo de ejecución, definiendo dónde ocurren las funciones, el bucle iterativo de la ruta y las decisiones condicionales para la gestión de la reserva de combustible.

## 1. Lógica Principal del Programa **En esta sección se hace uso de IA como apoyo para mantener el contenido organizado y mantener limpia la documentación**

**Aquí el contenido fue escrito por el programador pero se le pasó el archivo original a la IA (Específicamente Gemini) con el propósito de ordenar y dar un formato mas profesional**

El algoritmo se divide en tres bloques principales:
1.  **Inicialización:** Definición de las variables investigadas y el tanque inicial.
2.  **Módulo de Cálculo:** Una función aislada encargada exclusivamente de aplicar las penalizaciones o beneficios del viento sobre el consumo base.
3.  **Bucle de Navegación:** Un ciclo que itera a lo largo de los 5 tramos de la ruta, evalúa proyecciones de consumo y toma la decisión de continuar o abortar el vuelo mediante el uso de la instrucción `break`.

## 2. Pseudocódigo

```text
INICIO DEL PROGRAMA

  // Bloque 1: Inicialización de variables y constantes
  Definir CONSUMO_BASE, FACTOR_CONTRA, FACTOR_FAVOR, RESERVA_LEGAL
  Imprimir "Ingrese la cantidad inicial de combustible (kg): "
  Leer capacidad_inicial
  combustible_actual = capacidad_inicial

  // Bloque 2: Función de cálculo de consumo
  FUNCIÓN calcular_consumo_tramo(distancia, viento):
    consumo_estandar = distancia * CONSUMO_BASE
    
    // Condicionales para el factor viento
    SI viento es "contra" ENTONCES:
      consumo_final = consumo_estandar + (consumo_estandar * FACTOR_CONTRA)
    SINO SI viento es "favor" ENTONCES:
      consumo_final = consumo_estandar - (consumo_estandar * FACTOR_FAVOR)
    SINO:
      // Caso para viento cruzado o nulo
      consumo_final = consumo_estandar
    FIN SI
    
    RETORNAR consumo_final
  FIN FUNCIÓN

  // Bloque 3: Bucle principal de la ruta
  PARA tramo_actual DESDE 1 HASTA 5 CON PASO 1:
    Imprimir "--- Iniciando simulación del tramo: ", tramo_actual, " ---"
    
    Imprimir "Ingrese la distancia del tramo (km): "
    Leer distancia
    Imprimir "Ingrese la condición del viento (contra, favor, nulo): "
    Leer viento
    
    // Llamada a la función de cálculo
    consumo_del_tramo = calcular_consumo_tramo(distancia, viento)
    
    // Proyección del escenario antes de hacer efectivo el consumo
    combustible_proyectado = combustible_actual - consumo_del_tramo
    
    // Condicional de seguridad (Evaluación de reserva)
    SI combustible_proyectado <= RESERVA_LEGAL ENTONCES:
      Imprimir "¡ALERTA CRÍTICA! La reserva legal se verá comprometida."
      Imprimir "Abortando ruta. Desviando al aeropuerto alterno más cercano."
      ROMPER BUCLE (break)
    SINO:
      // Ejecución del tramo y actualización del tanque
      combustible_actual = combustible_proyectado
      Imprimir "Tramo completado exitosamente."
      Imprimir "Combustible restante en el tanque: ", combustible_actual, " kg"
    FIN SI
    
  FIN PARA

  Imprimir "Simulación de vuelo finalizada."

FIN DEL PROGRAMA