from carro import Carro

def main():
    marca = input("Digite a marca do carro: ")
    ano = int(input("Digite o ano do carro: "))
    
    carro = Carro(marca, ano)
    
    carro.exibir_informacoes()

if __name__ == "__main__":
    main()
