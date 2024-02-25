
def cargar_numero():
    try:
        numero = int(input("Ingrese un número entero: "))
        return numero
    except ValueError:
        print("ERROR: Debe ingresar un número entero.")
        return None

def sumar_valores(valor1, valor2):
    return valor1 + valor2
