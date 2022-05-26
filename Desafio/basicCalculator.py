def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiplica (a, b):
    return a * b


opcoes = {
    'soma': soma,
    'subtracao': subtracao,
    'divide': divide,
    'multiplica': multiplica
}


def funcionamento(a, op, b):
    funcao = opcoes[op]
    return funcao(a, b)


num_1 = int(input('Informe o primeiro número: '))
operacao = input('Escolha uma das operações (soma, subtracao, divide, multiplica): ')
num_2 = int(input(f'Informe o número que irá fazer a operação acima com o número {num_1}: '))
print(f'Resultado: {funcionamento(num_1, operacao, num_2)}')
