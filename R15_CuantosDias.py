"""
* Crea una función que calcule y retorne cuántos días hay entre dos cadenas
* de texto que representen fechas.
* - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
* - La función recibirá dos String y retornará un Int.
* - La diferencia en días será absoluta (no importa el orden de las fechas).
* - Si una de las dos cadenas de texto no representa una fecha correcta se
*   lanzará una excepción.
"""
import datetime

def how_many_days(date_01, date_02):
    list_01 = date_01.split("/")
    list_02 = date_02.split("/")

    print(list_01)
    print(list_02)

    date_old = datetime.date(int(list_01[2]), int(list_01[1]), int(list_01[0]))
    date_new = datetime.date(int(list_02[2]), int(list_02[1]), int(list_02[0]))

    print(date_new - date_old)
    print(date_old - date_new)

date_01 = "02/03/2000"
date_02 = "06/01/2022"

how_many_days(date_01, date_02)


