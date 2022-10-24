from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from conexao import criar_conexao,fechar_conexao
from database import insere_usuario,LoginUsuario
 

con = criar_conexao("localhost","root","admin","python")
cursor = con.cursor()
#criar janela=tela-----------------------------------------
janela = Tk()
#definir titulo
janela.title("Mão na Roda")
#tamanho da tela
janela.geometry("600x300")
#cor do fundo da janela
janela.configure(background="black")
#definir tamanho fixo da tela
janela.resizable(width=False, height=False)
#carregar icons
janela.iconbitmap(default='pngs/icon.ico')
#carregar imagem
logo = PhotoImage(file='pngs/iconsRoda.png')
#criar widht---------------------------------------------------------------
#criar elemento em uma parte da tela
LeftFrame = Frame(janela,width=200, height=300, bg='MIDNIGHTBLUE', relief='raise')
#aparecer o frame criado no lado desejado
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janela,width=395, height=300, bg='MIDNIGHTBLUE', relief='raise')
RightFrame.pack(side=RIGHT)
#criar labels---------------------------------------------------------------------------
#criar label para o icon
LogoLabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
#posicionar label
LogoLabel.place(x=1,y=20)
#criar label titulo
MRDLabel = Label(RightFrame, text="Mão na Roda",font=('Century Gothic',30),bg='Midnightblue', fg='White')
MRDLabel.place(x=65,y=20)
#criar label login
UserLabel = Label(RightFrame, text="Login:",font=('Century Gothic',18),bg='MIDNIGHTBLUE', fg='White')
UserLabel.place(x=20,y=100)
UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=120,y=110)
#criar label senha
SenhaLabel = Label(RightFrame, text="Senha:",font=('Century Gothic',18),bg='MIDNIGHTBLUE',fg='White')
SenhaLabel.place(x=20,y=140)
SenhaEntry =  ttk.Entry(RightFrame,width=30, show='•')
SenhaEntry.place(x=120,y=150)

def Login():
    Login = UserEntry.get()
    Senha = SenhaEntry.get()
    con = criar_conexao("localhost","root","admin","python")
    cursor = con.cursor()
    sql = "select * from login_usuario "
    cursor.execute(sql)
    VerificaLogin = cursor.fetchone()
    try:
        if(Login in VerificaLogin and Senha in VerificaLogin):
            messagebox.showinfo(title="Login Realizado",message="O Login Foi Realizado Com Sucesso. Seja Bem Vindo")
            print('3')
        else:
            pass
    except:
            messagebox.showerror(title="Login info",message="Acesso negado, verifique suas informações")
            print('2')
    print('1')
    cursor.close
    fechar_conexao(con)
#Criar botão entrar
LoginButton = ttk.Button(RightFrame,text='Entrar',width=20, command=Login)
LoginButton.place(x=150,y=205)

#criar função pro botão registrar
def Register():
    #sumirbotões
    LoginButton.place(x=601)
    RegisterBtn.place(x=601)
    MRDLabel.place(x=601)
    #criar cadastro
    NomeLabel = Label(RightFrame, text='Nome:',font=('Century Gothic',18),bg='MIDNIGHTBLUE', fg='White')
    NomeLabel.place(x=20,y=20)

    NomeEntry = ttk.Entry(RightFrame,width=30)
    NomeEntry.place(x=120,y=30)

    EmailLabel = Label(RightFrame, text='Email:',font=('Century Gothic',18),bg='MIDNIGHTBLUE', fg='White')
    EmailLabel.place(x=20,y=60)

    EmailEntry = ttk.Entry(RightFrame,width=30)
    EmailEntry.place(x=120,y=70)

    def RegisterToDataBase():
        #definindo variaveis do banco
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        Login = UserEntry.get()
        Senha = SenhaEntry.get()
        #inserindo no banco
        if (Name == "" or Email == "" or Login == "" or Senha == ""):
            messagebox.showerror(title="Erro no cadastro", message="Todos os Campos Devem Ser Preenchidos.")
        else:
            insere_usuario(con,Name,Email,Login,Senha)
            messagebox.showinfo(title="Informações de registro", message="Registro concluido!")

    RegisterButton = ttk.Button(RightFrame,text='Registrar',width=20, command=RegisterToDataBase )
    RegisterButton.place(x=150,y=200)
    def BackToLogin():
        #refazer a tela de login
        MRDLabel.place(x=65)
        NomeLabel.place(x=601)
        NomeEntry.place(x=601)
        EmailLabel.place(x=601)
        EmailEntry.place(x=601)
        Backbtn.place(x=601)
        RegisterButton.place(x=601)
        RegisterBtn.place(x=165)
        LoginButton.place(x=150)
    Backbtn = ttk.Button(RightFrame,text='Voltar',width=15, command=BackToLogin)
    Backbtn.place(x=20,y=250)

#Botão registrar
RegisterBtn = ttk.Button(RightFrame,text='Registrar',width=15, command=Register)
RegisterBtn.place(x=165,y=235)



#finalizar janela
janela.mainloop()