import tkinter as tk

def adicionar_cliente():
    print("Cliente adicionado!")

def main():
    root = tk.Tk()
    root.title("Sistema de Cadastro")
    
    btn_adicionar = tk.Button(root, text="Adicionar Cliente", command=adicionar_cliente)
    btn_adicionar.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
