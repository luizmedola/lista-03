from filme import Filme

def main():
    titulo = input("Digite o título do filme: ")
    duracao = int(input("Digite a duração do filme em minutos: "))
    
    filme = Filme(titulo, duracao)
  
    print("\nDetalhes do Filme:")
    filme.exibir_detalhes()

if __name__ == "__main__":
    main()
