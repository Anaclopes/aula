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

class revista(itemBiblioteca):
    def __init__(self, titulo,disponivel,ano_publicacao, edicao):
        super().__init__(titulo,disponivel,ano_publicacao)
        self.edicao = edicao

    def atualizar_edicao(self):
        if self.edicao > 0:
            nova_edicao = int(input("Insira o número atualizado da edição: "))
            if self.edicao > nova_edicao:
                print("Não é possível retroceder a edição")
            else:
                self.edicao = nova_edicao
                print(f"Edição alterada para: {self.edicao}")
        else:
            print("Nenhuma edição registrada")

    def restringir_emprestimo(self, dias_max: int = 7):
        dias = int(input("Insira por quantos dias deseja emprestar: "))
        if self.ano_publicacao < 2000:
            if dias > dias_max:
                print("Não é possível emprestar a revista por todo esse tempo.")
            else:
                print("Empréstimo concluído")

    def obter_info(self):
        print(f"Titulo: {self.titulo}\nAno:{self.ano_publicacao}\nDisponível:{self.disponivel}, Edição: {self.edicao}")


livro2 = revista("Colegial", True, 1999, 9)
livro2.obter_info()
livro2.atualizar_edicao()
livro2.restringir_emprestimo()

'''colecao = colecaoLivro("Coleção1", True, 2010)
livro1 = itemBiblioteca("Trono", True, 2018)
livro1.obter_info()
colecao.adicionar_livro(livro1)
colecao.adicionar_livro(itemBiblioteca("Principe", True, 2018))
colecao.adicionar_livro(itemBiblioteca("Corte", True, 2019))

colecao.verificar_disponibilidade()'''