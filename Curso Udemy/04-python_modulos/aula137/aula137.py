from dados import *
import json

# convertendo uma lista de número com json
# a função dumps converte para uma string
#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#lista_json = json.dumps(lista)
#print(lista_json, type(lista_json))

# convertendo um dicionário para string com json.dumps()
#dados_json = json.dumps(clientes_dicionario, indent=4)
#print(dados_json, type(dados_json))

# convertendo de json para um dicionário python
# usando a função json.loads()
#dicionario = json.loads(clientes_json)
#for chave, valor in dicionario.items():
#    print(chave)
#    print(valor)

with open('cliente.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)

with open('cliente.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)
