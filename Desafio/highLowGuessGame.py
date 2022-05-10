from random import randint


def analisa(aleatorio, chute):
    if chute > aleatorio:
        print('\nHmmm... Chute muito alto.')
    else:
        print('\nHmmm... Chute muito baixo.')


num_aleatorio = randint(1, 10)
tentativa = None
print('VAMOS JOGAR\n')
while True:
    try:
        tentativa = int(input('Pensei em um número entre 1 e 10. Consegue adivinhar? '))
    except ValueError:
        print('Digite um número inteiro.')
        continue
    else:
        break
if tentativa == num_aleatorio:
    print('Parabéns, você acertou!')
else:
    analisa(num_aleatorio, tentativa)
    while tentativa != num_aleatorio:
        while True:
            try:
                tentativa = int(input('Tente novamente: '))
            except ValueError:
                print('Digite um número inteiro.')
                continue
            else:
                break
        if tentativa == num_aleatorio:
            print('Parabéns, você ganhou!')
        else:
            analisa(num_aleatorio, tentativa)
