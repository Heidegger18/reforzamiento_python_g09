
"""
2. Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la
función una vez y mostrar el resultado por consola). Los números
serán ingresados y solicitados al usuario.
"""


def mostrar_cuadrados(a, b):
    while a + 1 != b:
        print("{}² = {}".format(a+1,pow(a+1, 2)))
        a = a + 1

num_1 = int(input("Ingrese un número: "))
num_2 = int(input("Ingrese un número: "))
mostrar_cuadrados(num_1, num_2)