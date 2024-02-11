
"""
9. Crear una clase llamada círculo que contenga radio en su constructor y
que contenga un método área que devuelva el área de un círculo.
Aplicar excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.
Instanciar la clase respectivamente para dos diferentes radios.
Habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola.
"""
import math

class Circulo():

    def __init__(self):
        self.radio = 0
        self.area = 0

    def ingresar_radio(self):
        try:
            self.radio = float(input("Ingrese el radio: "))
        except:
            print("El valor del radio ingresado es inválido.")

    def calcular_area(self):
        self.area = math.pi * (self.radio ** 2)
        return self.area

    def calcular_perimetro(self):
        self.perimetro = 2 * math.pi * self.radio
        return self.perimetro


#Ejecución con radio válido
c1 = Circulo()
c1.ingresar_radio()
print("El perímetro es: {}".format(c1.calcular_perimetro()))
print("El área es: {}".format(c1.calcular_area()))

print("-----------------------------------")

#Ejecución con radio inválido
c2 = Circulo()
c2.ingresar_radio()
