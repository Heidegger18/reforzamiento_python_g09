
"""
15. Queremos consumir un JSON que se encuentra alojado en la nube el cual
nos traerá los datos de una persona como la edad, nombre, email, dirección
o nombre de la compañía en donde trabaja.
La url a consumir usando Python es la siguiente:
https://jsonplaceholder.typicode.com/users
Obtener respectivamente los valores necesarios para formar la siguiente
oración:
Bienvenido “nombre” “apellido”, usted tiene “edad” años. El correo que
nos proporcionó es “correo” y la compañía actual donde trabaja se llama
“nombreCompañía”. Dentro de sus datos también encontramos una website
que es: “nombreWeb”
Finalmente agregar un usuario al json obtenido pero sólo con los datos de
nombre, apellido, edad y compañía donde trabaja y finalmente mostrarlo en
consola (sólo ese usuario nuevo)
"""

import requests

def obtener_datos_personales(url):
    response = requests.get(url)

    #Verificamos si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        data = response.json()

        nombre = data[0]['name']
        apellido = data[0]['username']
        edad = data[0]['address']['geo']['lat'][:2]  # Los primeros 2 caracteres para simular la edad
        correo = data[0]['email']
        nombre_compania = data[0]['company']['name']
        nombre_web = data[0]['website']

        oracion = ("Bienvenido {} {}, usted tiene {} años.\n"
                   "El correo que nos proporcionó es {}\n"
                   "La compañía actual donde trabaja se llama {}.\n"
                   "Dentro de sus datos también encontramos una website que es: {}\n"
                   .format(nombre, apellido, edad, correo, nombre_compania, nombre_web))
        print(oracion)

        #Para agregar un nuevo usuario al JSON
        nuevo_usuario = {
            "name": "Estela",
            "username": "estela_23",
            "address": {
                "geo": {
                    "lat": "38.8648",
                    "lng": "-74.0352"
                }
            },
            "email": "estela23@gmail.com",
            "company": {
                "name": "ABC Company"
            }
        }
        data.append(nuevo_usuario)

        print("Nuevo usuario agregado:")
        print(nuevo_usuario)
    else:
        print("Error al obtener los datos. Código de estado: {}".format(response.status_code))

#URL del JSON a consumir
url = "https://jsonplaceholder.typicode.com/users"

obtener_datos_personales(url)
