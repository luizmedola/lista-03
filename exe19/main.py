from moeda import ConversorMoeda

def main():
    taxa_conversao = float(input("Digite a taxa de conversão de dólares para reais: "))
    
    conversor = ConversorMoeda(taxa_conversao)
    
    dolares = float(input("Digite o valor em dólares: "))
    
    reais = conversor.converter_dolares_para_reais(dolares)
  
    print(f"{dolares} dólares equivalem a {reais:.2f} reais.")

if __name__ == "__main__":
    main()
