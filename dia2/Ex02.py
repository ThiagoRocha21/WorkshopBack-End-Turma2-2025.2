import math

def calculo_arredondado(numero, arredondado):
    calculo = arredondado - numero
    if calculo >= 0.5:
        resultado = math.floor(numero)
        return resultado
    elif calculo < 0.5:
        resultado = math.ceil(numero)
        return resultado


numero_digitado = float(input("Digite um número real: "))
numero_arredondado = math.ceil(numero_digitado)
print (calculo_arredondado(numero_digitado, numero_arredondado))
