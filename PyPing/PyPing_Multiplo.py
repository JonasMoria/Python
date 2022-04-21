
import os

print('\n=== PY PING ===\n')

targets = []

# Limpando o arquivo txt para novas entradas de dados
with open('LOGS.txt', 'r+') as file:
    file.truncate()

# Caminho do arquivo:
with open('PyHostsList.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for hosts in dump:
        targets.append(hosts)


for hosts in targets:

    print("Analisando..."+hosts)

    # Executando o ping
    os.system('ping -n 4 {} >> LOGS.txt'.format(hosts))
    os.system(
        'echo ============================================================== >> LOGS.txt')


print("\n")
print("Alvos Analisados: ")
print(targets)
