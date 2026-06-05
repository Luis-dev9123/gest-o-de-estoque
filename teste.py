import customtkinter as ctk

app = ctk.CTk()
app.geometry("600x400")

# Função para mostrar a tela 1
def abrir_tela1():
    frame_tela2.pack_forget()
    frame_tela1.pack(fill="both", expand=True)

# Função para mostrar a tela 2
def abrir_tela2():
    frame_tela1.pack_forget()
    frame_tela2.pack(fill="both", expand=True)

# Tela 1
frame_tela1 = ctk.CTkFrame(app)

label1 = ctk.CTkLabel(
    frame_tela1,
    text="Bem-vindo",
    font=("Arial", 24, "bold")
)
label1.pack(pady=20)

botao1 = ctk.CTkButton(
    frame_tela1,
    text="Fazer Login",
    command=abrir_tela2
)
botao1.pack()

# Tela 2
frame_tela2 = ctk.CTkFrame(app)

label2 = ctk.CTkLabel(
    frame_tela2,
    text="Tela de Estoque"
)
label2.pack(pady=20)

botao2 = ctk.CTkButton(
    frame_tela2,
    text="Voltar",
    command=abrir_tela1
)
botao2.pack()

# Tela inicial
frame_tela1.pack(fill="both", expand=True)

app.mainloop()