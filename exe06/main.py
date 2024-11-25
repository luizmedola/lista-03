from animal import Animal

def main():
    especie = input("Digite a espécie do animal: ")
    som = input("Digite o som do animal: ")
  
    animal = Animal(especie, som)
    
    animal.fazer_som()

if __name__ == "__main__":
    main()
