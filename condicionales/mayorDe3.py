# Escribe un programa que reciba tres números enteros y determine cuál es el mayor de ellos.
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))


if num1 >= num2 and num1 >= num3:
    print(f"El numero {num1} es el mayor de los 3 numeros ingresados")
elif num2 >= num1 and num2 >= num3:
    print(f"El numero {num2} es el mayor de los 3 numeros ingresados")
elif num3 >= num1 and num3 >= num2:
    print(f"El numero {num3} es el mayor de los 3 numeros ingresados")
