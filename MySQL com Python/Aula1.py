import mysql.connector


#Colocar os dados de: Hospedagem= Meu computador, Banco de dados = Cadastro, Usuário = root, Senha = não tem.
con = mysql.connector.connect(host='localhost', database = "cadastro", user="root", password='')

if con.is_connected():# Se con for conectado execute: 
    db_info = con.get_server_info() #Informação do servidor
    print(f"Conectado ao seridor MSQL versão {db_info}.")
    cursor = con.cursor() #Objeto que permite fazer ação para os objetos de uma tabela retornavel
    cursor.execute("select database();") #COMANDO SQL QUE FOI DIFITADO LÁ. 
    linha = cursor.fetchone() #vá buscar uma linha
    print(f"Conectado ao banco de dados {linha}.")

if con.is_connected(): #Comando para fechar o servidor. 
    cursor.close()
    con.close()
    print ("A CONEXÃO AO MySQL FOI ENCERRADA!")