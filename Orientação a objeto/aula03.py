class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá \n Meu nome é {self.nome} e tenho {self.idade} anos")

    #chamar a função em string
    def __str__(self):
        return f"{self.nome}"

    #compara uma pessoa com outra ou uma pessoa com outro objeto
    def __eq__(self, other):  #Exemplo: If pessoa1 == Pessoa2 (o Pessoa2 é o other)
        if isinstance(other,Pessoa): #conferindo se o other é uma pessoa
            if self.nome == other.nome and self.idade == other.idade:
                return True
        return False


    #maior ou igual = __ge__

    #Maior = __gt__

    #menor ou igual __le__
    #menor que = __lt__

    #diz o tamanho de algo
    def __len__(self):
        return self.idade

    #transforma em um dicionário
    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade
        }

pessoa1 = Pessoa("Fernanda Scanacapra", 35)
pessoa1.apresentar()

pessoa2 = Pessoa("Fernanda Batistão", 35)

if pessoa1 == pessoa2:
    print("São iguais")
else:
    print("Não são iguais")


dicionario = pessoa1.to_dict()
print(dicionario)

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super(). __init__(nome, idade) #usa sempre que a classe for herdar algo de outra classe
        self.cargo = cargo
    def apresentar(self):
        super(). apresentar() #chamando o apresentar do pai antes do dele
        print(f"Olá, eu sou {self.nome}, tenho {self.idade} anos e sou {self.cargo}")


funcionario = Funcionario("ABC", 25, "Aprendiz")
funcionario.apresentar()

#por herdar de pessoa, o funcionario também é uma pessoa
lista_pessoas = [pessoa1, pessoa2, funcionario]

for pessoa in lista_pessoas:
    pessoa.apresentar()

#Encapsulamento

print(funcionario.nome)
funcionario.nome = "DEF"
print(funcionario.nome)

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular #Isso é um atributo público
        self.__saldo = saldo #Isso é um atributo privado
#O atributo privado não permite que o usuário veja a informação e nem a altere
    # Outra forma de acessar um atributo privado
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")  # lança erro de valor
        self.__saldo = valor

'''    #permite acessar o saldo
    def get_saldo(self):
        return self.__saldo

    #permite alterar o valor
    def set_saldo(self, valor):
        if valor < 0:
            raise  ValueError ("Saldo não pode ser negativo")#lança erro de valor
        self.__saldo = valor'''

minha_conta = ContaBancaria("Ana", 60000)
print(minha_conta.titular)
minha_conta.saldo = 500
print(minha_conta.saldo)

#Abstração

#Molde para criar classe

from abc import  ABC, abstractmethod #trabalha com a parte de abstração

class Pagamento(ABC):
    @abstractmethod
    def autorizar(self, valor):
        pass

    @abstractmethod
    def estornar(self,valor):
        pass

class Pix(Pagamento):
    def autorizar(self, valor):
        print(f"Transferindo R${valor} via Pix")
    def estornar(self,valor):
        print(f"Devolvendo R$ {valor} via Pix")

Pix().autorizar(2000)