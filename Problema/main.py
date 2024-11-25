# main.py
from calculadora import Calculadora

def mostrar_menu():
    print("\nEscolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

def executar_calculadora():
    calculadora = Calculadora()
    
    while True:
        mostrar_menu()
        try:
            opcao = int(input("Digite a opção desejada: "))
            
            if opcao == 5:
                print("Saindo...")
                break

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            resultado = calculadora.realizar_operacao(opcao, num1, num2)
            print(f"Resultado: {resultado}")
            
            repetir = input("Deseja realizar outra operação?: ").lower()
            if repetir != 's':
                print("Saindo...")
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")

if __name__ == "__main__":
    executar_calculadora()
