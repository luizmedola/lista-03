from temperatura import Temperatura

def main():
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    
    temperatura = Temperatura()

    fahrenheit = temperatura.celsius_para_fahrenheit(celsius)
    
    print(f"A temperatura de {celsius}°C é equivalente a {fahrenheit:.2f}°F.")

if __name__ == "__main__":
    main()
