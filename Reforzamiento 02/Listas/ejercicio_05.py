
"""
5. Obtén la cantidad total ítems que tienes
en tu lista creada y mostrar el resultado en
consola. (Pista: len(lista))
"""

cursos = ["Big Data", "Base de Datos", "Inteligencia de Negocios",
          "Estadística", "Internet de las Cosas", "Sistemas Operativos"]

cursos.append("Inteligencia Artificial")
cursos.append("Sistemas Distribuidos")
cursos.append("Sistemas Inteligentes")
cursos.append("Minería de Datos")

cursos.remove("Sistemas Operativos")
cursos.remove("Sistemas Distribuidos")

cantidad = len(cursos)
print(cantidad)