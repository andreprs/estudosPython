from random import choice
from time import sleep


def ganhou(jogador, computador):
    print('Parabéns, você ganhou :)')
    print(f'As escolhas foram: \nJogador = {jogador}\nComputador = {computador}')


rodadasJogadas = 0
vitorias = 0

print('PEDRA, PAPEL OU TESOURA!')
respostas = ['Pedra', 'Papel', 'Tesoura']
while True:
    respJogador = None
    rodadasJogadas += 1
    respComputador = choice(respostas)
    while respJogador not in respostas:
        respJogador = input('\nPedra, papel ou tesoura? ').strip().capitalize()
        if respJogador not in respostas:
            print('Resposta não existe. Tente novamente...\n')
    print('Analisando resultados...')
    sleep(2)
    if respJogador == respComputador:
        print('Ops! Houve um empate :D\n')
    elif respJogador == 'Pedra' and respComputador == 'Tesoura':
        ganhou(respJogador, respComputador)
        vitorias += 1
    elif respJogador == 'Papel' and respComputador == 'Pedra':
        ganhou(respJogador, respComputador)
        vitorias += 1
    elif respJogador == 'Tesoura' and respComputador == 'Papel':
        ganhou(respJogador, respComputador)
        vitorias += 1
    else:
        print('\nVocê perdeu :(')
        print(f'As escolhas foram: \nJogador: {respJogador}\nComputador: {respComputador}')
    continua = input('\nDeseja jogar de novo? [S]im ou [N]ão: ').strip().upper()
    while continua not in 'SN':
        print('Desculpa, não entendi sua resposta. Tente novamente.')
        continua = input('Continuar? [S]im ou [N]ão: ').strip().upper()
    if continua == 'N':
        print(f'\nVocê jogou um total de {rodadasJogadas} e ganhou {vitorias} dessas rodadas.')
        print('Encerrando programa...')
        sleep(1.5)
        break
    else:
        continue
