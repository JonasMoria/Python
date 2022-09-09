
usuarios = {}
emails = ['example@email.com','example2@email.com']

tupla = list(enumerate(emails))

# print(tupla)

for chave in range (0, len(tupla)):
    print('Email: ',tupla[chave][1])
    usuarios[tupla[chave]] = [input('Digite o nome: '), input('Digite o Nivel: ')]

# print(usuarios.items())

for chave, dado in usuarios.items():
    print('\nUsuario....: ',chave[0])
    print('Email......: ',chave[1])
    print('Nome....: ',dado[0])
    print('Nivel....: ',dado[1])