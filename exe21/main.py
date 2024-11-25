from estoque import Livro

def main():
    livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 10)
    
    while True:
        print("\n--- Menu ---")
        print("1. Exibir detalhes do livro")
        print("2. Atualizar estoque")
        print("3. Sair")
        
        escolha = input("Escolha uma opção (1-3): ")
        
        if escolha == '1':
            print(livro.exibir_detalhes())
        
        elif escolha == '2':
            try:
                quantidade = int(input("Digite a quantidade a ser adicionada (ou removida, com número negativo): "))
                livro.atualizar_estoque(quantidade)
                print(f"Estoque atualizado. Novo estoque: {livro.estoque} unidades.")
            except ValueError:
                print("Por favor, digite um número válido.")
        
        elif escolha == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 3.")

if __name__ == "__main__":
    main()
