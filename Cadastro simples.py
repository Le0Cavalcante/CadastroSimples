from DefFunCadastro import*
usuario = []
minhaLista = usuario

print("O que deseja fazer?\n 1 - CADASTRAR NOVO USUÁRIO \n 2 - DELETAR USUÁRIO \n 3 - PESQUISAR USUÁRIO \n 4 - EXIBIR USUÁRIOS \n 5 - SALVAR LISTA \n 6 - SAIR")
resposta = int(input("Selecione uma opção: "))
while resposta > 0:
    if resposta == 1:
        print("Preenchendo...")
        dadosUser(usuario)
        print("Exibindo: ")
        exibirUsuario(usuario)
        print("O que deseja fazer?\n 1 - CADASTRAR NOVO USUÁRIO \n 2 - DELETAR USUÁRIO \n 3 - PESQUISAR USUÁRIO \n 4 - EXIBIR USUÁRIOS \n 5 - SALVAR LISTA \n 6 - SAIR")
        resposta = int(input("Selecione uma opção: "))
    elif resposta == 2:
        print("Selecionando usuário a ser apagado...")
        delUser(usuario)
        print("Usuário Deletado")
        print("O que deseja fazer?\n 1 - CADASTRAR NOVO USUÁRIO \n 2 - DELETAR USUÁRIO \n 3 - PESQUISAR USUÁRIO \n 4 - EXIBIR USUÁRIOS \n 5 - SALVAR LISTA \n 6 - SAIR")
        resposta = int(input("Selecione uma opção: "))

    elif resposta == 3:
        print("Procurando...")
        localizarUsuario(usuario)
        print("O que deseja fazer?\n 1 - CADASTRAR NOVO USUÁRIO \n 2 - DELETAR USUÁRIO \n 3 - PESQUISAR USUÁRIO \n 4 - EXIBIR USUÁRIOS \n 5 - SALVAR LISTA \n 6 - SAIR")
        resposta = int(input("Selecione uma opção: "))

    elif resposta == 4:
        print("Exibindo usuários ativos: ")
        exibirUsuario(usuario)
        print("O que deseja fazer?\n 1 - CADASTRAR NOVO USUÁRIO \n 2 - DELETAR USUÁRIO \n 3 - PESQUISAR USUÁRIO \n 4 - EXIBIR USUÁRIOS \n 5 - SALVAR LISTA \n 6 - SAIR")
        resposta = int(input("Selecione uma opção: "))

    elif resposta == 5:
        print("Salvando lista")
        salvar_arquivo(usuario)
        print("O que deseja fazer?\n 1 - CADASTRAR NOVO USUÁRIO \n 2 - DELETAR USUÁRIO \n 3 - PESQUISAR USUÁRIO \n 4 - EXIBIR USUÁRIOS \n 5 - SALVAR LISTA \n 6 - SAIR")
        resposta = int(input("Selecione uma opção: "))

    else:
        print("Encerrando a Aplicação.")
        break




