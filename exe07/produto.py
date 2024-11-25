class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual_desconto):
        desconto = (percentual_desconto / 100) * self.preco
        self.preco -= desconto
        return self.preco
