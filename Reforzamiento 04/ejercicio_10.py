
"""
10. Crear una función donde se permitirá guardar el nombre, apellido y
edad de un usuario en un fichero (agenda.txt), cada usuario tiene que
estar guardado en una línea diferente y cada dato de una persona tiene
que estar separados por comas.
"""

def agregar_usuario(nombre, apellido, edad):
    try:
        with open("agenda.txt", "a") as file:
            file.write("{},{},{}\n".format(nombre, apellido, edad))
        print("Usuario agregado exitosamente a la agenda")

    except Exception as e:
        print("ERROR al agregar usuario a la agenda: {}".format(e))


nombre = input("Ingrese el nombre del usuario: ")
apellido = input("Ingrese el apellido del usuario: ")
edad = input("Ingrese la edad del usuario: ")

agregar_usuario(nombre, apellido, edad)
