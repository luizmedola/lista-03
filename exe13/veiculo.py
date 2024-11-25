class Veiculo:
    def __init__(self, modelo, velocidade_inicial=0):
        self.modelo = modelo
        self.velocidade = velocidade_inicial

    def aumentar_velocidade(self, incremento):
        if incremento > 0:
            self.velocidade += incremento
            print(f"A velocidade do {self.modelo} foi aumentada para {self.velocidade} km/h.")
        else:
            print("Incremento de velocidade deve ser maior que zero.")
    
    def exibir_detalhes(self):
        print(f"Modelo: {self.modelo}")
        print(f"Velocidade atual: {self.velocidade} km/h")
