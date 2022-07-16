class Pessoa:  # Essa classe também é chamada de super-classe ou classe mãe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando...')


class Cliente(Pessoa):  # Isso indica que Cliente herda uma Pessoa (tudo dessa classe)
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')  # Método próprio da classe Cliente, não pode ser usado em outra


class Aluno(Pessoa):  # Subclasse
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')
