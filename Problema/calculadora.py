from soma import Soma
from subtracao import Subtracao
from multiplicacao import Multiplicacao
from divisao import Divisao

class Calculadora:
    def __init__(self):
        self.soma = Soma()
        self.subtracao = Subtracao()
        self.multiplicacao = Multiplicacao()
        self.divisao = Divisao()

    def realizar_operacao(self, operacao, num1, num2):
        if operacao == 1:  
            return self.soma.calcular(num1, num2)
        elif operacao == 2: 
            return self.subtracao.calcular(num1, num2)
        elif operacao == 3:  
            return self.multiplicacao.calcular(num1, num2)
        elif operacao == 4:  
            return self.divisao.calcular(num1, num2)
        else:
            return "Operação inválida"
