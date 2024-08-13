import tkinter as tk

class Cliente:
    def __init__(self, nome):
        self.nome = nome

def adicionar_cliente():
    cliente = Cliente("Nome Teste")
    print(f"Cliente {cliente.nome} adicionado!")

def main():
    root = tk.Tk()
    root.title("Sistema de Cadastro")
    
    btn_adicionar = tk.Button(root, text="Adicionar Cliente", command=adicionar_cliente)
    btn_adicionar.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
