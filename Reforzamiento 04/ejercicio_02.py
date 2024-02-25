
"""
2. Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]
"""

def acceder_elemento(lista, indice):
    try:
        elemento = lista[indice]
        return elemento
    except IndexError as e:
        print("Error: ", e)
        print("CAUSA: Estás intentando acceder a un índice que está fuera del rango de la lista.")
        print("SOLUCIÓN: Asegurarse de usar un índice válido dentro del rango de la lista.")
        return None

lista = [2, 6, 10, 4, 5, 23, 1]
indice = 10

resultado = acceder_elemento(lista, indice)

if resultado is not None:
    print("El elemento en el índice {} es: {}".format(indice, resultado))
else:
    print("No se pudo acceder al elemento debido a un error.")
