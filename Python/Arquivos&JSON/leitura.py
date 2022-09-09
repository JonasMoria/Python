
# primeira opção
# with open('Arquivos&JSON/primeiro_arquivo.txt','r') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# segunda opção readline -> leitura de apenas uma linha
with open('Arquivos&JSON/primeiro_arquivo.txt','r') as arquivo:
    conteudo = arquivo.readline()
    for linha in arquivo.readlines():
        print(linha)