"""
* Escribe un programa que se encargue de comprobar si un número es o no primo.
* Hecho esto, imprime los números primos entre 1 y 100.
"""

prime_number = 2

while (prime_number <=100):
    counter = 1
    divisors = 0
    while (counter <= prime_number):
        if ((prime_number % counter) == 0):
            divisors += 1
        counter += 1
    
    if divisors == 2:
        print(prime_number, "SI es Primo")
    #else:
        #print(prime_number, "NO es primo")
    
    prime_number += 1