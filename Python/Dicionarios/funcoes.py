
from datetime import datetime


def inserir(dicionario={}):
    chave = input('\nDigite Login: ').upper()
    nome = input('Digite o Nome: ').upper()
    data = datetime.today().strftime('%d-%m-%Y %H:%M')
    setor = input('Digite Ultimo Setor Acessado: ').upper()
    dicionario[chave] = [nome, data, setor]


# def listar(dicionario={}):
#     print(dicionario)

def listar(dicionario={}):
    with open('Dicionarios/bd.txt') as arquivo:
        for linhas in arquivo.readlines():
            print(linhas)
            


def pesquisar(dicionario={}):
    elemento = input('\nDigite o Login: ').upper()
    print(dicionario.get(elemento, 'Chave não encontrada'))

def excluir(dicionario={}):
    elemento = input('\nDigite Login Que Deseja Excluir: ').upper()
    del dicionario[elemento]

def salvar(dicionario={}):
    with open('Dicionarios/bd.txt','a') as arquivo:
        for chave,valor in dicionario.items():
            arquivo.write(chave+' : '+str(valor))



def menu():
    print('\n1) Inserir Usuario')
    print('2) Listar Usuario')
    print('3) Excluir Usuario')
    print('4) Pesquisar Usuario')
    print('5) Sair')
    return int(input('Selecione >>> '))
