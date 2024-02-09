
"""
3. Crear una función que sume los dígitos del número ingresado y
muestre por consola la suma de estos dígitos.
"""

def suma_digitos(numero):
    suma = 0
    for i in numero:
        suma = suma + int(i)
    return suma

n = input("Ingrese un número: ")
print(suma_digitos(n))