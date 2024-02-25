
"""
8. Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que realizará la carga de un valor entero.
- Una función que mostrará por pantalla la raíz cuadrada de dicho
valor
- Y otra función el valor elevado al cuadrado y al cubo de dicho
número.
- Utilizar el módulo math de python.
"""

import ejercicio_08_operaciones as op

def main():
    valor_entero = op.cargar_valor_entero()
    op.mostrar_raiz_cuadrada(valor_entero)
    op.mostrar_cuadrado_y_cubo(valor_entero)

if __name__ == "__main__":
    main()