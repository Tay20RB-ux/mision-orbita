# ============================================================
# Archivo: Ejercicio2Combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Tayrin Alexa Ramírez Barrantes
# Fecha: 11/10/2026      Versión: 1.0
# Descripción: Verifica el combustible y advierte si el margen es bajo.
# ============================================================

# --- Declaración de constantes ---
RESERVA_COMBUSTIBLE = 10
MARGEN_MINIMO_ADICIONAL = 10  # límite para advertir

# --- Entrada de datos ---
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para el viaje de ida: "))
combustible_regreso = int(input("Ingrese el combustible requerido para el viaje de regreso: "))

# --- Procesamiento ---
# Se necesita combustible para ir, volver y la reserva.
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total_requerido

# --- Salida de resultados (siempre se muestran) ---
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible requerido para llegar:", combustible_ida, "unidades")
print("Combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total_requerido, "unidades")
print("Combustible adicional:", combustible_adicional, "unidades")

# --- Decisión (condicional simple) ---
# Solo se advierte si sobra menos de 10 (con 10 exactos no).
if combustible_adicional < MARGEN_MINIMO_ADICIONAL:
    print("Advertencia: el margen adicional de combustible es bajo.")
