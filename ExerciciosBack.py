
#Exercício 1
Nome= "João"
print(Nome)


#Exercício 2
N1 = 10
N2 = 5
Soma = N1 + N2
Subtracao = N1 - N2
Multiplicacao = N1 * N2
Divisao = N1 // N2
print(f"Resultado da soma: {Soma}, Resultado da subtração: {Subtracao}, Resultado da multiplicação: {Multiplicacao}, Resultado da divisão: {Divisao}")


#Exercício 3
Preco = 50
Desconto = 10
Calculo = Preco - Desconto
print(f"Preço com desconto aplicado: {Calculo}")

#Exercício 4
Resultado = 10 + 5 * 2
print(Resultado)

#Exercício 5
numero = "150"
print(int(numero)*2)

#Exercicio 6 - Prof mandou pular

#Exercício 7
N1 = int(input("Insira o primeiro valor: "))
N2 = int(input("Insira o segundo valor: "))
Soma = N1 + N2
print(Soma)

#Exercício 8
Valor1 = int(input("Insira um valor: "))
Valor2 = int(input("Insira outro valor: "))
Conta = Valor1 // Valor2
print(Conta)

#Exercício 9
Num1 = int(input("Insira um número: "))
Num2 = int(input("Insira outro número: "))
N = Num1 > Num2
print(N)

#Exercício 10
Idade = int(input("Insira a sua idade: "))
Dias = Idade * 365
print(Dias)

#Exercicio 11
Base = int(input("Insira o valor da sua base: "))
Expoente = int(input("Insira o valor do seu expoente: "))
Calc = Base ** Expoente
print(Calc)

#Exercicio 12
preco= int(input("Digite o valor: "))
print("O preço é R$:" +str(preco))

#Exercicio 13
Raio = int(input("Informe o valor do raio: "))
Calc = (Raio**2)*3,14
print(Calc)

#Exercicio 14
Var1 = int(input("Insira o primeiro valor: "))
Var2 = int(input("Insira o segundo valor: "))

print(Var1, Var2)

Var1, Var2 = Var2, Var1
print(Var1, Var2)

#Exercicio 15
Nota1 = float(input("Insira a primeira nota: "))
Nota2 = float(input("Insira a segunda nota: "))
Nota3 = float(input("Insira a terceira nota: "))
Peso1 = 2
Peso2 = 3
Peso3 = 5

Soma = (Nota1 * Peso1 + Nota2 * Peso2 + Nota3 * Peso3) / (Peso1 + Peso2 + Peso3)
print(Soma)

#Exercicio 16

import math
x1= int(input("Insira a primeira coordenada X: "))
y1= int(input("Insira a primeira coordenada Y: "))
x2= int(input("Insira a segunda coordenada X: "))
y2= int(input("Insira a segunda coordenada Y: "))

distancia = math.sqrt((x2 - x1) **2 + (y2-y1)**2 **0.5)

print(f"Sua Distância é: {distancia}")