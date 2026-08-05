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

   
