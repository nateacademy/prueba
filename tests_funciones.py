
def reverse_string(string_to_reverse):
    string_reversed = ""
    current_index = len(string_to_reverse) - 1
    while current_index >= 0:
        string_reversed += string_to_reverse[current_index]
        current_index -= 1
    return string_reversed


print(reverse_string("Hola"))
print(reverse_string("Caracola"))
print(reverse_string("Cocacola"))
print(reverse_string("Me llamo dave"))
print(reverse_string("Tengo 100 años"))
print(reverse_string("Me duele la cadera"))
print(reverse_string("Tengo 80 hijos"))
print(reverse_string("Me apetece un té"))

""""
1 - Escribe un programa que encuentre el numero más grande entre 3 numeros:
2 - Escribe una funcion que dado un numero y un rango (otros dos numeros),
     compruebe que ese numero está entre los dos (dentro del rango)
numero_en_rango(101, 1, 100) -> False
numero_en_rango(10, 1, 100) -> True
3 - Escribe una funcion que reciba una lista de numeros y te devuelva otra pero solo con los pares
devolver_pares([1, 2, 3, 4, 5, 6])
[2, 4, 6]
"""
