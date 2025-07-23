# Ejercicio 9: Programa para determinar si una persona puede votar.
# Solicita la edad al usuario y verifica si tiene 18 años o más.
# Si es así, imprime "Puede votar".
# Si no, imprime cuántos años faltan para que pueda votar.

edadIngresada = int(input("Ingrese su edad: "))
if edadIngresada >= 18:
    print("Puedes votar")
else:
    años_faltantes = 18 - edadIngresada
    print(f"Espera {años_faltantes} año{'s' if años_faltantes > 1 else ''} para poder votar")
