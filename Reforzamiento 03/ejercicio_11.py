
"""
11. Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una
persona. Implementar los métodos necesarios para inicializar los
atributos (constructor), un método para mostrar los datos e indicar si
la persona es mayor de edad o no y otro método que bonificación que
retornará el 20% adicional de su sueldo.
Instanciar por lo menos la clase con 2 diferentes personas.
"""

class Persona():

    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mostrar_datos(self):
        print("-----------DATOS-----------")
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))
        print("Sueldo: {}".format(self.sueldo))

        if self.edad >= 18:
            print("Usted es mayor de edad")
        else:
            print("Usted no es mayor de edad")

    def calcular_bonificacion(self):
        bonificacion = self.sueldo + (self.sueldo * 0.20)
        return bonificacion


p1 = Persona("Max", 24, 1000)
p1.mostrar_datos()
print("Su bonificación es: {}".format(p1.calcular_bonificacion()))

p2 = Persona("Elvis", 20, 850)
p2.mostrar_datos()
print("Su bonificación es: {}".format(p2.calcular_bonificacion()))
