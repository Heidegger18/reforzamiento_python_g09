
"""
6. Devuelve la cantidad de veces que se repite un curso
(agregarla previamente a la lista) dentro de la lista.
"""

cursos = ["Big Data", "Base de Datos", "Inteligencia de Negocios",
          "Estadística", "Internet de las Cosas", "Sistemas Operativos"]

cursos.append("Big Data")
cursos.append("Big Data")
cursos.append("Big Data")

cantidad_Big_Data = cursos.count("Big Data")

print(cantidad_Big_Data)