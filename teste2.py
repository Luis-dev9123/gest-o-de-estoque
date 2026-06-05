import customtkinter as ctk

# Configurações iniciais
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
app = ctk.CTk()
app.title("Gestor de Estoque")
app.geometry("1000x600")

# Configuração do grid
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

# Frame lateral
frame_menu = ctk.CTkFrame(app, width=200)
frame_menu.grid(row=0, column=0, sticky="ns")

# Título do menu
titulo = ctk.CTkLabel(
    frame_menu,
    text="ESTOQUE",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=20)

# Botões do menu
btn_produtos = ctk.CTkButton(
    frame_menu,
    text="Produtos"
)
btn_produtos.pack(padx=10, pady=5)

btn_entradas = ctk.CTkButton(
    frame_menu,
    text="Entradas"
)
btn_entradas.pack(padx=10, pady=5)

btn_saidas = ctk.CTkButton(
    frame_menu,
    text="Saídas"
)
btn_saidas.pack(padx=10, pady=5)

# Frame principal
frame_principal = ctk.CTkFrame(app)
frame_principal.grid(
    row=0,
    column=1,
    sticky="nsew",
    padx=10,
    pady=10
)

# Título principal
lbl_titulo = ctk.CTkLabel(
    frame_principal,
    text="Cadastro de Produtos",
    font=("Arial", 22, "bold")
)
lbl_titulo.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=20
)

# Campo Nome
lbl_nome = ctk.CTkLabel(
    frame_principal,
    text="Nome do Produto:"
)
lbl_nome.grid(row=1, column=0, padx=10, pady=10)

entry_nome = ctk.CTkEntry(
    frame_principal,
    width=300
)
entry_nome.grid(row=1, column=1, padx=10, pady=10)

# Campo Quantidade
lbl_quantidade = ctk.CTkLabel(
    frame_principal,
    text="Quantidade:"
)
lbl_quantidade.grid(row=2, column=0, padx=10, pady=10)

entry_quantidade = ctk.CTkEntry(
    frame_principal,
    width=300
)
entry_quantidade.grid(row=2, column=1, padx=10, pady=10)

# Campo Preço
lbl_preco = ctk.CTkLabel(
    frame_principal,
    text="Preço:"
)
lbl_preco.grid(row=3, column=0, padx=10, pady=10)

entry_preco = ctk.CTkEntry(
    frame_principal,
    width=300
)
entry_preco.grid(row=3, column=1, padx=10, pady=10)

# Botão salvar
btn_salvar = ctk.CTkButton(
    frame_principal,
    text="Salvar Produto"
)
btn_salvar.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=20
)

app.mainloop()