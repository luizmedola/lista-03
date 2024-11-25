class Animal:
    def __init__(self, nome, tipo_movimento):
        self.nome = nome
        self.tipo_movimento = tipo_movimento

    def mover(self):
        print(f"O {self.nome} {self.tipo_movimento}.")

