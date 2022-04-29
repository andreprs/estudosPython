from random import uniform

print('GERADOR DE NÚMEROS ALEATÓRIOS\n')
while True:
    try:
        menu = int(input('Escolha uma opção abaixo. \n[ 1 ] Gerar número totalmente aleatório'
                         '\n[ 2 ] Escolher intervalo para gerar número \nSua escolha: '))
    except ValueError:
        print('Desculpe, resposta inválida. Tente novamente.')
        continue
    else:
        if menu != 1 and menu != 2:
            print('Opção não existe.')
            continue
        else:
            break
if menu == 1:
    numeroAleatorio = uniform(-999999, 999999)
    print(f'O número aleatório é: {numeroAleatorio:3f}')
else:
    print('\nEscolha um intervalo.')
    while True:
        try:
            limiteA = int(input('Primeiro limite: '))
            limiteB = int(input('Segundo limite: '))
        except ValueError:
            print('Informe números inteiros.')
            continue
        else:
            if limiteA > limiteB:
                print('O primeiro limite não pode ser maior que o segundo.')
                continue
            else:
                numeroAleatorio = uniform(limiteA, limiteB)
                print(f'\nNúmero gerado entre {limiteA} e {limiteB}: {numeroAleatorio:.3f}')
                break
