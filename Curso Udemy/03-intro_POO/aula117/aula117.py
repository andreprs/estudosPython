class A:
    # def __new__(cls, *args, **kwargs):  é como se substituisse a função do init
    #     cls.nome = 'André'
    #
    #     def haha(*args, **kwargs):
    #         if not hasattr(cls, '__jaexiste'):
    #             cls._jaexiste = object.__new__(cls)
    #         print('Fala Oi')
    #
    #     cls.haha = haha
    #
    #     return super().__new__(cls)

    def __init__(self):
        print('INIT')

    def __setattr__(self, key, value):
        if key == 'nome':
            self.__dict__[key] = 'Você não pode fazer isso'
        else:
            self.__dict__[key] = value

    # def __call__(self, *args, **kwargs):  # faz a classe funcionar como uma função
    #     resultado = 1                     # isso acontece apenas quando a instância é chamada como uma função
    #     for i in args:                    # se houver outros métodos na classe eles podem ser chamados normalmente
    #         resultado *= i
    #     return resultado


a = A()
# variavel = a(1, 2, 3, 4, 5)
# print(variavel)
a.nome = 'Andre'
a.qualquer = 255
print(a.nome, a.qualquer)
