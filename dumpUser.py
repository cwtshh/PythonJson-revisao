from model.user import User
import json


# Cria os usuarios
user1 = User("Joao", "joao@gmail.com", "123", 1000)
convertedUser1 = vars(user1)
user2 = User("Maria", "maria@gmail.com", "1234", 2000)
convertedUser2 = vars(user2)
user3 = User("Jose", "jose@gmail.com", "12345", 3000)
convertedUser3 = vars(user3)
user4 = User("Ana", "ana@gmail.com", "123456", 4000)
convertedUser4 = vars(user4)


# abre o arquivo json
with open("database\\users.json") as usersFile:
    usersList = json.load(usersFile)




usersList.append(convertedUser1)
usersList.append(convertedUser2)
usersList.append(convertedUser3)
usersList.append(convertedUser4)

print(usersList)



with open("database\\users.json", "w") as updateFile:
    json.dump(usersList, updateFile, indent=4)



