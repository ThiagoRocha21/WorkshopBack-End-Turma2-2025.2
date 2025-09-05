import math


class FiguraGeometrica:
    @staticmethod
    def circunferencia():
        raio = float(input('Digite o raio: '))
        return math.pi * math.pow(raio, 2)

    @staticmethod
    def area_triangulo():
        base = float(input('Digite o base: '))
        altura = float(input('Digite altura: '))
        return base * altura / 2

    @staticmethod
    def hipotenusa():
        cateto1 = float(input('Digite o cateto 1: '))
        cateto2 = float(input('Digite o cateto 2: '))
        return math.pow(cateto1, 2) + math.pow(cateto2, 2)

while True:
    escolha = int(input('Escolha uma opção: \n 1 - calcular a circunferência \n'
                        ' 2 - Calcular a área de um triângulo \n'
                        ' 3 - Calcular a hipotenusa \n '
                        '4 - Sair'))
    if escolha == 1:
        print(FiguraGeometrica.circunferencia())
    elif escolha == 2:
        print(FiguraGeometrica.area_triangulo())
    elif escolha == 3:
        print(FiguraGeometrica.hipotenusa())
    elif escolha == 4:
        break
    else:
        print("Escolha uma alternativa válida.")

