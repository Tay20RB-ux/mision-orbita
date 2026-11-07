# ============================================================
# Archivo: Ejercicio7Exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Tayrin Alexa Ramírez Barrantes
# Fecha: 05/11/2026       Versión: 1.0
# Descripción: Menú repetido de actividades de exploración científica.
# ============================================================

# --- Declaración de constantes ---
# Opciones del menú y costos de cada actividad (unidades ficticias de misión).
OPCION_ANALIZAR_TERRENO = 1
OPCION_RECOLECTAR_MUESTRA = 2
OPCION_REALIZAR_OBSERVACION = 3
OPCION_FINALIZAR = 4

ENERGIA_ANALIZAR_TERRENO = 8
PROVISIONES_ANALIZAR_TERRENO = 0
PUNTOS_ANALIZAR_TERRENO = 10

ENERGIA_RECOLECTAR_MUESTRA = 12
PROVISIONES_RECOLECTAR_MUESTRA = 2
PUNTOS_RECOLECTAR_MUESTRA = 20

ENERGIA_REALIZAR_OBSERVACION = 5
PROVISIONES_REALIZAR_OBSERVACION = 0
PUNTOS_REALIZAR_OBSERVACION = 8

# --- Entrada de datos ---
energia_disponible = int(input("Ingrese la energía disponible al llegar al destino: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles al llegar al destino: "))

# --- Inicialización del estado de la exploración ---
# Contadores y acumulador empiezan en 0; la variable de control permite el ciclo.
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
explorando = True

# --- Ciclo del menú ---
# El ciclo termina solo cuando explorando pasa a False (opción 4 o recursos insuficientes).
while explorando:
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")
    opcion = int(input("Seleccione una actividad: "))

    # --- Decisión múltiple sobre la opción elegida ---
    if opcion == OPCION_FINALIZAR:
        print("Exploración finalizada por la tripulación.")
        explorando = False
    elif (opcion == OPCION_ANALIZAR_TERRENO
          or opcion == OPCION_RECOLECTAR_MUESTRA
          or opcion == OPCION_REALIZAR_OBSERVACION):
        # Primero se obtienen los datos de la actividad elegida.
        if opcion == OPCION_ANALIZAR_TERRENO:
            nombre_actividad = "Analizar terreno"
            energia_actividad = ENERGIA_ANALIZAR_TERRENO
            provisiones_actividad = PROVISIONES_ANALIZAR_TERRENO
            puntos_actividad = PUNTOS_ANALIZAR_TERRENO
        elif opcion == OPCION_RECOLECTAR_MUESTRA:
            nombre_actividad = "Recolectar muestra"
            energia_actividad = ENERGIA_RECOLECTAR_MUESTRA
            provisiones_actividad = PROVISIONES_RECOLECTAR_MUESTRA
            puntos_actividad = PUNTOS_RECOLECTAR_MUESTRA
        else:
            nombre_actividad = "Realizar observación"
            energia_actividad = ENERGIA_REALIZAR_OBSERVACION
            provisiones_actividad = PROVISIONES_REALIZAR_OBSERVACION
            puntos_actividad = PUNTOS_REALIZAR_OBSERVACION

        # Se compara con >= porque tener justo lo necesario sí alcanza.
        if energia_disponible >= energia_actividad and provisiones_disponibles >= provisiones_actividad:
            energia_disponible = energia_disponible - energia_actividad
            provisiones_disponibles = provisiones_disponibles - provisiones_actividad
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + puntos_actividad
            # Solo la recolección de muestras aumenta este contador.
            if opcion == OPCION_RECOLECTAR_MUESTRA:
                muestras_recolectadas = muestras_recolectadas + 1
            print("Actividad realizada: " + nombre_actividad + ". Puntos obtenidos: " + str(puntos_actividad))
        else:
            # El estado no cambia y el menú termina aunque otra actividad más barata sí alcanzara.
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            explorando = False
    else:
        # Opción inválida: no cambia nada y el menú se muestra de nuevo.
        print("Opción no válida.")

# --- Salida del resumen final ---
print("Actividades realizadas: " + str(actividades_realizadas))
print("Muestras recolectadas: " + str(muestras_recolectadas))
print("Puntos científicos: " + str(puntos_cientificos))
print("Energía restante: " + str(energia_disponible) + " unidades")
print("Provisiones restantes: " + str(provisiones_disponibles) + " unidades")
