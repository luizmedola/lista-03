from circulo import Circulo

def main():
    raio = float(input("Digite o raio do círculo: "))

    circulo = Circulo(raio)

    perimetro = circulo.calcular_perimetro()
    print(f"O perímetro do círculo é: {perimetro:.2f}")

if __name__ == "__main__":
    main()
