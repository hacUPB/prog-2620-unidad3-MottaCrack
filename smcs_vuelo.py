# Bloque 2: Función de cálculo de consumo
def calcular_consumo_tramo(distancia, viento):
    consumo_estandar = distancia * CONSUMO_BASE
    
    viento_limpio = viento.strip().lower()
    
    if viento_limpio == "contra":
        consumo_final = consumo_estandar + (consumo_estandar * FACTOR_CONTRA)
    elif viento_limpio == "favor":
        consumo_final = consumo_estandar - (consumo_estandar * FACTOR_FAVOR)
    else:
        consumo_final = consumo_estandar
        
    return consumo_final


# Bloque 1: Inicialización de variables y constantes
CONSUMO_BASE = 3.2
FACTOR_CONTRA = 1.2
FACTOR_FAVOR = 0.2
RESERVA_LEGAL = 1000

# Solicitamos la capacidad inicial al usuario
capacidad_inicial = float(input("Ingrese la cantidad inicial de combustible (kg): "))
combustible_actual = capacidad_inicial


# Bloque 3: Bucle principal de la ruta
for tramo_actual in range(1, 5 + 1):
    print(f"\n--- Iniciando simulación del tramo: {tramo_actual} ---")
    
    distancia = float(input("Ingrese la distancia del tramo (km): "))
    viento = input("Ingrese la condición del viento (contra, favor, nulo): ")
    
    consumo_del_tramo = calcular_consumo_tramo(distancia, viento)
    
    combustible_proyectado = combustible_actual - consumo_del_tramo
    
    if combustible_proyectado <= RESERVA_LEGAL:
        print("¡ALERTA CRÍTICA! La reserva legal se verá comprometida.")
        print("Abortando ruta. Desviando al aeropuerto alterno más cercano.")
        break
        #Aquí se usó IA para comprobar el funcionamiento del código usando valores representativos en las variables y constantes. La IA sugirió usar "Break" para ahorrar líneas de código.
    else:
        combustible_actual = combustible_proyectado
        print("Tramo completado exitosamente.")
        print(f"Combustible restante en el tanque: {combustible_actual:.2f} kg")

print("\nSimulación de vuelo finalizada.")