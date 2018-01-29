"""
Dada una lista de enteros:
Vamos a sustituir los multiplos de 3 por un Fizz
Y los multiplos de 5 sustituir por un Buzz
multiplos de 3 y de 5, vamos a sustituirlos por un FizzBuzz
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 20, 15, 30, 60, 70]

for indice in range(len(numeros)):
    if numeros[indice] % 3 == 0 or numeros[indice] % 5 == 0:
        valor_a_sustituir = ""
        if numeros[indice] % 3 == 0:
            valor_a_sustituir += "Fizz"

        if numeros[indice] % 5 == 0:
            valor_a_sustituir += "Buzz"

        numeros[indice] = valor_a_sustituir

print(numeros)
