# ============================================================
# Archivo: Ejercicio3SoporteTripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Tayrin Alexa Ramírez Barrantes
# Fecha: 11/10/2026      Versión: 1.0
# Descripción: Verifica si hay oxígeno y provisiones para la tripulación.
# ============================================================

# --- Entrada de datos ---
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

# --- Decisión (condicional doble) ---
# and: se necesitan los dos recursos. >=: tener justo lo requerido alcanza.
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")
