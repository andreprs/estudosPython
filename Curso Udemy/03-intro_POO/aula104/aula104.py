"""
public, protected e private
"""


class BaseDados:
    def __init__(self):  # construtor
        self.__dados = {}  # coração da classe, tudo gira em torno dela e até o momento ele está público

    @property
    def dados(self):
        return self.__dados

    def inserir_ciente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}  # primeira execução é criado
        else:
            self.__dados['clientes'].update({id: nome})  # a partir da primeira ele vai atualizando

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDados()
bd.inserir_ciente(1, 'Andre')
bd.inserir_ciente(2, 'Prasel')
bd.inserir_ciente(3, 'Helena')
# bd.dados = 'Qualquer coisa'  # caso isso seja feito, toda a classe é quebrada
# Em outra linguagem de programação isso é contornado usando as palavras citadas no início.
# Privado "fraco": renomear o atributo ou método com um underline [ _ ] no início do seu nome.
# Privado "forte": renomear o atributo ou método com dois underlines [ __ ] no início do seu nome.
bd.__dados = 'Qualquer coisa'  # modificação
bd.lista_clientes()

print(bd.__dados)  # mostra a modificação feita anteriormente
print(bd._BaseDados__dados)  # busca na classe e mostra o dicionário definido nela

print(bd.dados)
