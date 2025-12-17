from geometria import Rectangulo, Triangulo, Circulo
figuras = [
        Rectangulo(base=5, altura=3),
        Triangulo(lado1=3, lado2=4, lado3=5, base=4, altura=3),
        Circulo(radio=4)
]

print("=" * 35)
print("CÁLCULO DE ÁREAS Y PERÍMETROS")
print("=" * 35) 
for figura in figuras:
    figura.mostrar_datos()
    figura.mostrar_longitudes()