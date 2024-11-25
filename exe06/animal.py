class Animal:
    def __init__(self, especie, som):
        self.especie = especie
        self.som = som

    def fazer_som(self):
        print(f"O som do {self.especie} é: {self.som}")
