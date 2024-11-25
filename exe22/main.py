from agenda import Agenda

def main():
    agenda = Agenda() 
    
    while True:
        print("\n--- Menu da Agenda ---")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Sair")
        
        escolha = input("Escolha uma opção (1-3): ")
        
        if escolha == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        
        elif escolha == '2':
            agenda.listar_contatos()
        
        elif escolha == '3':
            print("Saindo da agenda...")
            break
        
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 3.")

if __name__ == "__main__":
    main()
