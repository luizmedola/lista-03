from jogo import Jogo

def main():
    nome_jogo = input("Digite o nome do jogo: ")
    jogo = Jogo(nome_jogo)
    
    while True:
        print("\n--- Menu Jogo ---")
        print("1. Iniciar Jogo")
        print("2. Registrar Pontuação")
        print("3. Exibir Pontuação Atual")
        print("4. Sair")
        
        escolha = input("Escolha uma opção (1-4): ")
        
        if escolha == '1':
            jogo.iniciar_jogo()
        
        elif escolha == '2':
            pontos = int(input("Digite os pontos a serem registrados: "))
            jogo.registrar_pontuacao(pontos)
        
        elif escolha == '3':
            jogo.exibir_pontuacao()
        
        elif escolha == '4':
            print("Saindo do jogo... Até logo!")
            break
        
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")

if __name__ == "__main__":
    main()
