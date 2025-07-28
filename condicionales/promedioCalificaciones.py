# Calculadora de promedio y clasificación

calificaciones = []
numeroAprobados = 0
numeroReprobados = 0

numeroCalificaciones = int(input("¿Cuántas calificaciones vas a ingresar?: "))

for i in range(numeroCalificaciones):
    while True:
        try:
            nota = float(input(f"Ingrese calificación {i+1}: "))
            if 0 <= nota <= 100:
                calificaciones.append(nota)
                if nota >= 60:
                    numeroAprobados += 1
                else:
                    numeroReprobados += 1
                break 
            else:
                print("Calificación inválida. Debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")


promedio = sum(calificaciones) / len(calificaciones)
calificacion_max = max(calificaciones)
calificacion_min = min(calificaciones)

print("\nResultados:")
print(f"Calificaciones ingresadas: {calificaciones}")
print(f"Promedio general: {promedio:.2f}")
print(f"Calificación más alta: {calificacion_max}")
print(f"Calificación más baja: {calificacion_min}")
print(f"Número de aprobados (>= 60): {numeroAprobados}")
print(f"Número de reprobados (< 60): {numeroReprobados}")
