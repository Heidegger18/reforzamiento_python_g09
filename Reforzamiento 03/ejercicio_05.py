
"""
5. Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados
por el usuario también y un segundo parámetro que eliminará de la
lista que fue ingresada a la función, finalmente el output de la función
será la lista actualizada sin el valor que se sacará de la lista. Mostrar
también la lista original y el número que fue eliminado.
"""

def eliminar_valor(lista, valor):

    if valor in lista:
        lista.remove(valor)
        return lista
    else:
        return "ERROR\nEl valor que desea eliminar no se encuentra en la lista"

#Creación de lista
tamaño = int(input("Ingrese el número de elementos de su lista: "))
mi_lista = []
for i in range(tamaño):
    elemento = int(input("Digite un valor: "))
    mi_lista.append(elemento)

print("Mi lista original es: {}".format(mi_lista))

#Definimos el valor que eliminaremos de la lista
mi_valor = int(input("Ingrese el valor que eliminará de su lista: "))
lista_actualizada = eliminar_valor(mi_lista, mi_valor)

print("Mi lista actualizada es: {}".format(lista_actualizada))