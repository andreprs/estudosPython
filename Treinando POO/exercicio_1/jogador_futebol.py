from datetime import datetime


class Jogador_futebol():
    def __init__(self, nome, posicao, data_nascimento, nascionalidade, altura, peso) -> None:
        self.nome = nome
        self.posicao = posicao
        self.data_nascimento = data_nascimento
        self.nascionalidade = nascionalidade
        self.altura = altura
        self.peso = peso
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, valor):
        try:
            try:
                valor = datetime.strptime(valor, '%d/%m/%Y')
                valor = valor.strftime('%d/%m/%Y')
            except ValueError:
                try:
                    valor = datetime.strptime(valor, '%d%m%Y')
                    valor = valor.strftime('%d/%m/%Y')
                except ValueError:
                    valor = 'Desconhecido'
        
        except ValueError:
            valor = 'Desconhecido'
            
        self._data_nascimento = valor
    
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        try:
            float(valor)
            self._altura = valor
        except ValueError:
            self._altura = 'Desconhecida'
    
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, valor):
        try:
            float(valor)
            self._peso = valor
        except ValueError:
            self._peso = 'Desconhecido'
    
    def calcular_idade(self) -> int:
        try:
            idade = datetime.now().year - int(self.data_nascimento[6:])
            return idade
        except ValueError:
            return 'Idade desconhecida'
    
    def aposentar(self) -> str:
        try:
            idade = datetime.now().year - int(self.data_nascimento[6:])
        except ValueError:
            return 'Desconhecido'

        posicoes = {
            'defesa': 'defesa',
            'meio-campo': ['meio', 'meio campo', 'meio-campo', 'meiocampo'],
            'ataque': ['ataque', 'atacante']
        }
        
        if self.posicao in posicoes['defesa']:
            if idade >= 40:
                return 'Aposentado'
            else:
                return f'{40 - idade} anos para se aposentar'
        
        elif self.posicao in posicoes['ataque']:
            if idade >= 35:
                return 'Aposentado'
            else:
                return f'{35 - idade} anos para se aposentar'
            
        elif self.posicao in posicoes['meio-campo']:
            if idade >= 38:
                return 'Aposentado'
            else:
                return f'{38 - idade} anos para se aposentar'
            
        else:
            return 'Desconhecido'
            
    def mostrar_infos(self):
        print()
        print('-' * 30)
        print(f'Nome: {self.nome}')
        print(f'Posição: {self.posicao}')
        print(f'Data de nascimento: {self.data_nascimento}')
        print(f'Nascionalidade: {self.nascionalidade}')
        print(f'Altura(m): {self.altura}')
        print(f'Peso(Kg): {self.peso}')
