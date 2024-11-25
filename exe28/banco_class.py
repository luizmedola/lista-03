class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Valor de depósito deve ser positivo.")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso!")
        elif valor > self.saldo:
            print("Saldo insuficiente para o saque.")
        else:
            print("Valor de saque deve ser positivo.")
    
    def obter_saldo(self):
        return self.saldo
