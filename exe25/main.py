from pessoa import Pessoa

def main():
    print("Bem-vindo ao cálculo de IMC!")
    
    peso = float(input("Digite o seu peso (em kg): "))
    altura = float(input("Digite a sua altura (em metros): "))
    
    pessoa = Pessoa(peso, altura)
    
    print("\nInformações da Pessoa:")
    print(pessoa.exibir_informacoes())

if __name__ == "__main__":
    main()
