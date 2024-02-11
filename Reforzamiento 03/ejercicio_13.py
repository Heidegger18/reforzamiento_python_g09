
"""
13. Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase
Persona y agregue un atributo sueldo y muestre si debe pagar
impuestos (10% de su sueldo-encapsulamiento) (sueldo superior a
4000)
Instanciar la clase Empleado, mostrar el sueldo del empleado y cuánto
debe pagar de impuesto
"""

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):

    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def calcular_impuestos(self):
        if self.sueldo > 4000:
            impuesto = self.sueldo * 0.10
            return impuesto


nombre = input("Nombre del empleado: ")
edad = int(input("Edad: "))
sueldo = float(input("Sueldo: "))

e1 = Empleado(nombre, edad, sueldo)

print("El sueldo del empleado es: {}".format(e1.sueldo))
print("El impuesto a pagar del empleador es: {}".format(e1.calcular_impuestos()))