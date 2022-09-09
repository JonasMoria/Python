
print('=== CADASTRO DE FUNCIONÁRIOS ===')

name = input('nome do funcionário: ')
salary = float(input('salario a receber: '))
enterprise = input('nome da empresa/instituição: ')
employees = int(input('Qtnd. Funcionarios: '))

print('\n === CONCATENANDO DADOS ===')
print('o funcionario '+name+' trabalha na empresa '+enterprise+' que possui o total de '+str(employees)+' funcionarios e recebe um salario de '+str(salary))

print('\n === VERIFICANDO TIPOS DE DADOS ===')
print("O tipo de dado da variavel [nome] é: ", type(name))
print("O tipo de dado da variavel [empresa] é: ", type(enterprise))
print("O tipo de dado da variavel [qtde_funcionarios] é: ", type(employees))
print("O tipo de dado da variavel [salario] é: ", type(salary))
