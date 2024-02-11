
def ingresar_nombre_apellido():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    return nombre, apellido

def pedir_tipo_seguro():
    tipo_seguro = input("¿Qué tipo de seguro tiene? ")
    return tipo_seguro

def es_mayor_de_edad():
    edad = int(input("Ingrese su edad: "))
    return edad >= 18
