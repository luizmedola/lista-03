class ConversorMoeda:
    def __init__(self, taxa_conversao):
        self.taxa_conversao = taxa_conversao 

    def converter_dolares_para_reais(self, dolares):
        reais = dolares * self.taxa_conversao
        return reais
