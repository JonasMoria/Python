
import subprocess

print('\n===DESCOBRIDOR DE SENHAS WIFI SALVAS===')

# Capturando informações da rede
informations = subprocess.check_output([
    "netsh", "wlan", "show", "profiles"
], encoding='cp860')

print(informations)

# Exibindo as senhas
try:
    wifi_name = input("Digite o Nome Do Wifi: ")
    output = subprocess.check_output([
        "netsh", "wlan", "show", "profile", wifi_name, "key" "=" "clear"
    ], encoding='cp858')

    for lines in output.split('\n'):
        if "Conteúdo da Chave" in lines:
            # capturando a senha
            position = lines.find(":")
            password = lines[position+2:]
            print("Senha ==> "+password)
    moreInfo = input("Deseja ver Informações completas deste wifi?[s/n]: \n>>> ")
    moreInfo = moreInfo.upper()
    if moreInfo == 'S':
        print(output)
    else:
        print("Saindo...")


except:
    print("Erro, verifique se o nome do wifi foi digitado corretamente!!\n")
