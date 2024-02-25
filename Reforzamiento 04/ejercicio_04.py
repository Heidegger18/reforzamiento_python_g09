
"""
4. Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
string = "Hello Pythonista"
print(string/0)
"""

def division_string(string, divisor):
    try:
        result = string / divisor
        return result
    except ZeroDivisionError:
        print("ERROR: No puedes dividir un string por cero.")
        print("SOLUCIÓN: Debe asegurarse de que el divisor no sea cero.")
        return None

string = "Hello Pythonista"
divisor = 0

resultado = division_string(string, divisor)

if resultado is not None:
    print("El resultado de la división es: {}".format(resultado))
