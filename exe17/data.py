class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatar_data(self):
        return f"{self.dia:02}/{self.mes:02}/{self.ano}"
