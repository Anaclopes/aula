class Personagem:  # Definimos a classe Personagem
    def __init__(self, nome, vida):  # metodo construtor __init__ e atribuímos os    parametros nome e vida
        self.nome = nome
        self.vida = vida


class Heroi(Personagem):  # Herói herda de Personagem
    def __init__(self, nome, vida, habilidade):
        super().__init__(nome, vida)  # Chamando o construtor da classe mãe
        self.habilidade = habilidade


heroi1 = Heroi("Superman", 100, "Voo")  # Criando um herói
heroi2 = Heroi("Homem de Ferro", 200, "Morrer")
print(heroi1.nome)  # Saída: Superman
print(heroi1.vida)  # Saída: 100
print(heroi1.habilidade)  # Saída: Voo

#A partir daqui, começa o exemplo de polimorfismo
class Personagem:
  def __init__(self, nome, vida):
      self.nome = nome
      self.vida = vida


  class Heroi(Personagem):
      def __init__(self, nome, vida, habilidade):
          super().__init__(nome, vida)
          self.habilidade = habilidade


  class Vilao(Personagem):  # Adicionando a classe Vilão
      def __init__(self, nome, vida, poder):
          super().__init__(nome, vida)
          self.poder = poder


  def atacar(personagem):  # Função para atacar, pode ser chamada por heróis ou vilões
      print(f"{personagem.nome} está atacando!")


  heroi1 = Heroi("Superman", 100, "Voo")
  vilao1 = Vilao("Lex Luthor", 80, "Inteligência")


  atacar(heroi1)  # Chamando a função atacar() com um herói
  atacar(vilao1)  # Chamando a função atacar() com um vilão