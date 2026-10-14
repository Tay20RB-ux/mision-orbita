# ============================================================
# Archivo: Ejercicio1Recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Tayrin Alexa Ramírez Barrantes
# Fecha: 11/10/2026      Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión.
# ============================================================

# --- Declaración de constantes ---
# Valores fijos de la misión.
CONSUMO_COMBUSTIBLE_DIARIO = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_DIARIO = 2
OXIGENO_EMERGENCIA = 5
CONSUMO_ENERGIA_DIARIO = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_DIARIO = 1
PROVISIONES_ADICIONALES = 3
TRAMOS_VIAJE = 2  # ida y regreso

# --- Entrada de datos ---
nombre_mision = input("Ingrese el nombre de la misión: ")
cantidad_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los días estimados para llegar al destino: "))

# --- Procesamiento ---
# El regreso dura lo mismo que la ida.
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Se multiplica por TRAMOS_VIAJE porque se gasta en la ida y en el regreso.
oxigeno_requerido = dias_viaje * CONSUMO_OXIGENO_DIARIO * TRAMOS_VIAJE * cantidad_tripulantes + OXIGENO_EMERGENCIA
energia_requerida = dias_viaje * CONSUMO_ENERGIA_DIARIO * TRAMOS_VIAJE + ENERGIA_EXPLORACION
provisiones_requeridas = dias_viaje * CONSUMO_PROVISIONES_DIARIO * cantidad_tripulantes * TRAMOS_VIAJE + PROVISIONES_ADICIONALES

# --- Salida de resultados ---
print("Misión:", nombre_mision)
print("Tripulantes:", cantidad_tripulantes)
print("Duración estimada hasta el destino:", dias_viaje, "días")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total_requerido, "unidades")
print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")
