
"""
17. Crear una lista con los 10 primeros números al
cuadrado y mostrar el resultado en terminal.
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
for elemento in lista:
    lista[i] = elemento * elemento
    i += 1
print(lista)

"""
import numpy as np
vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
vector_2 = vector * vector
print(list(vector_2))
"""