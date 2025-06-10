class itemBiblioteca:
    def __init__(self, titulo:str, disponivel:bool, ano_publicacao:int = 1):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel == True:
            print("Item disponível")
        else:
            print("O livro já está emprestado")

    def devolver(self):
        if self.disponivel == False:
            print("Livro disponível novamente")
        else:
            print("Livro disponível")

    def obter_info(self):
        print(f"Titulo: {self.titulo}\nAno:{self.ano_publicacao}\nDisponível:{self.disponivel}")

class colecaoLivro(itemBiblioteca):
    def __init__(self, titulo, disponivel, ano_publicacao):
        super().__init__(titulo, disponivel, ano_publicacao)
        self.colecao = []

    def adicionar_livro(self, livro:itemBiblioteca):
        self.colecao.append(livro)

    def verificar_disponibilidade(self):
        for livro in self.colecao:
            if not livro.disponivel:
                print(f"Coleção não está disponível")
                return False
        print(f"Coleção está disponível")
        return True


colecao = colecaoLivro("Coleção1", True, 2010)
livro1 = itemBiblioteca("Trono", True, 2018)
colecao.adicionar_livro(livro1)
colecao.adicionar_livro(itemBiblioteca("Principe", True, 2018))
colecao.adicionar_livro(itemBiblioteca("Corte", True, 2019))

colecao.verificar_disponibilidade()