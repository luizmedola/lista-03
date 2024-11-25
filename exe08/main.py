from calculadora import Calculadora

def main():
    calc = Calculadora()
    
    while True:
        print("\nEscolha uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Sair")
     
        escolha = input("Digite o número da operação desejada: ")
        
        if escolha == '1' or escolha == '2':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if escolha == '1':
                resultado = calc.somar(num1, num2)
                print(f"O resultado da soma é: {resultado}")
            elif escolha == '2':
                resultado = calc.subtrair(num1, num2)
                print(f"O resultado da subtração é: {resultado}")
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
