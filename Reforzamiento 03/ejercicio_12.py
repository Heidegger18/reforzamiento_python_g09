
"""
12. Realizar una clase que administre una agenda. Se debe almacenar en
un diccionario dentro de una lista para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:
Añadir contacto
Mostrar contactos
Buscar contacto
(Por DNI)
"""

class Agenda():

    def __init__(self):
        self.contacto = {}
        self.lista_contacto = []

    def añadir_contacto(self):
        self.contacto["Nombre"] = input("Nombre del contacto: ")
        self.contacto["Teléfono"] = int(input("Teléfono: "))
        self.contacto["Email"] = input("Email: ")
        self.contacto["DNI"] = int(input("DNI: "))

        self.lista_contacto.append(self.contacto)


    def mostrar_contactos(self):
        i = 1
        for elemento in self.lista_contacto:
            print("CONTACTO {}".format(i))
            print(elemento)
            i += 1

    def buscar_contacto(self, dni):
        for i in range(len(self.lista_contacto)):
            if dni == self.lista_contacto[i]["DNI"]:
                print(self.lista_contacto[i])
        print("No tiene ningún contacto registrado con ese DNI")



#Prueba
agenda = Agenda()

agenda.añadir_contacto()
agenda.añadir_contacto()

print("-------------------------------------------------------------------")

agenda.mostrar_contactos()

print("--------------------------------------------------------------------")

agenda.buscar_contacto(75852291)