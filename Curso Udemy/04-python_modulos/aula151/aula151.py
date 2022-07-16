# Stacks são estruturas de dados que podem ser usadas com listas, 
# ou seja, o último item a ser adicionado, é o primeiro a ser removido
'''
livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
print(livros)
livro_removido = livros.pop()
print(livros)
print(livro_removido)
'''

# Queue - o primeiro a ser adicionado é o primeiro a sair
# Não é interessante trabalhar com essa estrutura de dados com listas, devido
# a alteração dos índices, ou seja, ao remover o primeiro item de uma lista, 
# por exemplo, todos os outros são afetados por essa alteração

from collections import deque

fila = deque()  # é possível limitar o número de itens com o parâmetro 
                # maxlen=
# caso seja adicionado mais valores do que o maxlen definiu, os primeiros
# itens da lista serão removidos para a entrada dos novos dados
fila.append('Joãozinho')
fila.append('Maria')
fila.append('Andre')
fila.append('Marcos')
fila.append('José')
fila.popleft()
print(fila)
