import tkinter as tk

class Cliente:
    def __init__(self, id_cliente, nome):
        self.id_cliente = id_cliente
        self.nome = nome

clientes = {}

def adicionar_cliente():
    id_cliente = "001"
    nome = "Cliente Teste"
    cliente = Cliente(id_cliente, nome)
    clientes[cliente.id_cliente] = cliente
    print(f"Cliente {cliente.nome} adicionado!")

def main():
    root = tk.Tk()
    root.title("Sistema de Cadastro")
    
    btn_adicionar = tk.Button(root, text="Adicionar Cliente", command=adicionar_cliente)
    btn_adicionar.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
