class Eletrodomestico:
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
        self.ligado = False 

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.nome} foi ligado com potência de {self.potencia} watts.")
        else:
            print(f"{self.nome} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"{self.nome} foi desligado.")
        else:
            print(f"{self.nome} já está desligado.")
    
    def exibir_detalhes(self):
        status = "ligado" if self.ligado else "desligado"
        print(f"{self.nome} - Potência: {self.potencia} watts - Status: {status}")
