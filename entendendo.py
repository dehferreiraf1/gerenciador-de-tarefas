import tkinter as tk

class Interface:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Gerenciador de Tarefas")

        # Caixa de texto para a descrição da tarefa
        self.tarefa_entry = tk.Entry(self.janela, width=40)
        self.tarefa_entry.pack(pady=10)

        # Botão para adicionar a tarefa
        self.adicionar_button = tk.Button(self.janela, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.adicionar_button.pack(pady=10)

        self.janela.mainloop()

    def adicionar_tarefa(self):
        descricao = self.tarefa_entry.get()  # Pega o texto da caixa de entrada
        print(f"Tarefa adicionada: {descricao}")  # Exibe a descrição da tarefa no console

# Criando a interface
interface = Interface()
