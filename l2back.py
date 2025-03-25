'''#Exercício 1
N1 = int(input("Insira um número: "))

if N1 % 2 == 0:
    print("Par")
else:
    print("Ímpar")'''
from time import strftime

'''#Exercício 2

N1 = int(input("Informe um número: "))

if N1 > 10:
    print(f"{N1} é maior que dez")
else:
    print(f"{N1} não é maior do que dez")'''

'''#Exercício 3
age = int(input("Informe a sua idade: "))

if age >=18:
    print("Maior de idade")
else:
    print("Menor de idade")'''

'''#Exercício 4
age = int(input("Informe a sua idade: "))

if age <16:
    print("Não eleitor")
elif age <= 17:
    print("Voto facultativo")
elif age <=69:
    print("Voto obrigatório")
else:
    print("Voto facultativo")'''

'''#Exercício 5
number = int(input("Insira um número: "))

if number <0:
    print("Número negativo")
elif number > 0:
    print("Número positivo")
else:
    print("Você inseriu o número 0")'''

'''#Exercício 6
nota = float(input("Informe a sua nota: "))

if nota >= 9:
    print("A")
elif nota >= 7:
    print("B")
elif nota >=5:
    print("C")
elif nota >=3:
    print("D")
else:
    print("E")'''

'''#Exercício 7 (adulto não tem desconto)

idade = int(input("Informe a sua idade: "))

if idade <=12:
    print("Eba! você tem direito a um desconto!")
elif idade <=59:
    print("Infelizmente você não tem direito a um desconto.")
else:
    print("Você tem direito a um desconto!")'''

'''#Exercício 8
lado1 = int(input("Informe o valor do primeiro lado: "))
lado2 = int(input("Informe o valor do segundo lado: "))
lado3 = int(input("Informe o valor do terceiro lado: "))

if lado1 + lado2 > lado3:
    print("É possível criar um triângulo!")
    if lado1 == lado2 == lado3:
        print("Você possui um triângulo equilátero!")
    elif lado1 != lado2 != lado3:
        print("Você possui um triângulo escaleno!")
    else:
        print("Você possui um triângulo isósceles!")
else:
    print("Não é possível criar um triângulo")
'''

'''#Exercício 9 ta dando negativo
valor = float(input("Insira o valor da compra: "))

if valor < 100:
    calc = valor*0.05 - (valor)
    print(calc)
elif valor <=500:
    calc = valor * 0.1 - (valor)
    print(calc)
else:
    calc= valor * 0.15 - (valor)
    print(calc)'''

'''#Exercício 10
ano = int(input("Insira um ano: "))

if ano % 4 == 0 and ano %100 !=0:
    print("O ano é bissexto")
elif ano %4 == 0 and ano %100 ==0 and ano %400 == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")'''

'''#Exercício 11
peso = float(input("Insira o seu peso: "))
altura = float (input("Insira a sua altura: "))
calc = peso / (altura*altura)

if calc < 18.5:
    print("Abaixo do peso")
elif calc <= 24.9:
    print("Peso normal")
elif calc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")'''

'''#Exercício 12
number1 = int(input("Informe o primeiro número: "))
number2 = int(input("Informe o segundo número: "))
number3 = int(input("Informe o terceiro número: "))

if number1 > number2 > number3:
    print("Os números estão em ordem decrescente")
elif number1 < number2 < number3:
    print("Os números estão em ordem crescente")
else:
    print("Os números são iguais")'''

'''#Exercício 13
temp = float(input("Informe a temperatura: "))

if temp < 10:
    print("Frio")
elif temp < 25:
    print("Aconchegante")
elif temp <= 40:
    print("Quente")
else:
    print("Muito quente")'''

'''#Exercício 14
dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))
data1 = (f"{ano:04d}/{mes:02d}/{dia:02d}")
print(data1)'''





#Desafio 19 (import re)  (r^\d{3}\.\d{3}\.\d{3}\.d{2}$)