from view.loginScreen import LoginScreen
from view.passScreen import PassScreen
from controller.userController import UserController
import json


if __name__ == "__main__":

    userDirectory = "database\\users.json"

    


    with open(userDirectory) as usersFile:
        usersList = json.load(usersFile)

    
    userController = UserController(usersList, userDirectory)

    for user in usersList:
        print(f"{user} \n")


    print("Digite o seu nome: ")
    name = input()
    print("Digite seu email: ")
    email = input()
    print("Digite sua senha: ")
    senha = input()
    print("Digite o seu dinheiro: ")
    dinheiro = int(input())


    userController.registerUser(name, email, senha, dinheiro)


    """ LoginScreen()

    name = input("Digite o seu nome: ")

    for user in usersList:
        if user['name'] == name:
            print("Usuario encontrado!")

    PassScreen()

    senha = input("Digite a sua senha: ")

    for user in usersList:
        if user['senha'] == senha:
            print("Senha correta!")

    LoggedUser = userController.login(name, senha)


    print(LoggedUser['name'])

    print(usersList[0]['dinheiro'])

    userController.deposito(2000, LoggedUser)

    print(usersList[0]['dinheiro']) """



        

