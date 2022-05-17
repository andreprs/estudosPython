from datetime import date


class JogadorFutebol:
    def __init__(self, nome, posicao, data_nascimento, nacionalidade, altura, peso):
        self.nome = nome
        self.posicao = posicao
        self.data_nascimento = data_nascimento
        self.nacionalidade = nacionalidade
        self.altura = altura
        self.peso = peso

    def mostrar_infos(self):
        print(f'\n{"-" * 20}')
        print('Dados do jogador.')
        print(f'Nome: {self.nome}\nPosição: {self.posicao}\nData de nascimento: {self.data_nascimento}')
        print(f'Nacionalidade: {self.nacionalidade}\nAltura: {self.altura}\nPeso: {self.peso}')

    def calcular_idade(self):
        defesa = ['Zagueiro', 'Lateral', 'Lateral esquerdo', 'Lateral direito', 'Libero', 'Goleiro', 'Defesa']
        meio_campo = ['Meio', 'Volante', 'Ala', 'Ala direito', 'Ala esquerdo', 'Meio campo']
        ataque = ['Atacante', 'Ponta esquerda', 'Ponta direito', 'Ponta', 'Centroavante', 'Ataque']

        ano_atual = date.today()
        if self.data_nascimento == 'DESCONHECIDO':
            idade = 'DESCONHECIDO'
        else:
            idade = int(ano_atual.year) - int(self.data_nascimento[6:])  # DD/MM/AAAA
        print(f'\nO jogador tem {idade} anos.')
        if not idade == 'DESCONHECIDO':
            if self.posicao in defesa:
                falta = 40 - idade
                if idade > 0:
                    print(f'Aposentadoria: falta(m) {falta} anos.')
                else:
                    print('Aposentadoria: o jogador ja deve estar aposentado.')
            elif self.posicao in meio_campo:
                falta = 38 - idade
                if idade > 0:
                    print(f'Aposentadoria: falta(m) {falta} anos.')
                else:
                    print('Aposentadoria: o jogador ja deve estar aposentado.')
            elif self.posicao in ataque:
                falta = 35 - idade
                if idade > 0:
                    print(f'Aposentadoria: falta(m) {falta} anos.')
                else:
                    print('Aposentadoria: o jogador ja deve estar aposentado.')
            else:
                print('Aposentadoria: DESCONHECIDA')

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, entrada):
        try:
            entrada = float(entrada)
        except ValueError:
            entrada = 'DESCONHECIDA'
        self._altura = f'{entrada} [m]'

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, entrada):
        try:
            entrada = float(entrada)
        except ValueError:
            entrada = 'DESCONHECIDO'
        self._peso = f'{entrada} [kg]'

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data):
        dia = mes = ano = None
        if len(data) != 8 or not data.isnumeric():
            data = 'DESCONHECIDO'
        else:
            dia = data[0:2]
            mes = data[2:4]
            ano = data[4:]
            data = f'{dia}/{mes}/{ano}'
        self._data_nascimento = data
