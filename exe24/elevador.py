class Elevador:
    def __init__(self, totalAndares):
        self.totalAndares = totalAndares 
        self.andarAtual = 0  

    def subir(self):
        if self.andarAtual < self.totalAndares:
            self.andarAtual += 1
            print(f"Subindo... Agora você está no andar {self.andarAtual}.")
        else:
            print("Você já está no último andar.")

    def descer(self):
        if self.andarAtual > 0:
            self.andarAtual -= 1
            print(f"Descendo... Agora você está no andar {self.andarAtual}.")
        else:
            print("Você já está no térreo.")

    def exibir_andar_atual(self):
        return f"Você está no andar {self.andarAtual}."
