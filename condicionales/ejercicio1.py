personasMayores = []
contadorPersonas= 0
for i in range(6):
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad"))
    if edad >60:
        personasMayores.append(nombre)
        contadorPersonas+=1

if contadorPersonas>0:       
    print(f"Total de personas: {contadorPersonas}")     
else:
    print("No hay personas mayores a 60")        
