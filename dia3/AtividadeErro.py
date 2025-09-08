#print("Olá, mundo!"

    #SyntaxError, falta um parênteses. Versão corrigida abaixo
print("Olá, mundo!")







#print(nome) 

    #NameError, falta definir a variável antes de usá-la. Versão corrigida abaixo
nome = "Thiago"
print(nome)








#def somar(a, b):
#   return a + b

#resultado = somar(10, "5")
#print(resultado)

    #TypeError, tentando somar tipos diferentes(Int + String)

def somar(a, b):
    return a + b

try:
    resultado = somar(10, 5)
    print(resultado)
except TypeError:
    print("Só é possível somar números inteiros (...-3, -2, -1, 0, 1, 2, 3...)")








#numeros = [10, 20, 30]
#indice = int(input("Digite um índice para acessar a lista: ")) 

#print(numeros[indice])
    
    #IndexError, Pode ser que o valor digitado seja maior que o número de indices da lista, 
    #tentando acessar um espaço que não existe.

numeros = [10, 20, 30]
while True:
    indice = int(input("Digite um número entre 0 e 2 para acessar a lista: ")) 
    try:
        print(numeros[indice])
        break
    except IndexError:
        print("Digite um número entre 0 e 2.")









#def dividir(a, b):
 #   return a / b

#num1 = input("Digite o primeiro número: ")
#num2 = input("Digite o segundo número: ")

#resultado = dividir(int(num1), int(num2))
#print(f"Resultado: {resultado}")

    #TypeError, ZeroDivisionError, ValueError. Pode dar esses erros porque a entrada pode ser
    # um 0 ou uma string. Além disso, é possível dar erro em "dividir(int(num1)...)", pois se o valor
    # for uma string, ele não irá passar para inteiro.
 
def dividir(a, b):
    return a / b
while True:    
    num1 = int(input("Digite o primeiro número (diferente de 0): "))
    num2 = int(input("Digite o segundo número (diferente de 0): "))
    try: 
        resultado = dividir(int(num1), int(num2))
        print(f"Resultado: {resultado}")
        break
    except ZeroDivisionError:
        print("Digite um número diferente de 0.")










#dados = {
 #   "nome": "Isaac ",
  #  "idade": 25,
   # "cidade": "São Paulo"
#}
#chave = input("Digite a chave que deseja acessar: ")
#print(f"O valor da chave '{chave}' é: {dados[chave]}")

    #KeyError,  pois ele pode procurar por uma chave que não exista.

dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

while True:
    try:    
        chave = str(input("Digite a chave que deseja acessar(Nome, idade ou cidade.): ")).lower()
        print(f"O valor da chave '{chave}' é: {dados.get(chave)}")
        break
    except KeyError:
        print("Digite uma das opções: nome, idade, cidade")
    








#def validar_idade(idade)
 #   if idade < 0 or idade > 120:
  #      raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
   # return f"Idade válida: {idade}"

#idade = int(input("Digite sua idade: "))
#print(validar_idade(idade))

def validar_idade(idade):
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
    return f"Idade válida: {idade}"

while True:
    try:
        idade = int(input("Digite sua idade: "))
        print(validar_idade(idade))
        break
    except:
        print("Digite uma idade válida.")










#def calcular_media(notas):
 #   soma = sum(notas)
  #  quantidade = len(notas)
   # return soma / quantidade

#notas = [8, 9, "10", 7]
#media = calcular_media(notas)
#print(f"Média: {media:.2f}")

def calcular_media(notas, quantidade):
    soma = sum(notas)
    quantidade = len(notas)
    return soma / quantidade

notas = []
try:
    quantidade_notas = int(input("Quantas notas você irá inserir? "))
except: 
    print("Digite um valor válido.")
i = 0
while i < quantidade_notas:
    try:
        nota_digitada = float(input(f"Digite a {i+1}ª nota."))
        notas.append(nota_digitada)
        i+=1
    except:
        print("Digite um valor válido.") 
        

while True:
    try:
        media = calcular_media(notas, quantidade_notas)
        print(f"Média: {media:.2f}")
        break
    except:
        print("...")