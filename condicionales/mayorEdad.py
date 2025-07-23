# Ejercicio: Mayor de edad
# Instrucciones:
# Solicita al usuario que ingrese su edad.
# Evalúa si la persona es mayor o menor de edad (18 años o más).
# Muestra el resultado correspondiente.
edadIngresada = int(input("Ingrese su edad"))
if edadIngresada >= 18:
    print(f"Tu edad es de: {edadIngresada} por lo que eres mayor de edad")
else: 
    print(f"Te faltan {18-edadIngresada} años para cumplir la mayoria de edad")