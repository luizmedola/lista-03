class Carro:
    def __init__(self, marca, combustivel_inicial=0):
        self.marca = marca
        self.combustivel = combustivel_inicial
    
    def abastecer(self, quantidade):
        if quantidade <= 0:
            print("A quantidade de combustível deve ser maior que zero.")
        else:
            self.combustivel += quantidade
            print(f"Você abasteceu {quantidade} litros de combustível.")
    
    def verificar_combustivel(self):
        print(f"O nível de combustível do carro {self.marca} é: {self.combustivel} litros.")
