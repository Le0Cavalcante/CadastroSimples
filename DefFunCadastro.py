lista = []
def dadosUser (lista):
    usuario = [input("Nome Completo: "),
            input("CPF: "),
            input("Telefone: "),
            input("Email: ")]
    lista.append(usuario)

def exibirUsuario(lista):
    for indice in range(0, len(lista)):
        print("\n CÓD: ", (indice+1))
        print(lista[indice])

def localizarUsuario(lista):
    busca = input(("\nDigite o CPF ou o nome do usuário: "))
    for elemento in lista:
        if busca == elemento[1] or elemento[0]:
            print("Nome: ", elemento[0])
            print("CPF: ", elemento[1])
            print("Contato: ", elemento[2], elemento[3])

def delUser(lista):
    delUser = input("Digite o CPF do usuário: ")
    for elemento in lista:
        if delUser == elemento[1]:
            lista.remove(elemento)
    return "Itens excluídos"

def salvar_arquivo(lista):
    with open("cadastro.txt", "a") as arquivo:
        arquivo.write(str(lista))

