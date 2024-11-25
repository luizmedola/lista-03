from pessoa import Pessoa

def main():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    
    pessoa = Pessoa(nome, idade)
   
    pessoa.imprimir_informacoes()

if __name__ == "__main__":
    main()
