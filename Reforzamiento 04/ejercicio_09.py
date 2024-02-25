
"""
9. Crear una función que pida al usuario un número entero entre 1 y 20 y
guarde en un fichero (que no existe) con el nombre tabla.txt la tabla
de multiplicar de ese número, done n es el número introducido
"""

def generar_tabla_multiplicar():
    try:
        numero = int(input("Ingrese un número entero entre 1 y 20: "))
        if numero < 1 or numero > 20:
            print("El número debe estar entre 1 y 20")
            return

        tabla = []
        for i in range(1, 11):
            tabla.append("{} x {} = {}\n".format(numero, i, numero * i))

        with open("tabla.txt", "w") as file:
            file.writelines(tabla)

        print("La tabla de multiplicar del número {} se ha guardado"
              " en el archivo tabla.txt.".format(numero))

    except ValueError:
        print("ERROR: Debe ingresar un número entero válido.")

generar_tabla_multiplicar()
