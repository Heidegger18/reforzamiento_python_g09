
"""
8. Ingresar el nombre de tu carrera dentro de los valores que
tienes en tu diccionario ya creado.
➢ Mostrar en consola los valores de su variable final (ya sea diccionario o lista).
"""

datos = {
    "nombre": "Max",
    "edad": 23,
    "salario": 1500
}

datos["carrera"] = "Ingeniería de Sistemas"

lista = list(datos.values())

variable_final = lista[-1]
print(variable_final)
