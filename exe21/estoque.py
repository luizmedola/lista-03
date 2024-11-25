class Livro:
    def __init__(self, titulo, autor, estoque):
        self.titulo = titulo
        self.autor = autor
        self.estoque = estoque

    def exibir_detalhes(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nEstoque: {self.estoque} unidades"

    def atualizar_estoque(self, quantidade):
        self.estoque += quantidade
        if self.estoque < 0:
            self.estoque = 0  
