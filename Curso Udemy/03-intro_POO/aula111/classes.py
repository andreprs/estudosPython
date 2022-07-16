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


class ClienteVIP(Cliente):  # Isso cria uma cadeia de heranças. ClienteVIP -> Cliente -> pessoa
    def falar(self):  # Cria uma sobreposição de métodos
        # Como cliente vip herda tudo de Cliente e de Pessoa, ClienteVIP tem acesso a todos os métodos dessas classes
        # Nesse exemplo, existe o método falar em Pessoa, porém ao definir em ClienteVIP outro método falar (mesmo nome)
        # Esse método será sobreposto, e ao chamar a instância com o método falar(), ele não irá usar o da classe
        # Pessoa, mas sim o da classe ClienteVIP
        print('Outra coisa qualquer.')
        super().falar()  # Isso chama o método da classe superior e executa tudo que está la dentro

        # O super faz o interpretador achar o método logo acima dele, ou seja, se tivesse um método falar() em Cliente
        # O interpretador irá executar esse método, e não o da classe mãe.
        # Para executar o da classe mãe, basta usar o nome da classe


class Aluno(Pessoa):  # Subclasse
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')
