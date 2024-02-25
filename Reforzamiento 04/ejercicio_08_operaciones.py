import math

def cargar_valor_entero():
    try:
        valor_entero = int(input("Ingrese un valor entero: "))
        return valor_entero
    except ValueError:
        print("ERROR: Debe ingresar un valor entero.")
        return None

def mostrar_raiz_cuadrada(valor):
    if valor is not None:
        raiz_cuadrada = math.sqrt(valor)
        print("La raíz cuadrada de {} es: {}".format(valor, raiz_cuadrada))

def mostrar_cuadrado_y_cubo(valor):
    if valor is not None:
        cuadrado = math.pow(valor, 2)
        cubo = math.pow(valor, 3)
        print("{} elevado al cuadrado es: {}".format(valor, cuadrado))
        print("{} elevado al cubo es: {}".format(valor, cubo))
