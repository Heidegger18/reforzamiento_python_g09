
"""
5. Convertir tu diccionario a una lista y mostrar en
consola el tipo de datos final que tiene.
"""

datos = {
    "nombre": "Max",
    "edad": 23,
    "salario": 1500
}

tipo_de_datos = type(list(datos))
print(tipo_de_datos)