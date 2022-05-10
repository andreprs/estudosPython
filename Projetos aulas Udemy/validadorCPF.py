from time import sleep
from random import randint


# NECESSÁRIO ARRUMAR EM CASO DE NÚMEROS TODOS IGUAIS. EX: 999.999.999-99
def validar(cpf):
    cpf_temporario = str(cpf)
    cpf_validado = ''
    i = 10
    controle = 9
    for c in range(2):
        soma = 0
        for posicao, letra in enumerate(cpf_temporario):
            if posicao < controle:
                soma += (int(letra) * i)
                if c == 0:
                    cpf_validado += letra
                i -= 1
            else:
                break
        operacao = 11 - (soma % 11)
        if operacao <= 9:
            cpf_validado += str(operacao)

        else:
            cpf_validado += '0'
        i = 11
        controle = 10
    if cpf_validado == cpf_temporario:
        return True
    else:
        return False


# Programa principal
while True:
    print('\nEscolha uma opção: \n1 - Validar um cpf \n2 - Gerar um cpf válido \n3 - Sair do programa')
    try:
        resposta = int(input('Sua opção: '))
    except:
        print('\033[1;31mERRO. Informe um número inteiro válido.\033[m')
        sleep(1.5)
    else:
        if not 0 < resposta <= 3:
            print('\033[1;31mERRO. Opção inválida.\033[m')
            sleep(1.5)
            continue
        else:
            if resposta == 1:
                while True:
                    try:
                        ler_cpf = int(input('\nInforme o CPF que deseja validar (somente 11 digitos inteiros): '))
                    except:
                        print('\033[1;31mERRO. Números inválidos.\033[m')
                        sleep(1.5)
                        continue
                    else:
                        if len(str(ler_cpf)) < 11 or len(str(ler_cpf)) > 11:
                            print('\033[1;31mERRO. Quantidade de números inválida.\033[m')
                            sleep(1)
                            continue
                        if validar(ler_cpf):
                            print('\033[1;32mCPF válido.\033[m')
                        else:
                            print('\033[1;31mCPF inválido.\033[m')
                        sleep(1.5)
                        break
            elif resposta == 2:
                while True:
                    novo_cpf = randint(00000000000, 99999999999)  # Não tenho certeza se essa sintaxe está correta
                    if validar(novo_cpf):
                        print(f'\n\033[1;32mCPF gerado:\033[m {novo_cpf}')
                        sleep(2)
                        break
            else:
                print('\n\033[1;31mPrograma finalizado...\033[m')
                sleep(2)
                break
