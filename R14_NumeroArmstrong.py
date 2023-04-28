"""
* Escribe una función que calcule si un número dado es un número de Armstrong
* (o también llamado narcisista).
* Si no conoces qué es un número de Armstrong, debes buscar información 
* al respecto.
"""

def armstrong_number(number):
    length = len(str(number))
    list_num = list(str(number))

    arms_num = 0 

    for i in range(len(list_num)):
        arms_num += int(list_num[i])**length
    
    if (number == arms_num):
        print(f"{number} ES número de Armstrong")
    else:
        print(f"{number} NO es número de Armstrong")
    
number = 4150

armstrong_number(number)