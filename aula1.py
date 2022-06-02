import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='07022109Ju+',
    database='bdyoutube',
)

cursor = conexao.cursor()

# CRUD
###
# comando = ''
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados {usar quando o comando for de escrita}
# resultado = cursor.fetchall() # le do banco de dados e armazena em "resultado" {usar quando o comando for de leitura}
##

# C
def SQL_CREATE_PRODUTO(nome_produto, valor):
    insert = f'INSERT INTO Vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor});'
    cursor.execute(insert)
    conexao.commit()

# R
def SQL_READ_PRODUTO(nome_produto):
    select = f'SELECT * FROM Vendas WHERE nome_produto="{nome_produto}"'
    cursor.execute(select)
    resultado = cursor.fetchall()
    return resultado

# U
def SQL_UPDATE_VALOR_PRODUTO(nome_produto, valor):
    update = f'UPDATE Vendas SET valor = {valor} WHERE nome_produto="{nome_produto}"'
    cursor.execute(update)
    conexao.commit()

# D
def SQL_DELETE_PRODUTO(nome_produto):
    delete = f'DELETE FROM Vendas WHERE nome_produto="{nome_produto}"'
    cursor.execute(delete)
    conexao.commit()



# variaveis
# so precisa ir alterando aqui toda vez q for querer alterar o banco
nome_produto = 'Todynho'
valor = 6


# testes

# C
# SQL_CREATE_PRODUTO(nome_produto, valor)

# R
# busca = SQL_READ_PRODUTO(nome_produto)
# print(f'index: {busca[0][0]}; nome do produto: {busca[0][1]}; valor: {busca[0][2]}')

# U
# SQL_UPDATE_VALOR_PRODUTO(nome_produto, valor)

# D
SQL_DELETE_PRODUTO(nome_produto)

cursor.close()
conexao.close()

