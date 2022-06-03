class Pessoa:  # Definindo classe pessoa e inicializando ela
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):  # Cliente que herda de Pessoa
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None  # Atributo da classe Cliente

    def inserir_conta(self, conta):
        self.conta = conta
