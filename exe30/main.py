from carro import Carro

def main():
    marca_carro = input("Digite a marca do carro: ")
    carro = Carro(marca_carro)
    
    while True:
        print("\n--- Menu Carro ---")
        print("1. Abastecer o carro")
        print("2. Verificar nível de combustível")
        print("3. Sair")
        
        escolha = input("Escolha uma opção (1-3): ")
        
        if escolha == '1':
            quantidade = float(input("Digite a quantidade de combustível (em litros): "))
            carro.abastecer(quantidade)
        
        elif escolha == '2':
            carro.verificar_combustivel()
        
        elif escolha == '3':
            print("Saindo... Até logo!")
            break
        
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 3.")

if __name__ == "__main__":
    main()
