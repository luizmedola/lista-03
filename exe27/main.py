from animal import Animal

def main():
    print("Bem-vindo ao simulador de movimentos de animais!")
    
    peixe = Animal("peixe", "nada")
    cavalo = Animal("cavalo", "galopa")
    ave = Animal("ave", "voa")
    
    while True:
        print("\nEscolha um animal para ver como ele se move:")
        print("1. Peixe")
        print("2. Cavalo")
        print("3. Ave")
        print("4. Sair")
        
        escolha = input("Escolha uma opção (1-4): ")
        
        if escolha == '1':
            peixe.mover()
        elif escolha == '2':
            cavalo.mover()
        elif escolha == '3':
            ave.mover()
        elif escolha == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")

if __name__ == "__main__":
    main()
