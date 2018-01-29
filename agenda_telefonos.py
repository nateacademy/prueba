

salida = False
agenda = {"rojo": "red",
          "amarillo": "yellow"}

while not salida:
    accion = input("¿Que quieres hacer? [Añadir numero[A] / Consultar numero[C]] / Salir [S]: ")

    # Accion añadir
    if accion == "A":
        print("Vamos a añadir un número de telefono:")
        print("-------------------------------------")
        nombre = input("Nombre: ")
        numero = input("Número: ")
        agenda[nombre] = numero

    # Accion consultar
    elif accion == "C":
        print("Consultar numero:")
        print("-------------------------------------")
        nombre = input("De quien quieres saber el numero:")
        print(agenda[nombre])

    # Accion salir
    elif accion == "S":
        salida = True


"""
Crea un programa que sea capaz de guardar los nombres de tus amigos y sus años de nacimiento

Crea un programa que al decirle el nombre de un color nos devuelva su traducción en inglés

Crea un programa que cuente el número de veces que aparece una palabra en una string

"Hola Hola como estas amigo amigo amigo"

Hola: 2 veces
como: 1 vez
estas: 1 vez
amigo: 3 veces


Crea una función que muestre por pantalla un texto y tantas barritas de subrayado como larga
sea la string.

mostrar_titulo_subrayado("Hola mundo")

Hola mundo
----------
"""