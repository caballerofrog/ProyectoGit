from PersonaClass import Personas

cantTrabajador = int(input('Ingrese la cantidad de trbajador:'))
listaTrabajador=[]
for i in range(1,cantTrabajador+1):
    nombre = input("Ïngresa el nombre:")
    edad = int(input("Ingrese edad:"))
    trabajo = input("Ingresar trabajo:")

    objPersona = Personas(nombre,edad,trabajo)
    listaTrabajador.append(objPersona)

for i in listaTrabajador:
    print(f"{i.nombre:>10}{i.edad:>10}{i.trabajo:>10}")



