# Primeira opção
# arquivo = open('Arquivos&JSON/primeiro_arquivo.txt','w')

# arquivo.write('Testando escrita de arquivo...')
# arquivo.close()

#segunda opção
with open('Arquivos&JSON/primeiro_arquivo.txt','w') as arquivo:
    arquivo.write('\nTestando com with open')
