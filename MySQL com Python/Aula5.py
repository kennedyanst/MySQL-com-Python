import mysql.connector
from mysql.connector import Error
#INSERINDO DADOS POR MEIO DO "INPUT"!!
print("ROTINA ADMINISTRATIVA PARA CADASTRO DE PRODUTOS NO BANCO DE DADOS.")
print("Entre com os dados conforme solicitado.")

idProd = "DEFAULT"
nomeProd = input("Nome do Produto: ")
precoProd = input("Preço: ")
quantProd = input("Quatidade: ")

dados = idProd + ',\'' + nomeProd + '\',' + precoProd + ',' + quantProd + ');'
declaracao = """INSERT INTO produtos values(
"""
sql = declaracao + dados


try:
    #CRIANDO CONEXÃO AO BANCO DE DADOS
    con = mysql.connector.connect(host='localhost', database = "aula_mysql_python", user="root", password='')

    inserir_produtos = sql
    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit() #Commit = Finalizar uma transação, deixando ele permanente. 
    print(cursor.rowcount, "\033[1;32mRegistros inseridos na tabela com SUCESSO!\033[m")
    cursor.close()
except Error as erro:
    print(f"\033[1;31;4mFALHA!!! Não consegui inserir os dados na tabela MySQL: {erro}\033[m")
finally:
    if (con.is_connected()):
        con.close()
        print("\033[1;3;97mConexão ao MySQL FINALIZADA!\033[m")
        