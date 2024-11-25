from retangulo import Retangulo

def main():
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    
    retangulo = Retangulo(largura, altura)
    
    area = retangulo.calcular_area()
    print(f"A área do retângulo é: {area}")

if __name__ == "__main__":
    main()
