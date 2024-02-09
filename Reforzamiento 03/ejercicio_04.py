
"""
4. Pedir al usuario que ingrese una oración con un mínimo de 3 palabras
la cual será usada por parámetro para una función que se creará e
indicará cuantas palabras existen dentro de la oración ingresada.
"""

def contar_palabras(oracion):
    if len(oracion.split(" ")) >= 3:
        palabras = oracion.split(" ")
        print("Cantidad de palabras:", len(palabras))
    else:
        print("La oración ingresada no tiene un mínimo de 3 palabras")

dato = input("Ingrese una oración: ")
contar_palabras(dato)