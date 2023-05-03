"""
* Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
* que calcule el mínimo común múltiplo (mcm) de dos números enteros.
* - No se pueden utilizar operaciones del lenguaje que 
*   lo resuelvan directamente.
"""

def mcd(num_1, num_2):
    if (num_1 > num_2):
        controller =  num_2
        while (controller >= 1):
            if((num_1 % controller) == 0 and (num_2 % controller) == 0):
                print(f"mcd: {controller}")
                controller = 0
            controller -= 1
    if (num_1 < num_2):
        controller =  num_1
        while (controller >= 1):
            if((num_1 % controller) == 0 and (num_2 % controller) == 0):
                print(f"mcd: {controller}")
                controller = 0
            controller -= 1
    if(num_1 == num_2):
        print(f"mcd: {num_1}")

def mcm(num_1, num_2):
    opc = False
    if (num_1 > num_2):
        controller =  num_1
        while (opc == False):
            if((controller % num_1) == 0 and (controller % num_2) == 0):
                print(f"mcm: {controller}")
                opc = True
            controller += 1
    if (num_1 < num_2):
        controller =  num_2
        while (opc == False):
            if((controller % num_1) == 0 and (controller % num_2) == 0):
                print(f"mcm: {controller}")
                opc = True
            controller += 1
    if(num_1 == num_2):
        print(f"mcm: {num_1}")

num_1 = 12
num_2 = 60

mcd(num_1, num_2)
mcm(num_1, num_2)