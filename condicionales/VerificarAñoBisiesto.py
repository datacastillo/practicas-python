# Escribe un programa que reciba un año y diga si es bisiesto.
año = int(input("Ingrese un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto")
else :
    print(f"{año} no es bisiesto")