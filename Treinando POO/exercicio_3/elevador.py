class Elevador:
    def __init__(self, andar_atual=0, total_andares=0, capacidade=0, qtd_pessoas=0) -> None:
        self.__andar_atual = andar_atual
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__qtd_pessoas = qtd_pessoas
    
    @property
    def andar_atual(self):
        return self.__andar_atual
    
    @andar_atual.setter
    def andar_atual(self, andar_atual):
        self.__andar_atual = andar_atual
    
    @property
    def total_andares(self):
        return self.__total_andares
    
    @total_andares.setter
    def total_andares(self, total_andares):
        self.__total_andares = total_andares
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade
    
    @property
    def qtd_pessoas(self):
        return self.__qtd_pessoas
    
    @qtd_pessoas.setter
    def qtd_pessoas(self, qtd_pessoas):
        self.__qtd_pessoas = qtd_pessoas
    
    def entrar(self):
        if (self.__qtd_pessoas >= self.__capacidade):
            print('Capacidade máxima de pessoas atingida.\n')
        else:
            print('Uma pessoa entrou no elevador\n')
            self.__qtd_pessoas += 1
    
    def sair(self):
        if not (self.__qtd_pessoas == 0):
            print('Uma pessoa saiu do elevador.\n')
            self.__qtd_pessoas -= 1
        else:
            print('O elevador está vazio.\n')
    
    def subir(self):
        if (self.__andar_atual < self.__total_andares):
            print('O elevador subiu um andar.\n')
            self.__andar_atual += 1
        else:
            print('O elevador está no último andar, não é possível subir mais\n')
    
    def descer(self):
        if (self.__andar_atual > 0):
            print('O elevador desceu um andar.\n')
            self.__andar_atual -= 1
        else:
            print('O elevador está no térreo, não é possível descer mais\n')
