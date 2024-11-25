from pessoa import Pessoa

def main():
    nome = input("Digite o nome da pessoa: ")
    altura = float(input("Digite a altura da pessoa (em metros): "))
    
    pessoa = Pessoa(nome, altura)
   
    print(pessoa.verificar_altura())

if __name__ == "__main__":
    main()
