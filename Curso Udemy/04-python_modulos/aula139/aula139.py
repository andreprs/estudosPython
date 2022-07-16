import random

inteiro = random.randint(10, 20)  # gera num aleat. entre 10 e 20
print(inteiro)

# gera número aleatório de forma semelhante a função range (inicio, fim, passo)
inteiro_2 = random.randrange(900, 1000, 10)
print(inteiro_2)

real = random.uniform(10, 20)  # gera num aleat. real entre 10 e 20
print(real)

flutuante = random.random()  # gera num aleat. real entre 0 e 1
print(flutuante)

lista = ['Andre', 'Helena', 'Rafa', 'Hiro']
sorteio = random.choice(lista)  # escolhe aleatoriamente um item da lista
sorteio_2 = random.choices(lista, k=2)  # escolhe aleatoriamente x itens da 
                                        # lista e retorna em forma de lista
                                        # aqui é possível repetição
sorteio_3 = random.sample(lista, 2)  # faz a mesma coisa que acima, sem rept.

random.shuffle(lista)  # embaralha a lista

print(sorteio)
print(sorteio_2)
print(sorteio_3)
print(lista)
