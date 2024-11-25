from data import Data

def main():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
   
    data = Data(dia, mes, ano)
 
    print(f"A data formatada é: {data.formatar_data()}")

if __name__ == "__main__":
    main()
