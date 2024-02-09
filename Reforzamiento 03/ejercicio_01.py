
"""
1. Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los
números cuya sumatoria de dígitos es menor que 10. Utilizar una o
más funciones, según sea conveniente.
"""

def numero_sumatoria_digitos_mayor(x, y):

    suma_1 = 0
    for i in x:
        suma_1 = suma_1 + int(i)

    suma_2 = 0
    for i in y:
        suma_2 = suma_2 + int(i)

    if suma_1 > suma_2:
        print(x)
    elif suma_1 < suma_2:
        print(y)
    else:
        print("Son iguales")
        print(x, y)

    """
    if suma_1 < 10:
        print(x)
    elif suma_2 < 10:
        print(y)
    """

num_1 = input("Digite un número: ")
num_2 = input("Digite un número: ")
numero_sumatoria_digitos_mayor(num_1, num_2)