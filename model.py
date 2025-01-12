import mysql.connector
from mysql.connector import Error

class Model:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root", 
                password="baubau77",  
                database="med_tracker"
            )
            if self.conn.is_connected():
                print("Conectado")
                self.cursor = self.conn.cursor()
        except Error as erro:
            print("Não conectado")
            print(f"Erro: {erro}")
            self.conn = None
            self.cursor = None

    def checar_se_cadastro_existe(self, nome):
        sql = "SELECT nome FROM Animais WHERE nome = %s"
        self.cursor.execute(sql, (nome,))
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return None 
    

    def salvarmedicacao(self, nome, medicamento, horario, dosagem):
        if self.cursor:
            try:
                sql = "INSERT INTO Medicacoes (nome, medicamento, horario, dosagem) VALUES (%s, %s, %s, %s)"
                values = (nome, medicamento, horario, dosagem)
                self.cursor.execute(sql, values)
                self.conn.commit()
                print("Deu certo")
            except mysql.connector.Error as erro:
                print(f"Erro ao inserir dados: {erro}")
                self.conn.rollback()
            


    def salvarcadastro(self, nome, especie, sexo, tutor, observacoes):
        if self.cursor:
            try:
                sql = "INSERT INTO Animais (nome, especie, sexo, tutor, observacoes) VALUES (%s, %s, %s, %s, %s) "
                values = (nome, especie, sexo, tutor, observacoes)
                self.cursor.execute(sql, values)
                self.conn.commit()
                print("Cadastro salvo com sucesso!")
            except mysql.connector.Error as erro:
                print(f"Erro ao inserir dados: {erro}")
                self.conn.rollback()


    def deletarcadastro(self, nome):
         if self.cursor:
            try:
                sql = "DELETE FROM Animais WHERE nome = %s"
                values = (nome,)
                self.cursor.execute(sql, values)
                self.conn.commit()
                print("Deu certo")
            except mysql.connector.Error as erro:
                print(f"Erro ao inserir dados: {erro}")
                self.conn.rollback()

    def atualizarcad(self, nome, observacoes):
         if self.cursor:
            try:
                sql = "UPDATE Animais SET observacoes = %s WHERE nome = %s"
                values = (observacoes, nome)
                self.cursor.execute(sql, values)
                self.conn.commit()
                print("Deu certo")
            except mysql.connector.Error as erro:
                print(f"Erro ao inserir dados: {erro}")
                self.conn.rollback()

           

    def getdadoscadastro(self, nome):
        if self.cursor:
            sql = "SELECT nome, especie, sexo, tutor, observacoes FROM Animais WHERE nome = %s"
            self.cursor.execute(sql, (nome,))
            print("yolo")
            return self.cursor.fetchone()
            
            
        
    def retornarag(self, nome):
        if self.cursor:
            sql = "SELECT medicamento, horario, dosagem FROM Medicacoes WHERE nome = %s ORDER BY horario"
            self.cursor.execute(sql, (nome,))
            return self.cursor.fetchall()
