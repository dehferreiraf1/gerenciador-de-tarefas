import tkinter as tk

# Classe para Tarefa
class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True

    def __str__(self):
        return f"{'[Concluída]' if self.concluida else '[Pendente]'} {self.descricao}"

# Classe para Gerenciador de Tarefas
class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        tarefa = Tarefa(descricao)
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        return [str(tarefa) for tarefa in self.tarefas]

    def marcar_concluida(self, tarefa):
        tarefa.marcar_concluida()

    def salvar_tarefas(self):
        with open("tarefas.txt", "w") as f:
            for tarefa in self.tarefas:
                f.write(f"{'1' if tarefa.concluida else '0'} {tarefa.descricao}\n")

    def carregar_tarefas(self):
        try:
            with open("tarefas.txt", "r") as f:
                for linha in f:
                    status, descricao = linha.strip().split(" ", 1)
                    tarefa = Tarefa(descricao)
                    if status == '1':
                        tarefa.marcar_concluida()
                    self.tarefas.append(tarefa)
        except FileNotFoundError:
            pass

# Classe para a Interface Gráfica com Tkinter
class Interface:
    def __init__(self, gerenciador):
        self.janela = tk.Tk()  # Cria a janela principal
        self.janela.title("Gerenciador de Tarefas")  # Define o título da janela

        self.gerenciador = gerenciador

        # Caixa de texto para o usuário digitar a descrição da tarefa
        self.tarefa_entry = tk.Entry(self.janela, width=40)
        self.tarefa_entry.pack()

        # Botão para adicionar a tarefa
        self.adicionar_button = tk.Button(self.janela, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.adicionar_button.pack()

        # Listbox para exibir as tarefas
        self.lista_tarefas = tk.Listbox(self.janela, width=50, height=10)
        self.lista_tarefas.pack()

        # Botão para marcar uma tarefa como concluída
        self.marcar_concluida_button = tk.Button(self.janela, text="Marcar como Concluída", command=self.marcar_concluida)
        self.marcar_concluida_button.pack()

        self.atualizar_lista()

        # Evento de fechamento da janela
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar_programa)

    def adicionar_tarefa(self):
        descricao = self.tarefa_entry.get()  # Pega o texto digitado
        if descricao:  # Verifica se não está vazio
            self.gerenciador.adicionar_tarefa(descricao)  # Adiciona a tarefa ao gerenciador
            self.atualizar_lista()  # Atualiza a lista na interface
        self.tarefa_entry.delete(0, tk.END)  # Limpa a caixa de texto após adicionar

    def marcar_concluida(self):
        tarefa_selecionada_index = self.lista_tarefas.curselection()

        if tarefa_selecionada_index:
            # Pegar o índice da tarefa selecionada
            tarefa_selecionada = self.lista_tarefas.get(tarefa_selecionada_index)

            # Encontrar a tarefa no gerenciador de tarefas
            for tarefa in self.gerenciador.tarefas:
                if str(tarefa) == tarefa_selecionada:
                    self.gerenciador.marcar_concluida(tarefa)  # Marcar a tarefa como concluída
                    break

            # Atualizar a lista de tarefas na interface
            self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_tarefas.delete(0, tk.END)  # Limpa a lista antes de adicionar novos itens
        for tarefa in self.gerenciador.listar_tarefas():
            self.lista_tarefas.insert(tk.END, tarefa)  # Adiciona cada tarefa ao Listbox

    def fechar_programa(self):
        self.gerenciador.salvar_tarefas()  # Salva as tarefas antes de fechar
        self.janela.destroy()  # Fecha a janela

    def rodar(self):
        self.janela.mainloop()  # Inicia o loop da interface gráfica

# Criando o Gerenciador de Tarefas e a Interface
gerenciador = GerenciadorDeTarefas()
gerenciador.carregar_tarefas()  # Carrega as tarefas do arquivo

interface = Interface(gerenciador)

# Rodando a interface
interface.rodar()
