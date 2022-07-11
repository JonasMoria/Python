
import itertools
import os

print('=== GERADOR DE WORDLIST ===')
word = input('Palavra Desejada Para Criar a Wordlist: ')
size = len(word)
fileName = input('Digite Nome do Arquivo a Ser Gerado: ')

# responsável por gerar a wordlist
wordList = itertools.permutations(word, size)

# gravando as palavras geradas em um arquivo txt
try:
    with open(fileName+'.txt', 'w') as f:
        for i in wordList:
            f.write('{}\n'.format(''.join(i)))
except:
    print('Não foi possivel gerar o arquivo, tente novamente...')


if os.path.exists(fileName+'.txt'):
    print('Arquivo gerado!!')
    input('Pressione Enter para encerrar...')
else:
    print('Arquivo Nao Gerado, Tente Novamente...')
