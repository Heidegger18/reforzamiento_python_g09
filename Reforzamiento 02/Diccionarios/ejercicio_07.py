
"""
7. Crear un diccionario con 6 departamentos en el país.
➢ Borrar cualquier departamento (uno) usando la palabra reservada del.
➢ Comprobar que no existe este departamento borrado dentro del diccionario.
"""

departamentos = {
    "departamento_1": "Lima",
    "departamento_2": "Chiclayo",
    "departamento_3": "Cajamarca",
    "departamento_4": "Ica",
    "departamento_5": "Huancayo",
    "departamento_6": "Arequipa"
}

del(departamentos["departamento_4"])

print(departamentos)