
"""
7. Crear una clase en python que contenga un método que revierta una
cadena de palabras.
Input: "Hola Pythonista, seguimos adelante"
Output: "adelante seguimos Pythonista Hola"
Llamarlo mínimo 2 veces y mostrar el resultado por consola.
"""

class Revertir():

    def revertir(self, entrada):
        entrada = entrada.replace(",", "")
        self.lista = entrada.split(" ")
        self.lista.reverse()
        self.salida = " ".join(self.lista)
        return self.salida


operacion = Revertir()

oracion_1 = "Hola Pythonista, seguimos adelante"
resultado_1 = operacion.revertir(oracion_1)
print(resultado_1)

oracion_2 = "Hola Pythonista, seguimos adelante"
resultado_2 = operacion.revertir(oracion_2)
print(resultado_2)
