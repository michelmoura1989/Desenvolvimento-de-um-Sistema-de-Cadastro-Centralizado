import tkinter as tk

class Cliente:
    def __init__(self, id_cliente, nome):
        self.id_cliente = id_cliente
        self.nome = nome

clientes = {}

def adicionar_cliente():
    id_cliente = entry_id.get()
    nome = entry_nome.get()
    cliente = Cliente(id_cliente, nome)
    clientes[cliente.id_cliente] = cliente
    print(f"Cliente {cliente.nome} adicionado!")

def main():
    global entry_id, entry_nome

    root = tk.Tk()
    root.title("Sistema de Cadastro")
    
    tk.Label(root, text="ID do Cliente").pack()
    entry_id = tk.Entry(root)
    entry_id.pack()
    
    tk.Label(root, text="Nome do Cliente").pack()
    entry_nome = tk.Entry(root)
    entry_nome.pack()

    btn_adicionar = tk.Button(root, text="Adicionar Cliente", command=adicionar_cliente)
    btn_adicionar.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
