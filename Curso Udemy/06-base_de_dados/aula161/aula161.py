import sqlite3

conexao = sqlite3.connect('base_de_dados.db')
cursor = conexao.cursor()


# Checando se uma tabela já existe e caso não, ela será criada.
# Apenas entendendo como fazer isso em python, mas na prática esse processo
# é feito através de softwares GUI mesmo.
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT,'
    'peso REAL'
    ')')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', 
#                ('Maria', 50))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', 
#                {'nome': 'Joãozinho', 'peso': 48})
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', 
#                {'id': None, 'nome': 'Daniel', 'peso': 98})
#conexao.commit()

# cursor.execute('UPDATE clientes  SET nome=:nome WHERE id=:id',
#                {'nome': 'Joana', 'id': 2})
# conexao.commit()

# cursor.execute('DELETE FROM clientes WHERE id=:id', {'id': 2})
# conexao.commit()

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',
               {'peso': 70})
for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso)

cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    identificador, nome, peso = linha
    print(identificador, nome, peso)

cursor.close()
conexao.close()
