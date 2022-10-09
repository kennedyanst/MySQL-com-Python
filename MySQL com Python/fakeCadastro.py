#PREENCHENDO UMA TABELA NO MYSQL COM CADASTROS FAKES.

from faker import Faker
import mysql.connector
from mysql.connector import Error


fake = Faker(locale="pt-br")

try:
    #CRIANDO CONEXÃO AO BANCO DE DADOS
    con = mysql.connector.connect(host='localhost', database = "cadastro", user="root", password='')
    cursor = con.cursor()


    inserir_dados = """INSERT INTO gafanhotos
                            (nome, prof, nascimento)
                        VALUES 
                            ('{}', '{}', '{}');
                        """

    for i in range(22):
        prof = fake.job()
        nome = fake.name()
        nascimento = fake.date()
        sql = inserir_dados.format(nome, prof, nascimento) 
        print (sql)
        cursor.execute(sql)


    cursor = con.cursor()   
    con.commit() #Commit = Finalizar uma transação, deixando ele permanente. 
    print(cursor.rowcount, "\033[1;32mRegistros inseridos na tabela com SUCESSO!\033[m")
    cursor.close()
except Error as erro:
    print(f"\033[1;31;4mFALHA!!! Não consegui inserir os dados na tabela MySQL: {erro}\033[m")
finally:
    if (con.is_connected()):
        con.close()
        print("\033[1;3;97mConexão ao MySQL FINALIZADA!\033[m")