
"""
12. Crear una función decoradora que dará los buenos días antes de
ejecutar una función a ser decorada y luego de ser ejecutada lanzará
un mensaje diciendo “Hasta luego”.
La función a decorar pedirá el nombre de una persona y retornará el
mensaje “Soy ‘nombre’”.
"""

def decorador_saludo(funcion):
    def wrapper(*args, **kwargs):
        print("¡Buenos días!")
        resultado = funcion(*args, **kwargs)
        print("¡Hasta luego!")
        return resultado
    return wrapper

@decorador_saludo
def saludar(nombre):
    return "Soy {}".format(nombre)

mensaje = saludar("Max")
print(mensaje)
