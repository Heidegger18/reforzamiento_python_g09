
"""
10. Crear una clase llamada Alumno que tenga como atributos el nombre,
edad y la nota final del alumno. Crear los métodos para inicializar sus
atributos, otro para imprimirlos y un método para mostrar un mensaje
con el resultado de la nota y si ha aprobado (mayor o igual a 11) o no el
alumno.Instanciar la clase por lo menos 3 veces (3 alumnos)
"""

class Alumno():

    def __init__(self):
        self.nombre = ""
        self.edad = ""
        self.nota_final = ""

    def iniciar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))
        self.nota_final = float(input("Ingrese su nota final: "))

    def mostrar_datos(self):
        print("--------DATOS--------")
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))
        print("Nota final: {}".format(self.nota_final))

    def mostrar_estado(self):
        print("--------ESTADO--------")
        if self.nota_final >= 11:
            print("Su nota es {}, su estado es aprobado".format(self.nota_final))
        else:
            print("Su nota es {}, su estado es desaprobado".format(self.nota_final))


#Instancia 1 de la clase
alumno_1 = Alumno()
alumno_1.iniciar_datos()
alumno_1.mostrar_datos()
alumno_1.mostrar_estado()

print("--------------------------------------")

#Instancia 2 de la clase
alumno_2 = Alumno()
alumno_2.iniciar_datos()
alumno_2.mostrar_datos()
alumno_2.mostrar_estado()

print("--------------------------------------")

#Instancia 3 de la clase
alumno_3 = Alumno()
alumno_3.iniciar_datos()
alumno_3.mostrar_datos()
alumno_3.mostrar_estado()
