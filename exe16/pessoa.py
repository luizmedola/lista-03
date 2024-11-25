class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self, outra_pessoa):
        print(f"Olá, {outra_pessoa.nome}!")
