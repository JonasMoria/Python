
print('\n=== COMPARADOR DE HASHES v2 ===')

totalHashes = 0

hash = input('Digite a Hash a ser comparada: ')
print('\n')

# lendo o arquivo onde estão as hashes
try:
    with open('HashList.txt') as file:
        dump = file.read()
        dump = dump.splitlines()
except:
   print('Erro ao encontrar o arquivo, verifique o caminho e tente novamente')

# método para buscar hashes iguais
def searchHash(hashes,totalHashes):
    for key, value in enumerate(hashes):
        if value == hash:
            totalHashes+=1
            print(f'Hash semelhante encontrada na posicao {key} da lista')

    if totalHashes >= 1:
        print(f'\n{totalHashes} Hashes semelhantes encontradas')
    else:
        print('\nNenhuma Hash semelhante foi encontrada')


searchHash(dump,totalHashes)