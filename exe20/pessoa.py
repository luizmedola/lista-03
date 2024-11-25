class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def verificar_altura(self):
        if self.altura > 1.75:
            return f"{self.nome} é mais alto que 1,75 metros."
        else:
            return f"{self.nome} não é mais alto que 1,75 metros."
