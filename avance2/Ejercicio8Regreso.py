# ============================================================
# Archivo: Ejercicio8Regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Tayrin Alexa Ramírez Barrantes
# Fecha: 05/11/2026       Versión: 1.0
# Descripción: Evalúa el regreso de la nave o la supervivencia de la tripulación varada.
# ============================================================

# --- Declaración de constantes ---
# Consumo diario de cada recurso (unidades ficticias de misión).
CONSUMO_COMBUSTIBLE_DIARIO = 8
CONSUMO_OXIGENO_DIARIO = 2        # por tripulante
CONSUMO_ENERGIA_DIARIO = 5
CONSUMO_PROVISIONES_DIARIO = 1    # por tripulante

# --- Entrada de datos ---
cantidad_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese la cantidad de días del viaje de ida: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# --- Procesamiento previo ---
# El consumo por tripulante se calcula una sola vez porque no cambia durante el regreso.
consumo_oxigeno_dia = cantidad_tripulantes * CONSUMO_OXIGENO_DIARIO
consumo_provisiones_dia = cantidad_tripulantes * CONSUMO_PROVISIONES_DIARIO
# En este ejercicio no se suma la reserva de emergencia.
combustible_regreso_necesario = dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO

# --- Decisión principal: caso A (regresa) o caso B (queda varada) ---
if combustible >= combustible_regreso_necesario:
    # --- Caso A: simulación de los días del regreso ---
    dias_completados = 0
    regreso_en_curso = True

    # El ciclo termina cuando se completan los días o cuando un recurso no alcanza.
    while dias_completados < dias_viaje and regreso_en_curso:
        # Se verifica antes de consumir para no dejar recursos negativos.
        if (combustible >= CONSUMO_COMBUSTIBLE_DIARIO
                and oxigeno >= consumo_oxigeno_dia
                and energia >= CONSUMO_ENERGIA_DIARIO
                and provisiones >= consumo_provisiones_dia):
            combustible = combustible - CONSUMO_COMBUSTIBLE_DIARIO
            oxigeno = oxigeno - consumo_oxigeno_dia
            energia = energia - CONSUMO_ENERGIA_DIARIO
            provisiones = provisiones - consumo_provisiones_dia
            dias_completados = dias_completados + 1
            print("Día " + str(dias_completados) + " | Combustible: " + str(combustible)
                  + " | Oxígeno: " + str(oxigeno) + " | Energía: " + str(energia)
                  + " | Provisiones: " + str(provisiones))
        else:
            regreso_en_curso = False

    # --- Salida del caso A ---
    if dias_completados == dias_viaje:
        print("La tripulación regresó exitosamente a la Tierra.")
        print("Combustible restante: " + str(combustible) + " unidades")
        print("Oxígeno restante: " + str(oxigeno) + " unidades")
        print("Energía restante: " + str(energia) + " unidades")
        print("Provisiones restantes: " + str(provisiones) + " unidades")
    else:
        print("El regreso se interrumpió en el día " + str(dias_completados + 1) + ".")
        # El combustible no se revisa aquí porque ya se verificó que alcanzaba para todo el regreso.
        if oxigeno < consumo_oxigeno_dia:
            print("Recurso insuficiente: oxígeno")
        if energia < CONSUMO_ENERGIA_DIARIO:
            print("Recurso insuficiente: energía")
        if provisiones < consumo_provisiones_dia:
            print("Recurso insuficiente: provisiones")
        print("La tripulación no completó el regreso.")
else:
    # --- Caso B: tripulación varada, se estiman los días de supervivencia ---
    print("La tripulación quedó varada en el destino.")
    dias_oxigeno = oxigeno // consumo_oxigeno_dia
    dias_energia = energia // CONSUMO_ENERGIA_DIARIO
    dias_provisiones = provisiones // consumo_provisiones_dia

    # El menor de los tres valores se obtiene con condicionales (sin min()).
    supervivencia_dias = dias_oxigeno
    if dias_energia < supervivencia_dias:
        supervivencia_dias = dias_energia
    if dias_provisiones < supervivencia_dias:
        supervivencia_dias = dias_provisiones

    # Si hay empate, se agregan todos los recursos con el valor mínimo, separados por coma.
    recursos_limitantes = ""
    if dias_oxigeno == supervivencia_dias:
        recursos_limitantes = "oxígeno"
    if dias_energia == supervivencia_dias:
        if recursos_limitantes == "":
            recursos_limitantes = "energía"
        else:
            recursos_limitantes = recursos_limitantes + ", energía"
    if dias_provisiones == supervivencia_dias:
        if recursos_limitantes == "":
            recursos_limitantes = "provisiones"
        else:
            recursos_limitantes = recursos_limitantes + ", provisiones"

    print("Días por oxígeno: " + str(dias_oxigeno))
    print("Días por energía: " + str(dias_energia))
    print("Días por provisiones: " + str(dias_provisiones))
    print("Supervivencia estimada: " + str(supervivencia_dias) + " días")
    print("Recurso(s) limitante(s): " + recursos_limitantes)
