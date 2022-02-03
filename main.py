from tkinter import *
import mysql.connector
from tkinter import messagebox

"""
#construtor padrao da classe
#self.x pertence a todo escopo da classe

def __init__(self):
    self.x = 12
    print('O que está no construtor padrao')
    print(self.x)
def mostrar():
    print('Fora do construtor')

JanelaLogin()
JanelaLogin.mostrar()


"""


class JanelaLogin():

    def verificarLogin(self):
        autenticado = False
        usuarioMaster = False

        try:
            conexao = mysql.connector.connect(
                host='',
                user='lucas',
                password='12345',
                db='erp',
                charset='utf8mb4'
            )
        except:
            print('Erro ao conectar ao banco de dados')

        usuario = self.login.get()
        senha = self.password.get()



        try:
            with conexao.cursor() as cx:
                cx.execute('SELECT * from cadastros')
                ret = cx.fetchall()
        except:
            print('Erro ao fazer consulta')

        for line in ret:
            if usuario == line[0] and senha == line[1]:
                if line[2] == 1:
                    usuarioMaster = False
                elif line[2] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False

        if not autenticado:
            messagebox.showinfo('login', 'Email ou senha incorretos')

        if autenticado:
            self.root.destroy()

            if usuarioMaster:
                messagebox.showinfo('login', 'Usuário autenticado')

    def __init__(self):
        self.root = Tk()
        self.root.title('Login')
        # self.root.geometry('300x150')
        Label(self.root, text='Faça o login').grid(row=0, column=0, columnspan=2)

        Label(self.root, text='Usuario').grid(row=1, column=0)
        self.login = Entry(self.root)
        self.login.grid(row=1, column=1, padx=5, pady=5)

        Label(self.root, text='Senha').grid(row=2, column=0)
        self.password = Entry(self.root)
        self.password.grid(row=2, column=1, padx=5, pady=5)
        Button(self.root, text='Login', bg='green3', width=10, command=self.verificarLogin).grid(row=3, column=0,
                                                                                                   padx=5, pady=5)
        Button(self.root, text='Cadastrar', bg='orange3', width=10).grid(row=3, column=1, padx=5, pady=5)

        self.root.mainloop()


JanelaLogin()