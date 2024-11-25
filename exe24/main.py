from elevador import Elevador

def main():
    total_andar = int(input("Digite o total de andares do prédio: "))
    
    elevador = Elevador(total_andar)

    while True:
        print("\n--- Menu do Elevador ---")
        print("1. Subir um andar")
        print("2. Descer um andar")
        print("3. Verificar andar atual")
        print("4. Sair")
        
        escolha = input("Escolha uma opção (1-4): ")
        
        if escolha == '1':
            elevador.subir()
        
        elif escolha == '2':
            elevador.descer()
        
        elif escolha == '3':
            print(elevador.exibir_andar_atual())
        
        elif escolha == '4':
            print("Saindo do elevador...")
            break
        
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")

if __name__ == "__main__":
    main()
