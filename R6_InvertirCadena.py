"""
* Crea un programa que invierta el orden de una cadena de texto
* sin usar funciones propias del lenguaje que lo hagan de forma automática.
* - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

print("Ingrese una letra, caracter, palabra o frase")
variable_01 = input()

string_list = list(variable_01)
inverse_list = string_list.copy()

for i in range(len(string_list)):
    inverse_list[i] = string_list[-(i+1)]

#print(inverse_list)
print("".join(inverse_list))