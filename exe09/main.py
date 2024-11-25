from aluno import Aluno

def main():
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    aluno = Aluno(nome, nota)
    
    resultado = aluno.verificar_aprovacao()
    print(resultado)

if __name__ == "__main__":
    main()
