# Ejercicio 7: Verificar si un número es positivo, negativo o cero
# El programa debe pedir al usuario que ingrese un número entero.
# Luego debe decir si es positivo, negativo o cero.
# Si es positivo, además debe decir si es mayor que 100 o no.

numeroIngresado = int(input("Ingrese un numero: "))
if numeroIngresado > 0:
    print(f"{numeroIngresado} : Es un numero positivo")
    if numeroIngresado >= 100:
        print("Su numero es mayor a 100")
    else:
        print(f"Su numero le falta : {100-numeroIngresado} , para llegar a 100")
elif numeroIngresado < 0:
    print(f"{numeroIngresado} es un numero negativo")
else :
    print("Su numero es un 0")