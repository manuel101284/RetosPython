"""
* Crea un programa que cuente cuantas veces se repite cada palabra
* y que muestre el recuento final de todas ellas.
* - Los signos de puntuación no forman parte de la palabra.
* - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
* - No se pueden utilizar funciones propias del lenguaje que
*   lo resuelvan automáticamente.
"""
print("Ingrese el texto que desee para contar palabras")
text_01 = input()
text_02 = text_01.lower()

text_02 = "".join(text_01.split(","))
text_02 = "".join(text_02.split("."))
text_02 = "".join(text_02.split(":"))
text_02 = "".join(text_02.split(";"))
text_02 = "".join(text_02.split("..."))
list_01 = text_02.split(" ")
set_01 = set(list_01)

print(list_01)
print(set_01)

for element in set_01:
    xtimes = list_01.count(element)
    print(f"{element}: {xtimes} veces")
