from calculadora import Calculadora

def main():
    calc = Calculadora()
    
    while True:
        print("\n--- Menu Calculadora ---")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Exibir Histórico")
        print("6. Sair")
        
        escolha = input("Escolha uma opção (1-6): ")
        
        if escolha in ['1', '2', '3', '4']:
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, insira números válidos.")
                continue
            
            if escolha == '1':
                resultado = calc.soma(a, b)
            elif escolha == '2':
                resultado = calc.subtracao(a, b)
            elif escolha == '3':
                resultado = calc.multiplicacao(a, b)
            elif escolha == '4':
                resultado = calc.divisao(a, b)
            
            print(f"Resultado: {resultado}")
        
        elif escolha == '5':
            print("\nHistórico de Operações:")
            print(calc.exibir_historico())
        
        elif escolha == '6':
            print("Saindo da calculadora...")
            break
        
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 6.")

if __name__ == "__main__":
    main()
