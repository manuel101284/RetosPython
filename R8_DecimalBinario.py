"""
* Crea un programa se encargue de transformar un número
* decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""
print("Ingrese un número entero positivo para transformarlo a binario")
num_dec = int(input())

if (num_dec < 0):
    print("el númerp no es válido")
else:
    if (num_dec == 0 ):
        print(f"{num_dec} --> {0}")
    elif (num_dec == 1):
        print(f"{num_dec} --> {1}")
    else:
        remainder = 0
        num_bin = 0
        quotient = num_dec
        counter = 0
        while (quotient >= 2):
            remainder = quotient % 2
            quotient = int(quotient // 2)
            num_bin += remainder*(10**counter)
            counter += 1
            if (quotient < 2):
                num_bin += quotient*(10**counter)
        print(f"{num_dec} --> {num_bin}")    
    