
from funcoes import *


usuarios = {}

opcao = menu()

while opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
    if opcao == 1:
        inserir(usuarios)
        salvar(usuarios)
        opcao = menu()

    if opcao == 2:
        listar(usuarios)
        opcao = menu()

    if opcao == 3:
        excluir(usuarios)
        opcao = menu()

    if opcao == 4:
        pesquisar(usuarios)
        opcao = menu()
    
    if opcao == 5:
        break

    if opcao != 1 or  opcao != 2 or opcao != 3 or opcao != 4 or opcao != 5:
        print('\nOpcao Invalida!!\n')
        opcao = menu()

