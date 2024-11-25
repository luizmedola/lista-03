from relogio import Relogio

def main():
    hora = int(input("Digite a hora (0-23): "))
    minuto = int(input("Digite o minuto (0-59): "))
    segundo = int(input("Digite o segundo (0-59): "))
    
    relogio = Relogio(hora, minuto, segundo)
    
    print(f"O horário é: {relogio.exibir_horario()}")

if __name__ == "__main__":
    main()
