
"""
4. Invierte y muestra en consola tu lista de cursos.
"""

cursos = ["Big Data", "Base de Datos", "Inteligencia de Negocios",
          "Estadística", "Internet de las Cosas", "Sistemas Operativos"]

cursos.append("Inteligencia Artificial")
cursos.append("Sistemas Distribuidos")
cursos.append("Sistemas Inteligentes")
cursos.append("Minería de Datos")

cursos.remove("Sistemas Operativos")
cursos.remove("Sistemas Distribuidos")

cursos.reverse()

print(cursos)