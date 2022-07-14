
print('\n=== COMPARADOR DE HASHES ===')

totalHashes = 0
hashList = []

hash = input('Digite a Hash a ser comparada: ')
print('\n')


print('Digite 0 para parar!')
print('\n')
while True:
    hashValue = input('Digite uma Hash para ser comparada: ')
    hashList.append(hashValue)

    if hashValue == '0':
      break

# removendo o input de parada do loop
hashList.pop()

print(f'\nHash: {hash}')
print('Lista de Hashes para comparar: ')
print(hashList)
print('\n')


for key, value in enumerate(hashList):
    if value == hash:
        totalHashes+=1
        print(f'Hash semelhante encontrada na posicao {key}')


if totalHashes >= 1:
    print(f'\n{totalHashes} Hashes semelhantes encontradas')
else:
    print('\nNenhuma Hash semelhante foi encontrada')
    