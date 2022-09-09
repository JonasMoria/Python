
print('=== INVENTÁRIO ===')
inventory = []
option = 'S'

while option == 'S':
    inventory.append(input('\nEquipamento: '))
    inventory.append(float(input('Valor: ')))
    inventory.append(int(input('Serial: ')))
    inventory.append(input('Departamento: '))
    option = input('Digite \"S\" para continuar adicionando: ').upper()


for element in inventory:
    print(element)

