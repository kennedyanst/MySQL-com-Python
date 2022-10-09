import mysql.connector
from mysql.connector import Error


try:
    #CRIANDO CONEXÃO AO BANCO DE DADOS
    con = mysql.connector.connect(host='localhost', database = "aula_mysql_python", user="root", password='')

    inserir_produtos = """INSERT INTO produtos values
                        (default, "Geladeira", "1700.00", "12"),
                        (default, "Sofá", "1080.50", "10"),
                        (default, "Fogão", "780.99", "21"),
                        (default, "Mesa", "990.50", "8"),
                        (default, "Teclado Gamer", "350.50", "15");
                        """
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
        