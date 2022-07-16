from aula112.eletronico import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1  # aqui um objeto da classe Cliente está sendo apagado
# Como na criação do objeto a classe Endereco é usada (criando objetos da classe Endereco), isso cria a composição
# Assim, ao apagar o objeto da classe Cliente, os objetos da classe Endereco associados ao objeto da classe Cliente
# Também são apagados
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
