
import random

def generar_numeros_aleatorios():
    numeros_aleatorios = []
    for i in range(30):
        numero = random.randint(0, 100)
        numeros_aleatorios.append(numero)
    print("---- Lista de 30 números enteros aleatorios entre 0 y 100 ----")
    print(numeros_aleatorios)
    return numeros_aleatorios

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("---- Lista ordenada ----")
    print(lista_ordenada)
    return lista_ordenada