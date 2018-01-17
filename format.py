"""
Programa un código que utilizando el método replace de las strings me sustituya las claves de mi string incial
por los valores en orden de una lista.
"""

valores_a_sustituir = [1, 2, "hola", "adios", 3]
string_a_cambiar = "Hola {}, numero {}, numero {}, {} y {}"

for valor in valores_a_sustituir:
    string_a_cambiar = string_a_cambiar.replace("{}", str(valor), 1)

print(string_a_cambiar)
