# Ejercicio: Calculadora básica
# Instrucciones:
# Solicita al usuario dos números y una operación (+, -, *, /).
# Realiza la operación correspondiente entre los dos números.
# Muestra el resultado o un mensaje si la operación no es válida o si hay error (como dividir entre cero).
numero1= int("Ingrese un numero")
numero2= int("Ingrese un numero")

opcion=input("Ponga el simbolo de la operacion que desea realizar (+, -, *, /)")
if opcion == "+":
    resultado=numero1 + numero2
elif opcion == "-":
    resultado=numero1 - numero2
elif opcion == "*":
    resultado=numero1 * numero2
elif opcion == "/":
    if numero2 != 0 :
        resultado=numero1 / numero2
    else:
        print("No se puede dividir entre 0")
else: print("Operacion invalida")

