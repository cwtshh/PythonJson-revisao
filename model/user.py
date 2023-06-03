class User:
    def __init__(self, name, email, senha, dinheiro):
        self.name = name
        self.email = email
        self.senha = senha
        self.dinheiro = dinheiro

    # NAO VAI USAR
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_senha(self):
        return self.senha
    