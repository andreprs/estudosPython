class A:
    def falar(self):
        print('Falando... Estou em A.')


class B(A):
    def falar(self):
        print('Falando... Estou em B.')


class C(A):
    def falar(self):
        print('Falando... Estou em C.')


class D(B, C):  # problema do diamente
    pass  # O interpretador python busca da esquerda para a direita qual método executar
          # Nesse exemplo acima, o método falar em B seria executado caso instanciado.


d = D()
d.falar()
