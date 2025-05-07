'''#Exercício1
for produtos in range (1):
    produtoA = 5 * 3
    produtoB = 8 * 3
    produtoC = 12 * 3

print(f"ProdutoA = R$ {produtoA}")
print(f"ProdutoB = R$ {produtoB}")
print(f"ProdutoC = R$ {produtoC}")'''
from statistics import median

'''#Exercício2

print("-----------------SEJA BEM VINDO(A)-----------------")
print("\nOlá,João!\n\t Seja muito bem vindo(a) ao nosso curso online!\n")

print("-----------------SEJA BEM VINDO(A)-----------------")
print("\nOlá,Maria!\n\t Seja muito bem vindo(a) ao nosso curso online!\n")

print("-----------------SEJA BEM VINDO(A)-----------------")
print("\nOlá,Carlos!\n\t Seja muito bem vindo(a) ao nosso curso online!\n")'''

'''#Exercício 3
import random
numeros = [4,7,10]

escolha = random.choice(numeros)

print(f"Número sorteado: {escolha}")
if escolha % 2 == 0:
    print("Você avançou um passo")
else:
    print("Você recuou um passo")'''

'''#Exercício 4

for numero in range(11):
    calculo = 2 * numero
    print(f"2 x {numero} = {calculo} ")

for numero in range(11):
    calculo = 3 * numero
    print(f"3 x {numero} = {calculo}")

for numero in range(11):
    calculo = 4 * numero
    print(f"4 x {numero} = {calculo} ")'''

'''#Exercício 5
cliente1 = 15
cliente2 = 20
cliente3 = 8

if cliente1 < 18:
    print("cliente1 não pode assistir ao filme pois é menor de 18")
else:
    print("cliente1 pode assistir ao filme")

if cliente2 < 18:
    print("cliente2 não pode assistir ao filme pois é menor de 18")
else:
    print("cliente2 pode assistir ao filme")

if cliente3 < 18:
    print("cliente3 não pode assistir ao filme pois é menor de 18")
else:
    print("cliente3 pode assistir ao filme")'''

'''#Exercício 6

produto1 = 50
produto2 = 120
produto3 = 200

calc1 = produto1 - (produto1 * 0.1)
print(f"Preço final do primeiro produto é: R$ {calc1}")

calc2 = produto2 - (produto2 * 0.1)
print(f"Preço final do segundo produto é: R$ {calc2}")

calc3 = produto3 - (produto3 * 0.1)
print(f"Preço final do terceiro produto é: R$ {calc3}")'''

'''#Exercício7
palavra1 = "Casa"
palavra2 = "Paralelepípedo"
palavra3 = "Python"

print(f"A palavra Casa tem: {len(palavra1)} letras")
print(f"A palavra Paralelepípedo tem: {len(palavra2)} letras")
print(f"A palavra Python tem: {len(palavra3)} letras")'''

'''#Exercício 8

temperatura1 = 30
temperatura2 = 100
temperatura3 = 0

calculo1 = (30*9/5) + 32
print(f"{temperatura1}ºC em Fahrenheit: {calculo1}ºF")

calculo2 = (100*9/5) + 32
print(f"{temperatura2}ºC em Fahrenheit: {calculo2}ºF")

calculo3 = (0*9/5) + 32
print(f"{temperatura3}ºC em Fahrenheit: {calculo3}ºF")'''

'''#Exercício9

numero1 = 3
numero2 = 9
numero3 = 12
media = (numero1 + numero2 + numero3) / 3

if numero1 < media:
    print(f"{numero1} - Pequeno")
elif numero1 == media:
    print(f"{numero1} - Médio")
else:
    print(f"{numero1} - Grande")

if numero2 < media:
    print(f"{numero2} - Pequeno")
elif numero2 == media:
    print(f"{numero2} - Médio")
else:
    print(f"{numero2} - Grande")

if numero3 < media:
    print(f"{numero3} - Pequeno")
elif numero3 == media:
    print(f"{numero3} - Médio")
else:
    print(f"{numero3} - Grande")'''

#Exercício 10
palavra1 = "Ana".lower().replace(" ", "")
palavra2 = "1DSTB-SENAI".lower().replace(" ", "")
palavra3 = "Subi no Onibus".lower().replace(" ", "")

print(palavra3)
p1 = palavra1[::-1]
p2 = palavra2[::-1]
p3 = palavra3[::-1]

if palavra1 == p1:
    print("As palavras são palíndromos")
else:
    print("As palavras não são palíndromos")

if palavra2 == p2:
    print("As palavras são palíndromos")
else:
    print("As palavras não são palíndromos")

if palavra3 == p3:
    print("As palavras são palíndromos")
else:
    print("As palavras não são palíndromos")

'''#Exercício 11
numero = int(input("Informe um número: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(fatorial)'''