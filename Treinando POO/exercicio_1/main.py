import jogador_futebol as jf

nome = input('Nome do jogador: ').title()
posicao = input('Posição: ').lower()
data_nascimento = input('Data de nascimento (Formato xx/xx/xxxx): ')
nascionalidade = input('Nascionalidade: ').lower()
altura = input('Altura: ')
peso = input('Peso: ')

jogador = jf.Jogador_futebol(nome, posicao, data_nascimento, nascionalidade, altura, peso)

jogador.mostrar_infos()
print(f'Idade do jogador: {jogador.calcular_idade()}')
print(f'Status de aposentadoria: {jogador.aposentar()}')
