"""
* Crea un programa que sea capaz de transformar texto natural a código
* morse y viceversa.
* - Debe detectar automáticamente de qué tipo se trata y realizar
*   la conversión.
* - En morse se soporta raya "—", punto ".", un espacio " " entre letras
*   o símbolos y dos espacios entre palabras "  ".
* - El alfabeto morse soportado será el mostrado en
*   https://es.wikipedia.org/wiki/Código_morse.
"""

def convert_text(text_to_convert):
    dict_01 = {
        "A": ".—", "B": "—...", "C": "—.—.", "CH": "————", "D": "—..",
        "E": ".", "F": "..—.", "G": "——.", "H": "....", "I": "..",
        "J": ".———", "K": "—.—", "L": ".—..", "M": "——", "N": "—.",
        "Ñ": "——.——", "O": "———", "P": ".——.", "Q": "——.—", "R": ".—.",
        "S": "...", "T": "—", "U": "..—", "V": "...—", "W": ".——",
        "X": "—..—", "Y": "—.——", "Z": "——..", "0": "—————", "1": ".————",
        "2": "..———", "3": "...——", "4": "....—", "5": ".....", "6": "—....",
        "7": "——...", "8": "———..", "9": "————.", ".": ".—.—.—", ",": "——..——",
        "?": "..——..", "\"": ".—..—.", "/": "—..—."
    }

print("Ingrese el texto para convertirlo")
text_to_convert = input()

convert_text(text_to_convert)

# ESTA EN PROCESO