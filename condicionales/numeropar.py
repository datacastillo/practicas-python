# Ejercicio: Par o impar
# Instrucciones:
# Pide al usuario que ingrese un número entero.
# Luego determina si el número es par o impar.
# Muestra un mensaje indicando el resultado.

numeroIngresado = int(input("Ingrese un número: "))
if numeroIngresado % 2 == 0:
    print(f"El número {numeroIngresado} es par.")
else:
    print(f"El número {numeroIngresado} es impar.")
