from model.user import User
import json

class UserController:
    def __init__(self, userList, usersDirectory):
        self.userList = userList
        self.usersDirectory = usersDirectory

    def updateJson(self):
        with open(self.usersDirectory, 'w') as updateFile:
            json.dump(self.userList, updateFile, indent=4)

    def registerUser(self, nome, email, senha, dinheiro):
        newUser = User(nome, email, senha, dinheiro)
        convertedUser = vars(newUser)
        self.userList.append(convertedUser)
        self.updateJson()



    def login(self, name, password):
        for user in self.userList:
            if user['name'] == name and user['senha'] == password:
                return user
            

    def deposito(self, valor, Loggeduser):
        for user in self.userList:
            if user['name'] == Loggeduser['name']:
                user['dinheiro'] += valor
                self.updateJson()
        
    
                

