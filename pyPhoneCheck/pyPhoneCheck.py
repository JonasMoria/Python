
# pip install phonenumbers

import phonenumbers
from phonenumbers import timezone, geocoder,carrier

print('\n=== VERIFICADOR DE NÚMERO DE TELEFONE ===')


def validateNumber(phone):
    
    phoneNumbers = phonenumbers.parse(phone)
    possible = phonenumbers.is_possible_number(phoneNumbers)

    if  possible == True:
        print('Número Válido \n')
    else:
        print('Numero Inválido \n')


def processNumber(phone):
    phoneNumbers = phonenumbers.parse(phone)
    timeZone = timezone.time_zones_for_number(phoneNumbers)
    region = geocoder.description_for_number(phoneNumbers, 'pt-br')
    Carrier = carrier.name_for_number(phoneNumbers,'pt-br')
    print('\nNúmero de telefone: '+phone)
    print('Fuso Horário' + str(timeZone))
    print('Região: '+region)
    print('Operadora: '+Carrier)


try:
    country = '+' + input('Digite cod. do País:  ')
    ddd = input('Digite o DDD: ')
    number = input('Digite o Numero de Telefone: ')
    phone = country + ddd + number

    processNumber(phone)
    validateNumber(phone)
except:
    print('Erro ao processar dados, verifique-os e tente novamente!')
