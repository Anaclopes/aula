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

'''#Exercício 15

import re
#Trabalha com expressões regulares (regex)

senha = input("Informe a senha desejada: ")

carac = len(senha) >=8
Mai = bool(re.search (r'[A-Z]', senha))
minu = bool(re.search (r'[a-z]', senha))
num = bool(re.search (r'[0-9]', senha))
caraces = bool(re.search (r'[@#$%&]', senha))

if (carac and Mai and minu and num and caraces) == True:
    print("Senha válida")
elif Mai == False:
    print("A senha precisa conter ao menos uma letra maiúscula!")
elif minu == False:
    print("A senha precisa conter ao menos uma letra minúscula!")
elif num == False:
    print("A senha precisa conter ao menos um número!")
elif caraces == False:
    print("A senha precisa conter ao menos um caractere especial (@, #, $, %, &)")
else:
    print("A senha precisa conter pelo menos 8 caracteres.")
'''

'''#Exercício 16
import math
num = int(input("Insira o número que deseja calcular: "))

if num < 0:
    print("Não é possível calcular a raiz de um número negativo!")
elif num > 100:
    print("Número muito grande, reduza para um valor abaixo de 100.")
else:
    raiz = math.sqrt(num)
    print(f"{raiz:.2f}")'''

'''#Exercíci 17

data = input("Informe uma data no formato dd/mm/aaaa: ")
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dtv = dia >= 1 and dia <=30
elif mes == 3 or mes == 5 or mes == 6 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dtv = dia >= 1 and dia <=31
    if ano %4 == 0 or (ano %100 ==0 and ano %400 ==0):
        dtv = dia >=1 and dia <=29
    else: 
        dtv = dia >=1 and dia<=28
else: 
    dtv = False

if dtv == True:
    print(f"{ano}/{mes:02d}/{dia:02d}")
else:
    print("Data inválida")'''

'''#Exercício 18

func = input("Insira uma função matemática: ")
print(func)
 #eval analisa expressões dentro de string

print(eval(func))'''


#Desafio 19 (import re)
import re
cpf = list(input("Insira o seu cpf: "))
cpf_r = r"^\d{3}\.\d{3}\.\d{3}\.d{2}$"
cpf = re.sub("[.]","", cpf)
cpf = re.sub("-","", cpf)

pv_one = int(cpf[0])*10
pv_two = int(cpf[1])*9
pv_three = int(cpf[2])*8
pv_four = int(cpf[4])*7
pv_five = int(cpf[5])*6
pv_six = int(cpf[6])*5
pv_seven = int(cpf[8])*4
pv_eight = int(cpf[9])*3
pv_nine = int(cpf[10])*2
pv_ten = int(cpf[12])
pv_eleven = int(cpf[13])
somapv = (pv_one + pv_two + pv_three + pv_four + pv_five + pv_six + pv_seven + pv_eight + pv_nine) / 11
restopv = somapv % 11

if  len(cpf) == 11:
    spv = (pv_one*10) + (pv_two*9) + (pv_three*8) + (pv_four*7) + (pv_five*6) + (pv_six*5) + (pv_seven*4) + (pv_eight*3) + (pv_nine*2)
    dspv = spv % 11
    if dspv < 2:
        edp = pv_ten == 0
    else:
        edp = pv_ten == 11-dspv
    ssv = (pv_one*11) + (pv_two*10) + (pv_three*9) + (pv_four*8) + (pv_five*7) + (pv_six*6) + (pv_seven*5) + (pv_eight*4) + (pv_nine*3) + (pv_ten*2)
    dspv = ssv % 11
    if dspv < 2:
        eds = pv_eleven == 0
    else:
        eds = pv_eleven == 11 - dspv

    if edp == False or eds == False:
        print("CPF Inválido!")
    else:
        print("CPF Válido!")
else:
    print("CPF Inválido!")