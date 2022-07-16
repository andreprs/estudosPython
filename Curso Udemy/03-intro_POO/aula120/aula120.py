class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'b_fala' not in namespace:
            print(f'Oi, você precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, não atributo em {name}')
        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atributo.')
            del namespace['attr_classe']
        # print(mcs)  # para saber o que cada coisa é
        # print(name)
        # print(bases)
        # print(namespace)
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()

    attr_classe = 'Valor A'


class B(A):
    teste = 'Valor'
    b_fala = 'WOW'
    attr_classe = 'Valor B'

    def sei_la(self):
        pass

    def b_fala(self):
        print('Oi')


b = B()
print(b.attr_classe)
