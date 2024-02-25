
"""
7. Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que genere 30 números enteros aleatorios entre 0 y
100, que muestre en pantalla esta lista.
- Otra función que ordene los valores de una lista y volver a
mostrarla
"""

import ejercicio_07_operaciones as op

def main():

    lista_aleatoria = op.generar_numeros_aleatorios()

    lista_ordenada = op.ordenar_lista(lista_aleatoria)

if __name__ == "__main__":
    main()