import tkinter as tk
from tkinter import ttk, messagebox
from controller import Controller
controller = Controller()

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Med Tracker")  
        self.root.geometry("500x360") 
        self.root.configure(bg="#D8EFF0")

        self.main_frame = tk.Frame(self.root, bg="#D8EFF0")
        self.main_frame.pack(expand=True)
        
        self.inicioview()

    def clear_frame(self):      #Limpa o frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def inicioview(self):       #Tela inicial
        self.clear_frame()

        titulo_font = ("Times New Roman", 27)
        minititulo_font = ("Times New Roman", 15)
        botao_font = ("Times New Roman", 11)

        label_main = tk.Label(self.main_frame, text="Med Tracker", font=titulo_font, bg="#D8EFF0")
        label_main.pack(pady=(20, 10)) 

        label_sub = tk.Label(self.main_frame, text="para pets", font=minititulo_font, bg="#D8EFF0")
        label_sub.pack(pady=(0, 20))  

        button_frame = tk.Frame(self.main_frame, bg="#D8EFF0")
        button_frame.pack(pady=(20, 0))

        button1 = tk.Button(button_frame, text="Animais cadastrados", font=botao_font, 
                            command=self.animaiscadastradosview, 
                            fg="#FFFFFF", bg="#589A8D", width=20, height=1)
        button1.pack(pady=10)

        button2 = tk.Button(button_frame, text="Novo medicamento", font=botao_font, 
                            command=self.novamedicacaoview, 
                            fg="#FFFFFF", bg="#589A8D", width=20, height=1)
        button2.pack(pady=10)

        button3 = tk.Button(button_frame, text="Criar/manipular cadastros", font=botao_font, 
                            command=self.telacadastroview, 
                            fg="#FFFFFF", bg="#589A8D", width=20, height=1)
        button3.pack(pady=(10, 50))

    def animaiscadastradosview(self):       #Tela de cadastro
        self.clear_frame()

        label_main = tk.Label(self.main_frame, text="Animais cadastrados", font = ("Times New Roman", 20), bg="#D8EFF0")
        label_main.pack(pady = (0, 40)) 

        nome = tk.Label(self.main_frame, text="Nome do paciente:", font=("Times New Roman", 12), bg="#D8EFF0")
        nome.pack()
        self.nome_entry = tk.Entry(self.main_frame, font=("Times New Roman", 14))
        self.nome_entry.pack()
        
        containerbotoes = tk.Frame(self.main_frame, bg = "#D8EFF0")
        containerbotoes.pack(padx = 20)

        adicionarbotao = tk.Button(containerbotoes, text="Avançar", font=("Times New Roman", 10), width=7, height=1, bg="#589A8D", fg="#FFFFFF", 
                                   command = self.dadodocadastro)
        adicionarbotao.grid(row = 0, column = 1, sticky = "e", pady = (50, 0), padx = 10)

        botaovoltar = tk.Button(containerbotoes, text="Voltar", font=("Times New Roman", 10), width=7, height=1, bg="#589A8D", fg="#FFFFFF", 
                                command = self.inicioview)
        botaovoltar.grid(row = 0, column = 0,  sticky = "w", pady = (50, 0), padx = 10)

    def dadodocadastro(self):       
        self.nomee = self.nome_entry.get()
        dados = controller.getdadoscadastro(self.nomee)
        if dados:  
            self.exibircadastroview()
            self.nomee = self.nome_entry.get()
        else:
            messagebox.showinfo("Info", "Cadastro não existe!")

    def novamedicacaoview(self):
        self.clear_frame()

        label_main = tk.Label(self.main_frame, text="Novo medicamento", font=("Times New Roman", 20), bg="#D8EFF0")
        label_main.pack(pady=(20, 0))  

        main_frame = tk.Frame(self.main_frame, bg="#D8EFF0")
        main_frame.pack(expand=True, pady=20)

        nome_id_paciente = tk.Label(main_frame, text="Paciente:", font=("Times New Roman", 14), bg="#D8EFF0")
        nome_id_paciente.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.paciente_entry = tk.Entry(main_frame, font=("Times New Roman", 14))
        self.paciente_entry.grid(row=0, column=1, padx=10, pady=10)

        medicamento = tk.Label(main_frame, text="Nome do medicamento:", font=("Times New Roman", 14), bg="#D8EFF0")
        medicamento.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.medicamento_entry = tk.Entry(main_frame, font=("Times New Roman", 14))
        self.medicamento_entry.grid(row=1, column=1, padx=10, pady=10)

        horario = tk.Label(main_frame, text="Horário:", font=("Times New Roman", 14), bg="#D8EFF0")
        horario.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.horario_entry = tk.Entry(main_frame, font=("Times New Roman", 14))
        self.horario_entry.grid(row=2, column=1, padx=10, pady=10)

        dosagem = tk.Label(main_frame, text="Dosagem:", font=("Times New Roman", 14), bg="#D8EFF0")
        dosagem.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.dosagem_entry = tk.Entry(main_frame, font=("Times New Roman", 14))
        self.dosagem_entry.grid(row=3, column=1, padx=10, pady=10)

        adicionarbotao = tk.Button(main_frame, text="Salvar", font=("Times New Roman", 10), width=7, height=1, bg="#589A8D", fg="#FFFFFF", 
                                command=self.salvarmed)
        adicionarbotao.grid(row=4, column=1)

        botaovoltar = tk.Button(main_frame, text="Voltar", font=("Times New Roman", 10), width=7, height=1, bg="#589A8D", fg="#FFFFFF", 
                                command=self.inicioview)
        botaovoltar.grid(row=4, column=0)

    def salvarmed(self):        #Função para salvar os dados do medicamento.
        nome = self.paciente_entry.get()
        medicamento = self.medicamento_entry.get()
        horario = self.horario_entry.get()
        dosagem = self.dosagem_entry.get()
        
        verificacao = controller.checar_se_cadastro_existe(nome)
        
        if verificacao:
            controller.medicacaocontroller(nome, medicamento, horario, dosagem)
            messagebox.showinfo("Info", "Cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Paciente não encontrado!")

    def telacadastroview(self):  #tela de manipular os cadastros.
        self.clear_frame()
        
        label_main = tk.Label(self.main_frame, text="Novo paciente", font=("Times New Roman", 18), bg="#D8EFF0")
        label_main.pack(pady=(10, 0))  

        main_frame = tk.Frame(self.main_frame, bg="#D8EFF0")
        main_frame.pack(expand=True, pady=10)

        nome = tk.Label(main_frame, text="Nome do paciente:", font=("Times New Roman", 12), bg="#D8EFF0")
        nome.grid(row=0, column=0, padx=10, pady=8, sticky="e")
        self.nome_entry = tk.Entry(main_frame, font=("Times New Roman", 12))
        self.nome_entry.grid(row=0, column=1, padx=10, pady=8)

        especie = tk.Label(main_frame, text="Espécie:", font=("Times New Roman", 12), bg="#D8EFF0")
        especie.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.especiee = tk.StringVar()
        self.especie_combobox = ttk.Combobox(main_frame, font=("Times New Roman", 11), 
                                             values = ["Cachorro", "Gato", "Ave", "Réptil", "Roedor", "Peixe", "Outros"], textvariable = self.especiee)
        self.especie_combobox.grid(row=1, column=1, padx=10, pady=10)

        sexo = tk.Label(main_frame, text="Sexo:", font=("Times New Roman", 12), bg="#D8EFF0")
        sexo.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.sexoo = tk.StringVar()
        self.sexo_combobox = ttk.Combobox(main_frame, font=("Times New Roman", 11), values=['F', 'M'], textvariable = self.sexoo)
        self.sexo_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="e")
       

        tutor = tk.Label(main_frame, text="Tutor:", font=("Times New Roman", 12), bg="#D8EFF0")
        tutor.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.tutor_entry = tk.Entry(main_frame, font=("Times New Roman", 12))
        self.tutor_entry.grid(row=3, column=1, padx=10, pady=10)

        observacoes = tk.Label(main_frame, text="Observações:", font=("Times New Roman", 12), bg="#D8EFF0")
        observacoes.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.observacoes_entry = tk.Entry(main_frame, font=("Times New Roman", 12))
        self.observacoes_entry.grid(row=4, column=1, padx=10, pady=10)

        containerbotoes = tk.Frame(self.main_frame, bg = "#D8EFF0")
        containerbotoes.pack(padx = 20)

        adicionarbotao = tk.Button(containerbotoes, text="Salvar", font=("Times New Roman", 10), width=7, height=1, bg="#589A8D", fg="#FFFFFF", command = self.salvarcad)
        adicionarbotao.grid(row=8, column=3, padx = (10, 20))

        adicionarbotao = tk.Button(containerbotoes, text="Atualizar", font=("Times New Roman", 10), width=7, height=1, bg="#589A8D", fg="#FFFFFF", command = self.atualizarcad)
        adicionarbotao.grid(row=8, column=2, padx = 10)

        botaodeletar = tk.Button(containerbotoes, text="Deletar", font=("Times New Roman", 10), width=7, height=1, bg="#589A8D", fg="#FFFFFF", command = self.deletarcadastro)
        botaodeletar.grid(row=8, column=1, padx = 10)

        botaovoltar = tk.Button(containerbotoes, text="Voltar", font=("Times New Roman", 10), width=7, height=1, bg="#589A8D", fg="#FFFFFF", command = self.inicioview)
        botaovoltar.grid(row=8, column=0, padx = (20, 10))
        
    def salvarcad(self):        #Função para salvar os dados do cadastro
        nome = self.nome_entry.get()
        especie = self.especiee.get()
        sexo = self.sexoo.get()
        tutor = self.tutor_entry.get()
        observacoes = self.observacoes_entry.get()
        controller.cadastrocontroller(nome, especie, sexo, tutor, observacoes)
        messagebox.showinfo("Info", "Cadastrado com sucesso!")

    def deletarcadastro(self):   #Inserir apenas nome para deletar um cadastro
        nome = self.nome_entry.get()
        controller.deletarcadastro(nome)
        messagebox.showinfo("Info", "Cadastro excluído!")

    def atualizarcad(self):     #Atualiza apenas observação. Inserir apenas nome e nova observação para atualizar.
        nome = self.nome_entry.get()
        observacoes = self.observacoes_entry.get()
        controller.atualizarcad(nome, observacoes)
        messagebox.showinfo("Info", "Cadastro atualizado!" )

    def set_dicionarios(self, diciocad, dicioag):
        self.diciocad = diciocad
        self.dicioag = dicioag


    def exibircadastroview(self):
        self.clear_frame()

        dados = controller.getdadoscadastro(self.nomee)
        agenda = controller.retornarag(self.nomee)

        nome = dados.get('nome')
        especie = dados.get('especie')
        sexo = dados.get('sexo')
        tutor = dados.get('tutor')
        observacoes = dados.get('observacoes')

        medicamento_list = agenda.get('medicamento', [])
        dosagem_list = agenda.get('dosagem', [])
        horario_list = agenda.get('horario', [])

        length = min(len(medicamento_list), len(dosagem_list), len(horario_list))

        alterar_frame = tk.Frame(self.main_frame, bg="#D8EFF0")
        alterar_frame.pack(expand=True, pady=20)
        
        left_frame = tk.Frame(alterar_frame, bg="#D8EFF0")
        left_frame.grid(row=0, column=0)

        label_titulo = tk.Label(left_frame, bg="#D8EFF0", text=nome, font=("Times New Roman", 18))
        label_titulo.pack(pady=10, anchor="w", padx=(15, 0))

        label_agenda = tk.Label(left_frame, bg="#D8EFF0", text="Agenda", font=("Times New Roman", 10))
        label_agenda.pack()

        agenda_frame = tk.Frame(left_frame, bg="#589A8D", width=180, height=200)
        agenda_frame.pack_propagate(False)
        agenda_frame.pack(padx=15)

        vars_dict = {}

        for i in range(length):
            var = tk.BooleanVar()
            vars_dict[i] = var

            medicamento = medicamento_list[i]
            dosagem = dosagem_list[i]
            horario = horario_list[i]

            texto = f"{medicamento} - {dosagem} - {horario}"
            chk = tk.Checkbutton(agenda_frame, bg="#589A8D", text=texto, variable=var, font=("Times New Roman", 8))
            chk.pack(anchor='w', pady=5)

    
        botaovoltar = tk.Button(left_frame, text="Voltar", font=("Times New Roman", 8), width=7, height=1, bg="#589A8D", fg="#FFFFFF", 
                                command=self.animaiscadastradosview)
        botaovoltar.pack(pady=20)

        right_frame = tk.Frame(alterar_frame, bg="#D8EFF0")
        right_frame.grid(row=0, column=1)

        label_dados = tk.Label(right_frame, bg="#D8EFF0", text="Dados", font=("Times New Roman", 10))
        label_dados.pack()

        dados_frame = tk.Frame(right_frame, bg="#83E6D0", width=180, height=130)
        dados_frame.pack_propagate(False)
        dados_frame.pack(padx=15)
        
        label_dadoss = tk.Label(dados_frame, bg="#83E6D0", 
                                text=f"Nome: {nome}\n\nEspécie: {especie}\n\nSexo: {sexo}\n\nTutor(a): {tutor}", 
                                font=("Times New Roman", 8))
        label_dadoss.pack(anchor="center", pady=(10, 10), padx=(8, 8))

        label_observacoes = tk.Label(right_frame, bg="#D8EFF0", text="Observações", font=("Times New Roman", 10))
        label_observacoes.pack()

        observacoes_frame = tk.Frame(right_frame, bg="#FFFFFF", width=180, height=80)
        observacoes_frame.pack_propagate(False)
        observacoes_frame.pack(padx=15)

        label_observacoess = tk.Label(observacoes_frame, bg="#FFFFFF", text=observacoes, font=("Times New Roman", 8))
        label_observacoess.pack(pady=(10, 10), padx=(8, 8))

        return vars_dict

    def run(self):
        self.root.mainloop()

