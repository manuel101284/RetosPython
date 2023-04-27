"""
* Crea una única función (importante que sólo sea una) que sea capaz
* de calcular y retornar el área de un polígono.
* - La función recibirá por parámetro sólo UN polígono a la vez.
* - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
* - Imprime el cálculo del área de un polígono de cada tipo.
"""

def poligon_area(poligon):
    
    if(poligon == "triangulo" or poligon == "cuadrado" or poligon == "rectangulo"):
        if (poligon == "triangulo"):
            print("Ingrese el valor de la base")
            value1 = int(input())
            print("Ingrese el valor de la altura")
            value2 = int(input())
            area = (value1*value2)/2
            
        elif (poligon == "cuadrado"):
            print("Ingrese el valor del lado")
            value1 = int(input())
            area = (value1*value1)
            
        elif (poligon == "rectangulo"):
            print("Ingrese el valor del alto")
            value1 = int(input())
            print("ingrese el valor del ancho")
            value2 = int(input())
            area = (value1*value2)
        print(f"El área del polígono {poligon} es {area}")

    else:
        print("Palabra o tipo de polígono NO válido")
        
    

print("Este código calcula el area de un triangulo, cuadrado o rectangulo")
print("Digite triangulo o cuadrado o rectangulo, según sea el caso")
poligon = input()
poligon_area(poligon)

