from funcionario import Funcionario

def main():
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: R$"))
    
    funcionario = Funcionario(nome, salario)
    
    while True:
        print("\n--- Menu ---")
        print("1. Exibir informações do funcionário")
        print("2. Calcular aumento de salário")
        print("3. Sair")
        
        escolha = input("Escolha uma opção (1-3): ")
        
        if escolha == '1':
            print(funcionario.exibir_informacoes())
        
        elif escolha == '2':
            percentual = float(input("Digite o percentual de aumento: "))
            aumento = funcionario.calcular_aumento(percentual)
            print(f"Aumento de R${aumento:.2f} aplicado. Novo salário: R${funcionario.salario:.2f}")
        
        elif escolha == '3':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 3.")

if __name__ == "__main__":
    main()
