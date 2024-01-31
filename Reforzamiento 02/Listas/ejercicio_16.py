
"""
16. Mostrar sólo los datos comprendidos entre la posición 10 y 35
"""
cien_primeros_enteros = []

i = 1
while i <= 100:
    cien_primeros_enteros.append(i)
    i += 1

muestra = cien_primeros_enteros[10:35]

print(muestra)