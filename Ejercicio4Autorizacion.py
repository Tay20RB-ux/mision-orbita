# ============================================================
# Archivo: Ejercicio4Autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Tayrin Alexa Ramírez Barrantes
# Fecha: 11/10/2026      Versión: 1.0
# Descripción: Decide si se autoriza el lanzamiento de la misión.
# ============================================================

# --- Declaración de constantes ---
RESERVA_COMBUSTIBLE = 10

# --- Entrada de datos ---
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para llegar al destino: "))
combustible_regreso = int(input("Ingrese el combustible requerido para regresar: "))
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))
energia_disponible = int(input("Ingrese la energía disponible: "))
energia_requerida = int(input("Ingrese la energía requerida: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

# --- Procesamiento ---
# Se compara con el total (ida + regreso + reserva), no solo con la ida.
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# --- Decisión (condicional doble, sin anidación) ---
# Deben cumplirse las cuatro condiciones (and).
if (combustible_disponible >= combustible_total_requerido
        and oxigeno_disponible >= oxigeno_requerido
        and energia_disponible >= energia_requerida
        and provisiones_disponibles >= provisiones_requeridas):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")
