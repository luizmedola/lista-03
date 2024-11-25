from produto import Produto

def main():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    
    produto = Produto(nome, preco)

    percentual_desconto = float(input("Digite o percentual de desconto: "))
    
    novo_preco = produto.aplicar_desconto(percentual_desconto)
    print(f"O preço do {produto.nome} após o desconto de {percentual_desconto}% é: R${novo_preco:.2f}")

if __name__ == "__main__":
    main()
