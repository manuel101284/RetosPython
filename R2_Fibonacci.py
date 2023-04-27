"""
* Escribe un programa que imprima los 50 primeros números de la sucesión
* de Fibonacci empezando en 0.
* - La serie Fibonacci se compone por una sucesión de números en
*   la que el siguiente siempre es la suma de los dos anteriores.
*   0, 1, 1, 2, 3, 5, 8, 13...
"""

counter = 3
num_previous = 0
num_next = 1

print(f"Número de Fibonacci 1 {num_previous}")
print(f"Número de Fibonacci 2 {num_next}")

while (counter <=50):
    num_fib = num_previous + num_next
    print(f"Número de Fibonacci {counter}: {num_fib}")
    num_previous = num_next
    num_next = num_fib
    counter += 1