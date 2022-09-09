
print('\n=== INVENTÁRIO ===')

inventory = []
option = 'S'

while option == 'S':
    equipment = (input('Equipamento: '),
                 float(input('Valor: ')),
                 int(input('Serial: ')),
                 input('Departamento: '))
    inventory.append(equipment)
    option = input('Digite "\S"\ para continuar: ').upper()


for element in inventory:
    print('\nNome:  ', element[0])
    print('Valor: ', element[1])
    print('Serial: ', element[2])
    print('Departamento: ', element[3])

search = input('\nDigite o Nome do Equipamento Que Deseja Buscar: ')
for element in inventory:
    if search == element[0]:
        print('Valor:  ', element[1])
        print('Serial: ', element[2])

depreciate = input('\nDigite o Nome do Equipamento Que Será Depreciado: ')
for element in inventory:
    if depreciate == element[0]:
        print('Valor Antigo:  ', element[1])
        newValue = element[1]*0.9
        print('Novo Valor: ', newValue)

remove = input('Digite Serial Do Equipamento Que Será Excluido: ')
for element in inventory:
    if element[2] == remove:
        inventory.remove(element)

for element in inventory:
    print('Nome:  ', element[0])
    print('Valor: ', element[1])
    print('Serial: ', element[2])
    print('Departamento: ', element[3])


values = []
for element in inventory:
    values.append(element[1])
if len(values)>0:
    print('O Equipamento mais caro custa: ',max(values))
    print('O Equipamento mais barato custa: ',min(values))
    print('O Valor total de equipamentos: ',sum(values))


for element in inventory:
    print('\nNome:  ', element[0])
    print('Valor: ', element[1])
    print('Serial: ', element[2])
    print('Departamento: ', element[3])
