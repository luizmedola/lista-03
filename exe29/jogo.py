class Jogo:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
    
    def iniciar_jogo(self):
        print(f"Iniciando o jogo: {self.nome}")
        self.pontuacao = 0  
        print("Jogo iniciado! Boa sorte!")
    
    def registrar_pontuacao(self, pontos):
        if pontos < 0:
            print("A pontuação não pode ser negativa!")
        else:
            self.pontuacao += pontos
            print(f"Pontuação registrada: {pontos} pontos.")
    
    def exibir_pontuacao(self):
        print(f"A pontuação atual no jogo {self.nome} é: {self.pontuacao} pontos.")
