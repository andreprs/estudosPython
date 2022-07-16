from time import sleep
from threading import Thread
from threading import Lock

""""
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        
        super().__init__()
        
    def run(self):
        sleep(self.tempo)
        print(self.texto)
    
    
t1 = MeuThread('thread 1', 5)
t1.start()

t2 = MeuThread('thread 2', 2)
t2.start()

t3 = MeuThread('thread 3', 7)
t3.start()

for i in range(20):
    print(i)
    sleep(1)
"""

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá mundo 2', 2))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo 3', 1))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
"""

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo', 10))
t1.start()

while t1.is_alive():
    print('Esperando a thread.')
    sleep(2)
"""


class Ingresso:
    def __init__(self, estoque) -> None:
        self.estoque = estoque
        self.lock = Lock()
    
    def comprar(self, quantidade):
        self.lock.acquire()
        
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return

        sleep(1)
        
        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s).'
              f'Ainda temos {self.estoque} em estoque')

        self.lock.release()
        


if __name__ == '__main__':
    ingressos = Ingresso(10)
    
    threads = []
    
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)
    
    for t in threads:
        t.start()
    
    executando = True
    while executando:
        executando = False
        
        for t in threads:
            if t.is_alive():
                executando = True
                break
            
    print()
    print(ingressos.estoque)
