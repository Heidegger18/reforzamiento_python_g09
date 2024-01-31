
"""
19. Crea una lista vacía (con 10 posiciones), pedir al usuario c/u
sus valores y que finalmente se devuelva la suma y la media de los
números ingresados de la lista.
"""

numeros_ingresados = []

for i in range(10):
    valor = int(input("Ingrese un valor {}: ".format(i+1)))
    numeros_ingresados.append(valor)

#Suma → otra opción es con la función "sum(lista)"
suma = 0
for elemento in numeros_ingresados:
    suma = suma + elemento

#Media
media = suma/len(numeros_ingresados)

print("La suma es: {}".format(suma))
print("La media es: {}".format(media))