
print('\n=== INVENTÁRIO ===')

equipment = []
values = []
serials = []
departments = []
option = 'S'

while option == 'S':
    equipment.append(input('\nEquipamento: '))
    values.append(float(input('Valor: ')))
    serials.append(int(input('Numero Serial: ')))
    departments.append(input('Departamento: '))
    option = input('Digite "\S"\ para continuar: ').upper()


search = input('\nDigite Equipamento Que Deseja Buscar: ')

for i in range(0,len(equipment)):
    if search == equipment[i]:
        print('Valor:  ', values[i])
        print('Serial: ', serials[i])
        print('Departamento: ',departments[i])