class Agenda:
    def __init__(self):
        self.contatos = [] 

    def adicionar_contato(self, nome, telefone):
        contato = {"nome": nome, "telefone": telefone}
        self.contatos.append(contato)
        print(f"Contato de {nome} adicionado com sucesso!")

    def listar_contatos(self):
        if not self.contatos:
            print("Agenda vazia. Nenhum contato encontrado.")
        else:
            print("\n--- Contatos na Agenda ---")
            for contato in self.contatos:
                print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")
