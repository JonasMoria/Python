
print('\n=== tabuada ===')

tabuada = int(input('Digite Numero para exibir a tabuada: '))

print('Tabuada do numero '+str(tabuada))

for valor in range(1,11,1):
    print(str(tabuada) + 'x' + str(valor) + '=' + str(tabuada*valor))