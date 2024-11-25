class Pessoa:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def classificacao_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade grau 1"
        elif 35 <= imc < 39.9:
            return "Obesidade grau 2"
        else:
            return "Obesidade grau 3"

    def exibir_informacoes(self):
        imc = self.calcular_imc()
        classificacao = self.classificacao_imc()
        return (f"Peso: {self.peso} kg\nAltura: {self.altura} m\nIMC: {imc:.2f}\nClassificação: {classificacao}")
