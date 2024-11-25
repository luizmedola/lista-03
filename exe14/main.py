from eletrodomestico import Eletrodomestico

def main():
    nome = input("Digite o nome do eletrodoméstico: ")
    potencia = int(input("Digite a potência do eletrodoméstico em watts: "))
    
    eletrodomestico = Eletrodomestico(nome, potencia)
    
    while True:
        print("\nEscolha uma operação:")
        print("1. Exibir Detalhes do Eletrodoméstico")
        print("2. Ligar o Eletrodoméstico")
        print("3. Desligar o Eletrodoméstico")
        print("4. Sair")
    
        escolha = input("Digite o número da operação desejada: ")
        
        if escolha == '1':
            eletrodomestico.exibir_detalhes()
        elif escolha == '2':
            eletrodomestico.ligar()
        elif escolha == '3':
            eletrodomestico.desligar()
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
