from banco_class import Banco
from banco_class import ContaBancaria

def main():
    banco = Banco()

    while True:
        print("\n--- Menu Banco ---")
        print("1. Adicionar Conta")
        print("2. Depositar em Conta")
        print("3. Sacar de Conta")
        print("4. Listar Saldos de Todas as Contas")
        print("5. Sair")
        
        escolha = input("Escolha uma opção (1-5): ")
        
        if escolha == '1':
            nome = input("Digite o nome do titular da conta: ")
            saldo_inicial = float(input("Digite o saldo inicial da conta: R$"))
            conta = ContaBancaria(nome, saldo_inicial)
            banco.adicionar_conta(conta)
            print(f"Conta de {nome} criada com sucesso!")
        
        elif escolha == '2':
            nome = input("Digite o nome do titular da conta para depósito: ")
            valor = float(input("Digite o valor do depósito: R$"))
            conta_encontrada = None
            for conta in banco.contas:
                if conta.titular.lower() == nome.lower():
                    conta_encontrada = conta
                    break
            
            if conta_encontrada:
                conta_encontrada.depositar(valor)
            else:
                print("Conta não encontrada.")
        
        elif escolha == '3':
            nome = input("Digite o nome do titular da conta para saque: ")
            valor = float(input("Digite o valor do saque: R$"))
            conta_encontrada = None
            for conta in banco.contas:
                if conta.titular.lower() == nome.lower():
                    conta_encontrada = conta
                    break
            
            if conta_encontrada:
                conta_encontrada.sacar(valor)
            else:
                print("Conta não encontrada.")
        
        elif escolha == '4':
            banco.listar_saldos()
        
        elif escolha == '5':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 5.")

if __name__ == "__main__":
    main()
