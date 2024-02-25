
"""
5. Crear un módulo que validará nombres de usuarios. Dicho módulo,
deberá tener una función y cumplir con los siguientes requisitos:
- Crear un archivo principal (main.py) donde importará al módulo
creado.
- El nombre de usuario debe tener una longitud mínima de 7
caracteres y un máximo de 12.
- El nombre de usuario debe ser alfanumérico (usar isalnum() )
- Nombre de usuario con menos de 7 caracteres, retorna el mensaje
"El nombre de usuario debe contener al menos 7 caracteres".
- Nombre de usuario con más de 12 caracteres, retorna el mensaje
"El nombre de usuario no puede contener más de 12 caracteres".
- Nombre de usuario con caracteres distintos a los alfanuméricos,
retorna el mensaje "El nombre de usuario puede contener solo
letras y números".
- Si el nombre de usuario válido, la función retornará True.
"""

# main.py
import ejercicio_05_modulo as m

def main():
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    resultado = m.validar_usuario(nombre_usuario)
    if resultado == True:
        print("El nombre de usuario es válido.")
    else:
        print("Error: {}".format(resultado))

if __name__ == "__main__":
    main()
