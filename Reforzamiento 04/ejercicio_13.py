
"""
13. Haciendo el uso de *args y **kwargs aplicarlo debidamente para usar
decorar una función que recibirá 4 argumentos los cuales se
multiplicaran entre ellos.
Mensaje previo al usar el decorador “Está por ejecutarse la función” y
mensaje luego de usar el decorador “La función ha sido ejecutado
correctamente”
"""

def decorador_mensaje(funcion):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función")
        resultado = funcion(*args, **kwargs)
        print("La función ha sido ejecutada correctamente")
        return resultado
    return wrapper

@decorador_mensaje
def multiplicar(*args):
    resultado = 1
    for arg in args:
        resultado = resultado * arg
    return resultado

resultado = multiplicar(23, 3, 18, 8)
print("El resultado de la multiplicación es: {}".format(resultado))
