from banco import ContaBancaria

def main():
    conta = ContaBancaria()
    
    while True:
        print("\nEscolha uma operação:")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")
        
        escolha = input("Digite o número da operação desejada: ")
        
        if escolha == '1':
            conta.consultar_saldo()
        elif escolha == '2':
            valor_deposito = float(input("Digite o valor a ser depositado: R$"))
            conta.depositar(valor_deposito)
        elif escolha == '3':
            valor_saque = float(input("Digite o valor a ser sacado: R$"))
            conta.sacar(valor_saque)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
