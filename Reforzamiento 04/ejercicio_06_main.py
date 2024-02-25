
"""
6. Creando un archivo principal donde llamará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones.
- La primera función cargará una un número entero que pedirá al
usuario que ingrese por consola un valor.
- La segunda función solamente sumará dos valores.
- Desde el archivo principal importar al módulo y sumar dos valores
usando las funciones anteriormente creadas en el módulo
"""

import ejercicio_06_operaciones as op

def main():
    numero1 = op.cargar_numero()
    numero2 = op.cargar_numero()

    if numero1 is not None and numero2 is not None:
        resultado = op.sumar_valores(numero1, numero2)
        print("La suma de los dos números es: {}".format(resultado))

if __name__ == "__main__":
    main()