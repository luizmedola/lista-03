import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
