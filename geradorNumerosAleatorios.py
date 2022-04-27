from random import randint

print('GERADOR DE NÚMEROS ALEATÓRIOS')
while True:
    try:  # Perguntar se o usuário deseja escolher o intervalo que o número estará
        pergunta = input('Deseja escolher os limites de aleatoriedade? [S] Sim / [N] Não: ').upper().strip()
    except ValueError:
        print('Ocorreu um erro. Tente novamente.')
        continue
    else:
        if pergunta == 'S':
            while True:
                try:
                    limiteA = int(input('Digite o primeiro limite: '))
                    limiteB = int(input('Digite o segundo limite: '))
                except ValueError:
                    print('Ocorreu um erro. Digite números inteiros.')
                    continue
                else:
                    if limiteA > limiteB:
                        print('O primeiro limite não pode ser maior que o segundo.')
                        continue
                    numeroAleatorio = randint(limiteA, limiteB)
                    print(f'Número gerado: {numeroAleatorio}')
                    break
            break
        elif pergunta == 'N':
            print('Limite de aleatoriedade: [-999999, 999999]')
            numeroAleatorio = randint(-999999, 999999)
            print(f'Número gerado: {numeroAleatorio}')
            break
        else:
            print('Erro. Resposta não existe, tente novamente.')
            continue
