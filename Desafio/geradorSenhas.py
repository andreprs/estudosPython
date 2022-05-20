from random import randint

print('GERADOR DE SENHAS')

caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%&'
continua = ' '
while continua not in ['SAIR', 'S', 'SAI']:
    while True:
        try:
            quantidade = int(input('\nInforme o número de caracteres desejado para a senha: '))
        except ValueError:
            print('Erro. Informe um número inteiro válido.')
            continue
        else:
            if quantidade <= 0:
                print('Número de caracteres inválido.')
                continue
            break
    senha = ''
    for c in range(0, quantidade):
        senha += caracteres[randint(0, len(caracteres))]
    print(f'Senha gerada: {senha}\n')
    continua = input('Precione qualquer tecla para continuar. Caso deseja sair digite [Sair]: ').upper()
