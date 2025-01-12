from model import Model
model = Model()

class Controller:

    def cadastrocontroller(self, nome, especie, sexo, tutor, observacoes):
        model.salvarcadastro(nome, especie, sexo, tutor, observacoes)

    def deletarcadastro(self, nome):
        model.deletarcadastro(nome)

    def atualizarcad(self, nome, observacoes):
        model.atualizarcad(nome, observacoes)

    def checar_se_cadastro_existe(self, nome):
        return model.checar_se_cadastro_existe(nome)

    def medicacaocontroller(self, nome, medicamento, horario, dosagem):
        model.salvarmedicacao(nome, medicamento, horario, dosagem)

    def getdadoscadastro(self, nomee):
        dados = model.getdadoscadastro(nomee)
        
        if dados:  
            diciocad = {
                'nome': dados[0],
                'especie': dados[1],
                'sexo': dados[2],
                'tutor': dados[3],
                'observacoes': dados[4]
            }
            return diciocad
    
    
    def retornarag(self, nome):
        registros = model.retornarag(nome)
    
        dicioag = {
            'medicamento': [],
            'dosagem': [],
            'horario': []
        }
        
        for registro in registros:
            dicioag['medicamento'].append(registro[0])  
            dicioag['dosagem'].append(registro[1])     
            dicioag['horario'].append(registro[2])    

        return dicioag
            
