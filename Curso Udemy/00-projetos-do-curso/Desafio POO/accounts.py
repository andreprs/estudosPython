from abc import ABC, abstractmethod


class Conta(ABC):  # Herdando de ABC para poder ter métodos abstratos
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia}\nConta: {self.numero}\nSaldo: {self.saldo}\n')

    @abstractmethod  # Método abstrato que classes filhas abaixo precisam ter, mas com comportamento diferente
    def sacar(self, valor): pass


class ContaPoupanca(Conta):
    # Não precisa de inicializador, pois herda de conta e ja possui todas as informações
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente...\n')
            return
        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite=200):  # Inicializador da classe ContaCorrente
        # Precisa desse inicializador, pois há um novo parâmetro
        super().__init__(agencia, numero, saldo)
        self.limite = limite  # Atributo da classe ContaCorrente

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print('Saldo insuficiente...\n')
            return
        self.saldo -= valor
        self.detalhes()
