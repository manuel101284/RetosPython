"""
* Crea una función que reciba dos cadenas como parámetro (str1, str2)
* e imprima otras dos cadenas como salida (out1, out2).
* - out1 contendrá todos los caracteres presentes en la str1 pero NO
*   estén presentes en str2.
* - out2 contendrá todos los caracteres presentes en la str2 pero NO
*   estén presentes en str1.
"""

def delete_characters(str1, str2):
    list_1 = list(str1.lower())
    list_2 = list(str2.lower())

    set_1 = set(list_1)
    set_2 = set(list_2)

    out1 = set_1.difference(set_2)
    out2 = set_2.difference(set_1) 

    print(out1)
    print(out2)

print("Ingrese la primera cadena")
str1 = input()
print("Ingrese la segunda cadena")
str2 = input()

delete_characters(str1, str2)