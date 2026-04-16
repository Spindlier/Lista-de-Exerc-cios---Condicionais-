usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")