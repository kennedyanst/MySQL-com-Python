import mysql.connector

try:
    #CRIANDO CONEXÃO AO BANCO DE DADOS
    con = mysql.connector.connect(host='localhost', database = "cadastro", user="root", password='')

    #DECLARAÇÃO SQL A SER EXECUTADA
    tabela_MySQL = """ USE aula_mysql_python;
                    CREATE TABLE produtos
                    (
                    idProduto int(11) NOT NULL AUTO_INCREMENT,
                    Nome_Produto VARCHAR(40) NOT NULL,
                    Preço FLOAT NOT NULL,
                    Quantidade TINYINT NOT NULL,
                    PRIMARY KEY (idProduto)
                    ) default charset = utf8;"""
                   
    # CRIAR CURSOSR E EXECUTAR SQL NO BANCO DE DADOS
    cursor = con.cursor()
    cursor.execute(tabela_MySQL)
    print(f"\033[1;32mTabela de Produtos criada com sucesso!\033[m")

except mysql.connector.Error as erro:
    print(f"\033[1;31m FALHA!! A tabela não foi criada por causa do erro {erro}\033[m")

finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print (f"\033[1;30;107mCONEÇÃO AO MySQL FINALIZADA!!\033[m")
