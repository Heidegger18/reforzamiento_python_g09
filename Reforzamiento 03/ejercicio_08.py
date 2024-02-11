
"""
8. Crear una clase que contenga dos métodos, uno que pida ingresar un
nombre y apellido, un método para pedir su edad y otro método que lo
imprima ambos resultados, pero estarán contenidos en un diccionario.
Comprobar ambos métodos instanciado la clase respectivamente.
Considerar en el constructor los valores necesarios.
"""

class Persona():

    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.edad = ""

    def ingresar_nombre_completo(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")

    def ingresar_edad(self):
        self.edad = int(input("Ingrese su edad: "))

    def imprimir_datos(self):

        datos = {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Edad": self.edad
        }

        print("-------------------")
        print("Datos de la persona")
        for key, value in datos.items():
            print("{}: {}".format(key, value))

p1 = Persona()
p1.ingresar_nombre_completo()
p1.ingresar_edad()
p1.imprimir_datos()