
"""
11. Crear una función que creará el archivo calificaciones.txt que contiene
las calificaciones de un curso.
Escribir un programa que contenga las siguientes funciones:
- Una función que guarde el nombre, 2 notas y el promedio (el
promedio lo calculará la función antes de escribirlo en el fichero)
- Y una función que leerá el fichero anterior y dirá si el alumno X,
aprobó o no, tener en cuenta que si tiene un promedio mayor a día
tendrá un mensaje de “Alumno X, aprobado” de lo contrario “Alumno
X, desaprobado”
"""


def guardar_calificaciones(nombre, nota1, nota2):
    try:
        promedio = (nota1 + nota2) / 2
        with open("calificaciones.txt", "a") as file:
            file.write(f"{nombre},{nota1},{nota2},{promedio}\n")
        print("Calificaciones guardadas exitosamente")
    except Exception as e:
        print("ERROR al guardar calificaciones: {}".format(e))


def verificar_aprobacion(nombre_alumno, nota_minima_aprobacion):
    try:
        with open("calificaciones.txt", "r") as file:
            for linea in file:
                datos = linea.strip().split(",")
                nombre = datos[0]
                promedio = float(datos[3])
                if nombre == nombre_alumno:
                    if promedio >= nota_minima_aprobacion:
                        print("Alumno {} está aprobado".format(nombre_alumno))
                    else:
                        print("Alumno {} está desaprobado".format(nombre_alumno))
                    return
            print("No se encontraron calificaciones para el alumno {}".format(nombre_alumno))

    except FileNotFoundError:
        print("El archivo de calificaciones no existe")


guardar_calificaciones("Elvis", 18, 20)
guardar_calificaciones("Max", 19, 17)

print("--------------------------------")
verificar_aprobacion("Elvis", 11)
print("--------------------------------")
verificar_aprobacion("Max", 10)
print("--------------------------------")
verificar_aprobacion("Estela", 11)
