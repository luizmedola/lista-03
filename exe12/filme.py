class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Duração: {self.duracao} minutos")
