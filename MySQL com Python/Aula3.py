import mysql.connector
from mysql.connector import Error


try:
    #CRIANDO CONEXÃO AO BANCO DE DADOS
    con = mysql.connector.connect(host='localhost', database = "aula_mysql_python", user="root", password='')

    consulta_sql = "select*from produtos;"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall() #fetchall = Vá buscar TUDO!!
    print (f"\033[35mO número total de registros retornados foram: {cursor.rowcount}\033[m")

    print("\033[36m\nMostrando os autores cadastrados\033[m")
    for linha in linhas:
        print (f"\033[33mID do produto: {linha[0]}")
        print (f"\033[34mNome do Produto: {linha[1]}")
        print (f"\033[32mPreço: {linha[2]}")
        print (f"\033[31mQuatidade: {linha[3]}\033[m", "\n")


except Error as e:
    print(f"\033[31mERRO AO ACESSAR TABELA NO MYSQL {e}\033[m")
finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print("\033[36mConexão ao MySL encerrada!\033[m")