# Ejercicio 8: Determinar si un número es múltiplo de 3 y/o 5.
# Solicita al usuario un número y evalúa si es múltiplo de 3, de 5 o de ambos.
# Imprime un mensaje dependiendo del caso.

numeroIngresado = int(input("Ingrese un numero: "))
if numeroIngresado % 3 == 0 and numeroIngresado % 5 == 0:
    print(f"{numeroIngresado}, es multiplo de 3 y 5")
elif numeroIngresado % 3 == 0:
    print(f"{numeroIngresado}, es multiplo de 3")
elif numeroIngresado % 5 == 0:
    print(f"{numeroIngresado}, es multiplo de 5")
else :
    print(f"{numeroIngresado}, no es multiplo de 3 ni de 5")