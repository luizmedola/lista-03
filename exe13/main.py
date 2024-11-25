from veiculo import Veiculo

def main():
    modelo = input("Digite o modelo do veículo: ")
    velocidade_inicial = int(input("Digite a velocidade inicial do veículo (em km/h): "))
    
    veiculo = Veiculo(modelo, velocidade_inicial)
    
    while True:
        print("\nEscolha uma operação:")
        print("1. Exibir Detalhes do Veículo")
        print("2. Aumentar Velocidade")
        print("3. Sair")
        
        escolha = input("Digite o número da operação desejada: ")
        
        if escolha == '1':
            veiculo.exibir_detalhes()
        elif escolha == '2':
            incremento = int(input("Digite o incremento de velocidade (em km/h): "))
            veiculo.aumentar_velocidade(incremento)
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
