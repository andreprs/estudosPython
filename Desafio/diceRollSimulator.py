from random import randint

print('Hora de rolar os dados!')
print('PARA SAIR DO PROGRAMA A QUALQUER MOMENTO DIGITE 0\n')
escolhas = ['d6', 'd12', 'd20']
while True:
    rolada = input('Qual dado você quer jogar? (d6, d12, d20) ').strip().lower()
    if rolada == '0':
        print('\nPrograma encerrado...')
        break
    if rolada not in escolhas:
        print('A opção informada não existe.')
        continue
    if rolada == escolhas[0]:
        print(f'{randint(1, 6)}\n')
    elif rolada == escolhas[1]:
        print(f'{randint(1, 12)}\n')
    elif rolada == escolhas[2]:
        print(f'{randint(1, 20)}\n')
