import tkinter as tk
from tkinter import ttk


#Função ue abre a tela de cadastro
def abrir_cadastro():
    cadastro = tk.Toplevel()
    cadastro.title("Cadastro")
    cadastro.geometry("400x650")
    cadastro.config(bg="#f4f6f9")

#Título

    titulo = tk.Label(
        cadastro,
        text="Cadastro",
        font=("Segoe UI", 22, "bold"),
        bg="#f4f6f9",
        fg="#1f4e79"
)
    titulo.pack(pady=20)

    #nome
    tk.Label(
        cadastro,   
        text="Nome completo",
        bg="#f4f6f9",font=("Segoe UI", 11),
    ).pack(anchor="w", padx=50)

    entry_nome = tk.Entry(
        cadastro,
        font=("Segoe UI", 11),
        width=40
    )
    entry_nome.pack(pady=5)

    #Usuário
    tk.Label(
        cadastro,
        text="Usuário",
        bg="#f4f6f9",font=("Segoe UI", 11),
    ).pack(anchor="w", padx=50)

    entry_usuario = tk.Entry(
        cadastro,
        font=("Segoe UI", 11),
        width=40
    )
    entry_usuario.pack(pady=5)

    #Senha
    tk.Label(
        cadastro,
        text="Senha",
        bg="#f4f6f9",font=("Segoe UI", 11),
    ).pack(anchor="w", padx=50)

    entry_senha = tk.Entry(
        cadastro,
        font=("Segoe UI", 11),
        width=40,
        show="*"
    )
    entry_senha.pack(pady=5)

#Confirmar senha
    tk.Label(
        cadastro,
        text="Confirmar Senha",
        bg="#f4f6f9",font=("Segoe UI", 11),
    ).pack(anchor="w", padx=50)

    entry_confirmar_senha = tk.Entry(
        cadastro,
        font=("Segoe UI", 11),
        width=40,
        show="*"
    )
    entry_confirmar_senha.pack(pady=5)

#Cargo

    tk.Label(
        cadastro,
        text="Cargo",
        bg="#f4f6f9",font=("Segoe UI", 11),
    ).pack(anchor="w", padx=50)

    cargos = [
        "Administrador",
        "Pastor",
        "Recepção",
        "Mídia",
        "Tesoureiro"
    ]

    combo_cargo = ttk.Combobox(
        cadastro,
        values=cargos,
        width=37,
        state="readdonly"
    )

    combo_cargo.current(0)
    combo_cargo.pack(pady=5)

#Botões

    frame_botoes = tk.Frame(cadastro, bg="#f4f6f9")
    frame_botoes.pack(pady=30)

    btn_salvar = tk.Button(
        frame_botoes,
        text="Salvar",
        width=15,
        bg="#198754",
        fg="white",
        font=("Segoe UI", 10, "bold")
)
    btn_salvar.grid(row=0, column=0, padx=10)

    btn_cancelar = tk.Button(
        frame_botoes,
        text="Cancelar",
        width=15,
        bg="#dc3545",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        command=cadastro.destroy
)

    btn_cancelar.grid(row=0, column=1, padx=10)