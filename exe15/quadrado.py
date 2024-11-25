class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

    def exibir_detalhes(self):
        print(f"Lado do quadrado: {self.lado} unidades")
        print(f"Área do quadrado: {self.calcular_area()} unidades quadradas")
        print(f"Perímetro do quadrado: {self.calcular_perimetro()} unidades")
