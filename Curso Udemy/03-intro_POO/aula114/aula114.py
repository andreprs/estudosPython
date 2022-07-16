from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg):
        pass


class B(A):
    def fala(self, msg):  # método fala que tem assinatura fala e msg
        print(f'B está falando {msg}')


class C(A):
    def fala(self, msg):  # aqui o polimorfismo acontece, a classe herda de uma super classe
        print(f'C falando {msg}')  # o método tem as mesmas assinaturas, mas um comportamento diferente
# Mesmo que apenas uma letra esteja sendo mudada (B para C, no print), já é uma mudança, assim considernado polimorfismo


b = B()
c = C()
b.fala('Um assunto')
c.fala('Outro assunto')
