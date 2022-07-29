from random import randint


def get_cpf(stdscr) -> str:
    '''
    Input do cpf pelo usuário. O input não permite outros tipos de caracteres a não ser números.
    
        Returns:
            cpf (str): cpf informado pelo usuário (input)
    '''
    
    cpf = []
    stdscr.clear()
   
    while True:
        if len(cpf) == 11:
            cpf = ''.join(cpf)  # convertendo a lista em uma string única
            break
        
        stdscr.addstr('Informe o CPF: ')
        for digito in cpf:
            stdscr.addstr(digito)
        stdscr.refresh()
        char = stdscr.getkey()
        
        if ord(char) == 27:
            exit()  # sair do programa a qualquer momento
            
        if char in ('KEY_BACKSPACE', '\b', '\x7f'):
            if len(cpf) > 0:
                cpf.pop()
        else:
            try:
                int(char)  # conferindo se o caracter digitado é um número
                cpf.append(char)
            except ValueError:
                pass
                            
        stdscr.clear()
    
    return cpf


def formatar(cpf) -> str:
    '''
    Formata o CPF para o padrão XXX.XXX.XXX-XX
    
        Parameters:
            cpf (str): cpf retornado na função get_cpf (input do usuário)
        
        Returns:
            str: cpf formatado no padrão XXX.XXX.XXX-XX usando f-strings
    '''
    
    return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    
    
def validar(cpf):
    '''
    Faz a validação matemática do CPF informado pelo usuário. Para mais informações sobre os passos dessa validação
    acesse: https://www.calculadorafacil.com.br/computacao/validar-cpf
    
        Parameters:
            cpf (str): cpf retornado na função get_cpf (input do usuário)
        
        Returns:
            boolean: true se o cpf é matematicamente válido e false se não é válido.
    '''
    
    cpf_numeros = [int(digito) for digito in cpf]
    cpf_validado = ''
    
    sequencia = cpf == (cpf[0] * len(cpf))  # verificando sequência de 11 num.
    if sequencia:
        return False
    
    controle = 10
    limite = 9
        
    for t in range(2):
        soma = 0
            
        for posicao, digito in enumerate(cpf_numeros):
            if posicao < limite:
                soma += digito * controle
                
                if t == 0:
                    cpf_validado += str(digito)
                controle -= 1
            else:
                break
            
        operacao = 11 - (soma % 11)
            
        if operacao <= 9:
            cpf_validado += str(operacao)
        else:
            cpf_validado += '0'
            
        controle = 11
        limite = 10
        
    if cpf_validado == cpf:
        return True
    else:
        return False 
     
        
def gerar() -> str:
    '''
    Gera aleatoriamente um CPF até que ele seja validado pela função validar().
    
        Returns:
            cpf_gerado (str): cpf gerado, validado e formatado.
    '''
    valido = False
    
    while not valido:
        cpf_gerado = ''
        for t in range(11):
            temp = randint(0, 9)
            cpf_gerado += str(temp)
        
        if validar(cpf_gerado):
            valido = True
    return formatar(cpf_gerado)
