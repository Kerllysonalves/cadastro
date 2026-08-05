import tkinter as tk
from cadastro import abrir_cadastro
#Janela

igrejApp = tk.Tk()
igrejApp.title("IgrejApp")
igrejApp.geometry("400x650")
#igrejApp.resizable(False, False)

largura = 400
altura = 350

#Centralizar janela

largura_tela = igrejApp.winfo_screenwidth()
altura_tela = igrejApp.winfo_screenheight()

x = (largura_tela - largura) // 2 - (largura // 2)
y = (altura_tela - altura) // 2 - (altura // 2)

igrejApp.geometry(f"400x650+{x}+{y}")
igrejApp.config(bg="#f4f6f9")

#Titulo

titulo = tk.Label(
    igrejApp,
    text="IgrejApp",
    font=("Segoe UI", 22, "bold"),
    bg="#f4f6f9",
    fg="#1f4e79"
)
titulo.pack(pady=40, padx=10)

substituto = tk.Label(
    igrejApp,
    text="Faça seu login",
    font=("Segoe UI", 11),
    bg="#f4f6f9",
    fg="gray"
)
substituto.pack(pady=0, padx=30)

#Frame

frame = tk.Frame(
    igrejApp,
    bg="white",
    bd=1,
    relief="solid",
    padx=30,
    pady=25
)
frame.pack()



#Usuário"

tk.Label(
    frame,
    text="Usuário:",
    font=("Segoe UI", 11, "bold"),
    bg="white"
).pack(anchor="w")


entry_usuario = tk.Entry(
    frame,
    font=("Segoe UI", 12),
    width=30
)
entry_usuario.pack(pady=5)

#Senha
lbl_senha = tk.Label(
    frame,
    text="Senha:",
    font=("Segoe UI", 11, "bold"),
    bg="white"
)

lbl_senha.pack(pady=5)

entry_senha = tk.Entry(
    frame,
    font=("Segoe UI", 12),
    width=30,
    show="*"
)
entry_senha.pack(pady=5)

#Botão de login

btn_login = tk.Button(
    igrejApp,
    text="Login",
    cursor="hand2",
    font=("Segoe UI", 12),
    width=10,
    command=lambda: print("Login realizado!")
)
btn_login.pack(pady=10)


lbl_cadastro = tk.Label(
    igrejApp,
    text="Não possui uma conta?",
    font=("Segoe UI", 10),
    bg="#f4f6f9",
    fg="gray"
)
lbl_cadastro.pack(pady=(10, 2))

#Botão de cadastro

btn_cadastro = tk.Button(
    igrejApp,
    text="Cadastrar",
    cursor="hand2",
    font=("Segoe UI", 12),
    width=10,
    command=abrir_cadastro
)


btn_cadastro.pack(pady=10)



igrejApp.mainloop()