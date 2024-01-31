
"""
18. Crear una lista con los 15 primeros números impares,
luego agregar 3 números flotantes repetidos (los cuales son
impares dentro del rango indicado y que no sea el último impar).
    - Empezando desde 1 y no 0.
    - Agregar un cadena en la posición 3 de la lista.
    - Eliminar este valor string de la cadena usando del.
"""

quince_primeros_impares = [1, 3, 5, 7, 9,
                           11, 13, 15, 17, 19,
                           23, 25, 27, 29, 31]

quince_primeros_impares.append(3.0)
quince_primeros_impares.append(23.0)
quince_primeros_impares.append(29.0)

quince_primeros_impares.insert(3, "Python")
del(quince_primeros_impares[3])

print(quince_primeros_impares)