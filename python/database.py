from conexao import criar_conexao, fechar_conexao


print("Conectado ao banco")

#função para criar usuarios novos no sistema
def insere_usuario(con, nome, email, login, senha):
    cursor = con.cursor()
    sql = "INSERT INTO cadastro (nome,email,login,senha) values (%s,%s,%s,%s)"
    valores = (nome,email,login,senha)
    cursor.execute(sql,valores)
    cursor.close()
    con.commit()
    fechar_conexao(con)
#função para ver todos os usuarios
def select_todos_usuarios(con):
    cursor = con.cursor()
    sql ="select id_usuario,nome,email,login FROM cadastro"
    cursor.execute(sql)

    for(id_usuario,nome,email) in cursor:
        print(id_usuario,nome,email)
    cursor.close
    fechar_conexao(con)

def LoginUsuario(con,login,senha):
    con = criar_conexao("localhost","root","admin","python")
    cursor = con.cursor()
    sql = "select * from login_usuario"
    cursor.execute(sql)
    cursor.close
    fechar_conexao(con)
def main():
    con = criar_conexao("localhost","root","admin","python")
    #insere_usuario(con,"bill","bill@hotmail.com","bill123")
    #select_todos_usuarios(con)
    fechar_conexao(con)

if __name__ == "__main__":
    main()
