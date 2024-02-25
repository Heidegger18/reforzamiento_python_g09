
"""
1. Crear una función para encontrar el error en el siguiente bloque de
código. Crea una excepción para evitar que tu programa se bloquee y
además imprime un mensaje al usuario la causa y/o solución:
suma = 80 + “Hola Pythonista”
"""

def suma_valida():
    try:
        suma = 80 + "Hola Pythonista"
        return suma
    except TypeError as e:
        print("Error: ", e)
        print("CAUSA: Estás intentando sumar un número con una cadena de texto.")
        print("SOLUCIÓN: Asegurarse en sumar valores del mismo tipo, o convierte uno de ellos al tipo correcto.")
        return None

resultado = suma_valida()


if resultado is not None:
    print("El resultado de la suma es {}".format(resultado))
else:
    print("No se pudo realizar la suma debido a un error.")
