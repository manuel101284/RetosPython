"""
* Escribe una función que calcule y retorne el factorial de un número dado
* de forma recursiva.
"""

def recursive_fact(number):
    fact = 1
    if (number ==1 or number == 0):
        fact = 1
        print(fact)
    elif (number > 1):
        fact = number*recursive_fact(number - 1)
        print(fact)
    return fact

number = 6
recursive_fact(number)