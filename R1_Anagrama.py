"""
* Escribe una función que reciba dos palabras (String) y retorne
* verdadero o falso (Bool) según sean o no anagramas.
* - Un Anagrama consiste en formar una palabra reordenando TODAS
*   las letras de otra palabra inicial.
* - NO hace falta comprobar que ambas palabras existan.
* - Dos palabras exactamente iguales no son anagrama.
"""

print("Ingrese la primera palabra")
word_01 = input()
word_01 = word_01.upper()

print("Ingrese la segunda palabra")
word_02 = input()
word_02 = word_02.upper()

if (word_01 == word_02):
    print("Falso")
    print("No son anagramas")
else:
    list_word_01 = list(word_01)
    # print(list_word_01)

    list_word_02 = list(word_02)
    # print(list_word_02)
    counter = 0
    if (len(list_word_01) == len(list_word_02)):
        for i_01 in range(len(list_word_01)):
            for i_02 in range(len(list_word_02)):
                if (i_01 == i_02):
                    if (list_word_01[i_01] == list_word_02[i_02]):
                        counter += 1

        if (counter == len(list_word_01)):
            print("Verdadero")
            print("Si son anagramas")
        else:
            print("Falso")
            print("No son anagramas")
    else:
        print("Falso")
        print("No son anagramas")

