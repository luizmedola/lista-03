class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")