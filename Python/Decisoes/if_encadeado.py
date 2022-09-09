
name = input('\nDigite  o nome: ')
idade = int(input('Digite a idade: '))
doenca = input('Suspeita de Doenca infectocontagiosa?[sim/nao]: ').upper()

if idade >= 65:
    print('Atendimento preferencial para '+name)
elif doenca == 'SIM':
    print('Paciente '+name+'deve ser direcionado para sala de espera reserva!')
else:
    print('paciente '+name+' nao possui atendimento prioritario!')
