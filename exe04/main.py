from livro import Livro

def main():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")

    livro = Livro(titulo, autor)
    
    livro.exibir_detalhes()

if __name__ == "__main__":
    main()
