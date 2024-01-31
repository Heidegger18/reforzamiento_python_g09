
"""
3. Quita 2 elementos de tu nueva lista ítems por valor, no por índice.
"""

cursos = ["Big Data", "Base de Datos", "Inteligencia de Negocios",
          "Estadística", "Internet de las Cosas", "Sistemas Operativos"]

cursos.append("Inteligencia Artificial")
cursos.append("Sistemas Distribuidos")
cursos.append("Sistemas Inteligentes")
cursos.append("Minería de Datos")

#Quitar 2 elementos por valor (remove → por valor, pop → por índice)

cursos.remove("Sistemas Operativos")
cursos.remove("Sistemas Distribuidos")

print(cursos)