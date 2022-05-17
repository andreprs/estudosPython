from jogador_futebol import JogadorFutebol

nome = input('Informe o nome do jogador: ').strip().capitalize()
posicao = input(f'Em que posição {nome} joga? ').strip().capitalize()
data_nascimento = input('Informe a data de nascimento (somente números. Ex: 11062001): ').strip()
nacionalidade = input('Qual é a nacionalidade do jogador? ').strip().capitalize()
altura = input('Qual a altura do jogador? ').strip()
peso = input('Qual o peso do jogador? ').strip()

jogador = JogadorFutebol(nome, posicao, data_nascimento, nacionalidade, altura, peso)
jogador.mostrar_infos()
jogador.calcular_idade()
