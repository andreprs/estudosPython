import pymysql.cursors
from contextlib import contextmanager

# CRUD - CREATE, READ, UPDATE, DELETE


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        database='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:  # Resolvendo a questão de esquecer de fechar a base de dados
        yield conexao
    finally:
        conexao.close()

# with conexao.cursor() as cursor:
#     cursor.execute('SELECT nome, sobrenome FROM clientes LIMIT 100')
#     resultado = cursor.fetchall()
#     for linha in resultado:
#         print(linha['nome'], linha['sobrenome'])


# INSERE UM REGISTRO NA BASE DE DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
              '(%s, %s, %s, %s)'
        cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
        # conexao.commit()

# INSERE VÁRIOS REGISTROS NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
#               '(%s, %s, %s, %s)'
#
#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('ROSE', 'FIGUEIREDO', 19, 55),
#             ('JOSÉ', 'FIGUEIREDO', 19, 55),
#         ]
#
#         cursor.executemany(sql, dados)
#         conexao.commit()

# DELETA UM REGISTRO DA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         conexao.commit()

# DELETA VÁRIOS REGISTRO DA BASE DE DADOS  (EM RANGE)
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (1, 4))
#         conexao.commit()

# ATUALIZA UM DOS REGISTROS NA BASE DE DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('JOANA', 5))
        conexao.commit()

# ESTE SELECIONA OS DADOS DA BASE DE DADOS
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha)
