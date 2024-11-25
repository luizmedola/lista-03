from pessoa import Pessoa

def main():
    nome_pessoa1 = input("Digite o nome da primeira pessoa: ")
    pessoa1 = Pessoa(nome_pessoa1)
    
    nome_pessoa2 = input("Digite o nome da segunda pessoa: ")
    pessoa2 = Pessoa(nome_pessoa2)
    
    pessoa1.cumprimentar(pessoa2)

if __name__ == "__main__":
    main()
