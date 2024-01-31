
"""
Elimina el key edad tipo de tu diccionario, incluyendo su valor.
del var[‘key’]
"""

datos = {
    "nombre": "Max",
    "edad": 23,
    "salario": 1500
}

del(datos["edad"])

print(datos)