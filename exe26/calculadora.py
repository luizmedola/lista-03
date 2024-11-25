class Calculadora:
    def __init__(self):
        self.historico = []  

    def soma(self, a, b):
        resultado = a + b
        self.historico.append(f"Soma: {a} + {b} = {resultado}")
        return resultado

    def subtracao(self, a, b):
        resultado = a - b
        self.historico.append(f"Subtração: {a} - {b} = {resultado}")
        return resultado

    def multiplicacao(self, a, b):
        resultado = a * b
        self.historico.append(f"Multiplicação: {a} * {b} = {resultado}")
        return resultado

    def divisao(self, a, b):
        if b == 0:
            self.historico.append(f"Divisão: {a} / {b} = Erro! Divisão por zero.")
            return "Erro! Divisão por zero."
        resultado = a / b
        self.historico.append(f"Divisão: {a} / {b} = {resultado}")
        return resultado

    def exibir_historico(self):
        if not self.historico:
            return "Nenhuma operação realizada."
        return "\n".join(self.historico)
