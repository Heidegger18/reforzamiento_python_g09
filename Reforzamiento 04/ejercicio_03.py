
"""
3. Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
persona= { 'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion']
"""

def obtener_profesion(persona):
    try:
        profesion = persona["profesion"]
        return profesion
    except KeyError:
        print("ERROR: La clave ""profesion"" no existe en el diccionario proporcionado.")
        print("SOLUCIÓN: Asegúrate de que la clave ""profesion"" esté presente.")
        return None

persona = {
    "nombre": "Max",
    "apellido": "Estela",
    "dni": 75852291,
    #"profesion": "Ingeniería de Sistemas"
}

profesion = obtener_profesion(persona)

if profesion is not None:
    print("La profesión de {} es: {}".format(persona["nombre"], profesion))
