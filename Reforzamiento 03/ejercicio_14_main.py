
"""
14. Crear un módulo y un archivo principal (donde llamará las funciones del
módulo) el módulo tendrá una función para ingresar nombres y
apellidos, una función para pedir el tipo de seguro que tiene y otra
función para indicar si es mayor de edad o no (pedir la edad desde
consola)
"""

import ejercicio_14_modulo as modulo

def main():
    nombre, apellido = modulo.ingresar_nombre_apellido()
    print("Nombre: {}".format(nombre))
    print("Apellido: {}".format(apellido))

    tipo_seguro = modulo.pedir_tipo_seguro()
    print("Tiene el seguro de tipo: {}".format(tipo_seguro))

    if modulo.es_mayor_de_edad():
        print("Es mayor de edad.")
    else:
        print("No es mayor de edad.")

if __name__ == "__main__":
    main()