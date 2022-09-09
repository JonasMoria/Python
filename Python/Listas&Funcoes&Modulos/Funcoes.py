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


def showInventory(list):
    for element in list:
        print('\nNome...........:', element[0])
        print('Valor............:', element[1])
        print('Serial...........:', element[2])
        print('Departamento.....:', element[3])


def searchByName(list):
    search = input('\nDigite o Nome do Equipamento Que Deseja Buscar: ')
    for element in list:
        if search == element[0]:
            print('\nValor:  ', element[1])
            print('Serial: ', element[2])
            print('Departamento: ', element[2])

def depreciateByName(list):
    depreciate = input('\nDigite o Nome do Equipamento Que Será Depreciado: ')
    for element in list:
        if depreciate == element[0]:
            print('Valor Antigo:  ', element[1])
            newValue = element[1]*0.9
            print('Novo Valor: ', newValue)

def removeBySerial(list):
    remove = input('Digite Serial Do Equipamento Que Será Excluido: ')
    for element in list:
        if element[2] == remove:
            list.remove(element)
            return 'Excluido com Sucesso'
        else:
           return 'Falha ao excluir'

def showResume(list):
    values = []
    for element in list:
        values.append(element[1])
    if len(values)>0:
        print('\nO Equipamento mais caro custa: ',max(values))
        print('O Equipamento mais barato custa: ',min(values))
        print('O Valor total de equipamentos: ',sum(values))  

select = 0
while(select!=6):
    print('\n=== OPCOES ===')
    print('1) Mostrar Resumo Dos Equipamentos')
    print('2) Remover Um Equipamento')
    print('3) Depreciar um Equipamento')
    print('4) Pesquisar Equipamento')
    print('5) Mostrar Todos os Equipamentos')
    print('6) Sair')
    select = int(input('>>> '))

    if select == 1:
        showResume(inventory)
    if select == 2:
        removeBySerial(inventory)
    if select == 3:
        depreciateByName(inventory)
    if select == 4:
        searchByName(inventory)
    if select == 5:
        showInventory(inventory)
