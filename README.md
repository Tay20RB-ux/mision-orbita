# Misión Órbita

Simulador básico de exploración espacial en Python, desarrollado de forma progresiva en tres avances para el curso **SOFT-01 Principios de programación 1** (Universidad CENFOTEC, Escuela de Ingeniería del Software, sección SCV6, periodo C3-2026).

## Integrante

- Tayrin Alexa Ramírez Barrantes (trabajo individual)

Docente facilitador: Verónica Mora Lezcano

## Avance 1: Preparación de la misión

Cuatro programas independientes que representan la preparación de una misión (entrada → procesamiento → decisión → salida). Los valores son unidades ficticias de misión y se manejan como enteros positivos.

| Archivo | Descripción | Estructura de control |
|---|---|---|
| `avance1/Ejercicio1Recursos.py` | Calcula combustible (ida, regreso, reserva, total), oxígeno, energía y provisiones. | Secuencial |
| `avance1/Ejercicio2Combustible.py` | Verifica el combustible y advierte si el margen adicional es menor que 10. | Condicional simple |
| `avance1/Ejercicio3SoporteTripulacion.py` | Verifica si hay oxígeno y provisiones suficientes para la tripulación. | Condicional doble |
| `avance1/Ejercicio4Autorizacion.py` | Autoriza o rechaza el lanzamiento según combustible, oxígeno, energía y provisiones. | Condicional doble sin anidación |

La documentación (tablas de variables, diagramas de flujo, código y casos de prueba) está en `documentacion/Avance1.pdf`.

## Estructura del repositorio

```
mision-orbita/
├── README.md
├── avance1/
│   ├── Ejercicio1Recursos.py
│   ├── Ejercicio2Combustible.py
│   ├── Ejercicio3SoporteTripulacion.py
│   └── Ejercicio4Autorizacion.py
└── documentacion/
    └── Avance1.pdf
```

## Cómo ejecutar los programas

Requisitos: Python 3 instalado (no se usan librerías externas). Desde la carpeta raíz del repositorio:

```
python avance1/Ejercicio1Recursos.py
python avance1/Ejercicio2Combustible.py
python avance1/Ejercicio3SoporteTripulacion.py
python avance1/Ejercicio4Autorizacion.py
```

Cada programa solicita sus datos por consola y muestra los resultados en pantalla.

## Convenciones y estilos

- Variables en `snake_case`, descriptivas y en minúscula.
- Constantes en MAYÚSCULAS con guion bajo, declaradas al inicio del archivo; no hay números mágicos en las fórmulas.
- Indentación de 4 espacios, espacios alrededor de operadores y líneas en blanco entre bloques lógicos.
- Cada archivo inicia con un encabezado (archivo, curso, integrantes, fecha, versión y descripción).
- Cada bloque lógico (constantes, entrada, procesamiento, decisión, salida) está precedido por un comentario.
- Mensajes de consola con unidades.
- Restricciones del avance: sin ciclos, colecciones, funciones propias (`def`), librerías, archivos ni POO; sin condicionales anidadas ni `elif`; solo entrada y salida por consola.
- Mensajes de commit descriptivos, por ejemplo: "Agrega validación de combustible de regreso en ejercicio 4".
