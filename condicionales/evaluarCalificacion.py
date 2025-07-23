# Ejercicio 6:
# Pide al usuario una calificación del 0 al 100. 
# Muestra un mensaje según el rango:
# 90-100: "Excelente", 80-89: "Muy bien", 70-79: "Bien", 60-69: "Suficiente", menos de 60: "Reprobado".

calificacionIngresada = int(input("Ingrese una calificacion entre 0 y 100"))
if calificacionIngresada >=90 and calificacionIngresada <=100:
    print(f"Calificacion: {calificacionIngresada} Excelente")
elif calificacionIngresada >=80 and calificacionIngresada <=89:
    print(f"Calificacion: {calificacionIngresada} Muy bien")
elif calificacionIngresada >=70 and calificacionIngresada <=79:
    print(f"Calificacion: {calificacionIngresada} Bien")
elif calificacionIngresada >=60 and calificacionIngresada <=69:
    print(f"Calificacion: {calificacionIngresada} Suficiente")
elif calificacionIngresada <60:
    print(f"Calificacion: {calificacionIngresada} Reprobado")
    