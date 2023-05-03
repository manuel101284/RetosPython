"""
* Crea una función que reciba días, horas, minutos y segundos (como enteros)
* y retorne su resultado en milisegundos.
"""

def convert_time(days_01, hours_01, minutes_01, seconds_01):
    total_time = seconds_01*1000 + minutes_01*60000 + hours_01*3600000 + days_01*86400000
    print(f"Tiempo en Milisegundo:{total_time}")

days_01 = 8
hours_01 = 15
minutes_01 = 55
seconds_01 = 17


convert_time(days_01, hours_01, minutes_01, seconds_01)