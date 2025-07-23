# Reto: Escribe un programa que pida al usuario un número entero positivo
# y luego imprima la suma de todos los números desde 1 hasta ese número.
# Por ejemplo, si el usuario ingresa 5, el programa debe mostrar 15 (1+2+3+4+5).

numeroIngresado = int(input("ingrese un numero: "))
resultado = 0
for i in range(1,numeroIngresado+1):
    resultado += i

    
print(f"El resultado es de sumar de uno en uno. Desde 1 hasta {numeroIngresado} da como resultado: {resultado}")
