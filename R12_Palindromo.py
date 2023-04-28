"""
* Escribe una función que reciba un texto y retorne verdadero o
* falso (Boolean) según sean o no palíndromos.
* Un Palíndromo es una palabra o expresión que es igual si se lee
* de izquierda a derecha que de derecha a izquierda.
* NO se tienen en cuenta los espacios, signos de puntuación y tildes.
* Ejemplo: Ana lleva al oso la avellana.
"""
def palindrome(text1):
    list1 = text1.lower()
    list1 = "".join(list1.split(" "))
    list1 = list(list1)
    list2 = list()
    for i in range(len(list1)):
        list2.append(list1[-(i + 1)])

    #print(list1)
    #print(list2)

    if (list1 == list2):
        print("True")
    else:
        print("False")

print("Ingrese una frase o palabra para saber si es palindromo")
text1 = input()
#text1 = "Anita Lava La Tina"
palindrome(text1)