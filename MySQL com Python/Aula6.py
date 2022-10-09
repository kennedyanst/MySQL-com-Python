#ATUALIZAÇÃO DE BANCO DE DADOS

import mysql.connector 
from mysql.connector import Error

go = ";"
def conectar():
    try:
        global con
        con = mysql.connector.connect(host="localhost", 
                                      database="aula_mysql_python", 
                                      user="root", 
                                      password="")
    except Error as erro:
        print(f"Erro de coneção {erro}")


def consulta(idProd):
    try:
        conectar()
        consulta_sql = """select * from produtos 
                          WHERE idProduto = """ + idProd + go
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print(f"Id: {linha[0]}")
            print(f"Produto: {linha[1]}")
            print(f"Preço: {linha[2]}")
    except Error as erro:
        print(f"Falha ao consultar a tabela: {erro}")
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()

def atualiza (declaracao):
    try:
        conectar()
        altera_preco = declaracao
        cursor = con.cursor()
        cursor.execute(altera_preco)
        con.commit()
        print("Preço alterado com SUCESSO!!")
    except Error as erro:
        print(f"Falha ao inserir dados na tabela: {erro}")
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()
    

if __name__ == "__main__":
    print("Atualizar preço de produtos no banco de dados.")
    print("Entre com os dados conforme solicitado:")

    print("\nDigite o código do produto a alterar:")
    idProd = input("Id do produto: ")

    consulta(idProd)

    print("\nEntre com o novo preço do produto:")
    precoProd = input("Preço: ")

    declaracao = """UPDATE produtos
    SET Preço = """ + precoProd + """
    WHERE idProduto = """ + idProd + go

    atualiza(declaracao)

    verifica = input("\n Deseja consultar a atualização? s = Sim, n = Não: ")
    if verifica == "s":
        consulta(idProd)
    else:
        print("Até mais!!")
print("VOLTE SEMPRE!")