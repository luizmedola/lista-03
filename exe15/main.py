from quadrado import Quadrado

def main():
    lado = float(input("Digite o valor do lado do quadrado: "))
    
    quadrado = Quadrado(lado)

    quadrado.exibir_detalhes()

if __name__ == "__main__":
    main()
