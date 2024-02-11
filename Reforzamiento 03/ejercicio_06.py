
"""
6. Escribir una clase en Python que contenga un método que convierta un
número entero en su cubo y contenga otro método que obtenga el
cuadrado de ese resultado. El valor inicial de resultado deberá estar
creado en el constructor. Considerar un método en la cual le pedirá al
usuario ingresar un valor numérico.
"""

class Operacion():

    def __init__(self):
        self.resultado = 0

    def ingresar_valor(self):
        self.valor = int(input("Ingrese un valor: "))

    def convertir_cubo(self):
        self.cubo = self.valor ** 3
        return self.cubo

    def obtener_resultado(self):
        self.resultado = self.cubo ** 2
        return self.resultado

op = Operacion()
op.ingresar_valor()
print(op.valor)

#Cubo
print(op.convertir_cubo())
print(op.cubo)

#Cuadrado del resultado
print(op.obtener_resultado())
print(op.resultado)