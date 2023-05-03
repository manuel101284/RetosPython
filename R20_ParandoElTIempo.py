"""
* Crea una función que sume 2 números y retorne su resultado pasados
* unos segundos.
* - Recibirá por parámetros los 2 números a sumar y los segundos que
*   debe tardar en finalizar su ejecución.
* - Si el lenguaje lo soporta, deberá retornar el resultado de forma
*   asíncrona, es decir, sin detener la ejecución del programa principal.
*   Se podría ejecutar varias veces al mismo tiempo.
"""
import time

def stop_the_time(num_1, num_2, time_1):
    result = num_1+ num_2

    time.sleep(time_1)
    print(result)


num_1 = 48
num_2 = 54
time_1 = 13

stop_the_time(num_1, num_2, time_1)

num_1 = 2
num_2 = 7
time_1 = 3

stop_the_time(num_1, num_2, time_1)
