class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_aumento(self, percentual):
        aumento = (self.salario * percentual) / 100
        self.salario += aumento
        return aumento

    def exibir_informacoes(self):
        return f"Nome: {self.nome}\nSalário: R${self.salario:.2f}"
