import tkinter as tk
from tkinter import messagebox

# Classe para representar um equipamento
class Equipamento:
    def __init__(self, id_equipamento, nome, tipo, data_aquisicao, numero_serie, fabricante, modelo):
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.tipo = tipo
        self.data_aquisicao = data_aquisicao
        self.numero_serie = numero_serie
        self.fabricante = fabricante
        self.modelo = modelo

# Classe para representar um cliente
class Cliente:
    def __init__(self, id_cliente, nome, telefone, email):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.email = email

# Classe para gerenciar o sistema de cadastro
class SistemaCadastro:
    def __init__(self):
        self.clientes = {}
        self.equipamentos = {}

    def adicionar_cliente(self, cliente):
        self.clientes[cliente.id_cliente] = cliente
        messagebox.showinfo("Sucesso", f"Cliente {cliente.nome} adicionado com sucesso!")

    def adicionar_equipamento(self, equipamento):
        self.equipamentos[equipamento.id_equipamento] = equipamento
        messagebox.showinfo("Sucesso", f"Equipamento {equipamento.nome} adicionado com sucesso!")

    def visualizar_clientes(self):
        if not self.clientes:
            messagebox.showinfo("Clientes", "Nenhum cliente cadastrado.")
            return
        clientes_str = "\n".join([f"ID: {cliente.id_cliente}, Nome: {cliente.nome}, Telefone: {cliente.telefone}, Email: {cliente.email}" for cliente in self.clientes.values()])
        messagebox.showinfo("Clientes", clientes_str)

    def visualizar_equipamentos(self):
        if not self.equipamentos:
            messagebox.showinfo("Equipamentos", "Nenhum equipamento cadastrado.")
            return
        equipamentos_str = "\n".join([f"ID: {equipamento.id_equipamento}, Nome: {equipamento.nome}, Tipo: {equipamento.tipo}, Data de Aquisição: {equipamento.data_aquisicao}, Número de Série: {equipamento.numero_serie}, Fabricante: {equipamento.fabricante}, Modelo: {equipamento.modelo}" for equipamento in self.equipamentos.values()])
        messagebox.showinfo("Equipamentos", equipamentos_str)

    def remover_cliente(self, id_cliente):
        if id_cliente in self.clientes:
            del self.clientes[id_cliente]
            messagebox.showinfo("Sucesso", f"Cliente com ID {id_cliente} removido com sucesso!")
        else:
            messagebox.showerror("Erro", "Cliente não encontrado.")

    def remover_equipamento(self, id_equipamento):
        if id_equipamento in self.equipamentos:
            del self.equipamentos[id_equipamento]
            messagebox.showinfo("Sucesso", f"Equipamento com ID {id_equipamento} removido com sucesso!")
        else:
            messagebox.showerror("Erro", "Equipamento não encontrado.")

# Função para criar a janela principal
def main():
    sistema = SistemaCadastro()

    root = tk.Tk()
    root.title("Sistema de Cadastro de Manutenção de Equipamentos")

    # Adiciona o nome da empresa
    label_empresa = tk.Label(root, text="Gtec", font=("Helvetica", 16, "bold"))
    label_empresa.pack(pady=10)

    # Funções de interface gráfica
    def adicionar_cliente():
        id_cliente = entry_id_cliente.get()
        nome = entry_nome_cliente.get()
        telefone = entry_telefone_cliente.get()
        email = entry_email_cliente.get()
        cliente = Cliente(id_cliente, nome, telefone, email)
        sistema.adicionar_cliente(cliente)

    def adicionar_equipamento():
        id_equipamento = entry_id_equipamento.get()
        nome = entry_nome_equipamento.get()
        tipo = entry_tipo_equipamento.get()
        data_aquisicao = entry_data_aquisicao.get()
        numero_serie = entry_numero_serie.get()
        fabricante = entry_fabricante.get()
        modelo = entry_modelo.get()
        equipamento = Equipamento(id_equipamento, nome, tipo, data_aquisicao, numero_serie, fabricante, modelo)
        sistema.adicionar_equipamento(equipamento)

    def remover_cliente():
        id_cliente = entry_id_cliente_remover.get()
        sistema.remover_cliente(id_cliente)

    def remover_equipamento():
        id_equipamento = entry_id_equipamento_remover.get()
        sistema.remover_equipamento(id_equipamento)

    # Elementos da interface gráfica
    frame_cliente = tk.Frame(root)
    frame_cliente.pack(pady=10)

    tk.Label(frame_cliente, text="ID do Cliente").grid(row=0, column=0)
    entry_id_cliente = tk.Entry(frame_cliente)
    entry_id_cliente.grid(row=0, column=1)

    tk.Label(frame_cliente, text="Nome do Cliente").grid(row=1, column=0)
    entry_nome_cliente = tk.Entry(frame_cliente)
    entry_nome_cliente.grid(row=1, column=1)

    tk.Label(frame_cliente, text="Telefone do Cliente").grid(row=2, column=0)
    entry_telefone_cliente = tk.Entry(frame_cliente)
    entry_telefone_cliente.grid(row=2, column=1)

    tk.Label(frame_cliente, text="Email do Cliente").grid(row=3, column=0)
    entry_email_cliente = tk.Entry(frame_cliente)
    entry_email_cliente.grid(row=3, column=1)

    tk.Button(frame_cliente, text="Adicionar Cliente", command=adicionar_cliente).grid(row=4, column=0, columnspan=2, pady=10)

    frame_equipamento = tk.Frame(root)
    frame_equipamento.pack(pady=10)

    tk.Label(frame_equipamento, text="ID do Equipamento").grid(row=0, column=0)
    entry_id_equipamento = tk.Entry(frame_equipamento)
    entry_id_equipamento.grid(row=0, column=1)

    tk.Label(frame_equipamento, text="Nome do Equipamento").grid(row=1, column=0)
    entry_nome_equipamento = tk.Entry(frame_equipamento)
    entry_nome_equipamento.grid(row=1, column=1)

    tk.Label(frame_equipamento, text="Tipo do Equipamento").grid(row=2, column=0)
    entry_tipo_equipamento = tk.Entry(frame_equipamento)
    entry_tipo_equipamento.grid(row=2, column=1)

    tk.Label(frame_equipamento, text="Data de Aquisição").grid(row=3, column=0)
    entry_data_aquisicao = tk.Entry(frame_equipamento)
    entry_data_aquisicao.grid(row=3, column=1)

    tk.Label(frame_equipamento, text="Número de Série").grid(row=4, column=0)
    entry_numero_serie = tk.Entry(frame_equipamento)
    entry_numero_serie.grid(row=4, column=1)

    tk.Label(frame_equipamento, text="Fabricante").grid(row=5, column=0)
    entry_fabricante = tk.Entry(frame_equipamento)
    entry_fabricante.grid(row=5, column=1)

    tk.Label(frame_equipamento, text="Modelo").grid(row=6, column=0)
    entry_modelo = tk.Entry(frame_equipamento)
    entry_modelo.grid(row=6, column=1)

    tk.Button(frame_equipamento, text="Adicionar Equipamento", command=adicionar_equipamento).grid(row=7, column=0, columnspan=2, pady=10)

    frame_visualizar = tk.Frame(root)
    frame_visualizar.pack(pady=10)

    tk.Button(frame_visualizar, text="Visualizar Clientes", command=sistema.visualizar_clientes).pack(side=tk.LEFT, padx=10)
    tk.Button(frame_visualizar, text="Visualizar Equipamentos", command=sistema.visualizar_equipamentos).pack(side=tk.LEFT, padx=10)

    frame_remover = tk.Frame(root)
    frame_remover.pack(pady=10)

    tk.Label(frame_remover, text="ID do Cliente a remover").grid(row=0, column=0)
    entry_id_cliente_remover = tk.Entry(frame_remover)
    entry_id_cliente_remover.grid(row=0, column=1)

    tk.Button(frame_remover, text="Remover Cliente", command=remover_cliente).grid(row=1, column=0, columnspan=2, pady=10)

    tk.Label(frame_remover, text="ID do Equipamento a remover").grid(row=2, column=0)
    entry_id_equipamento_remover = tk.Entry(frame_remover)
    entry_id_equipamento_remover.grid(row=2, column=1)

    tk.Button(frame_remover, text="Remover Equipamento", command=remover_equipamento).grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
