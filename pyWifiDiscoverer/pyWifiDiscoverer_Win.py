
import subprocess

print('\n===DESCOBRIDOR DE SENHAS WIFI SALVAS===')


while True:
    try:
        # Capturando informações das redes Wifi salvas
        informations = subprocess.check_output([
            "netsh", "wlan", "show", "profiles"
        ], encoding='cp860')
        print(informations)

        # Perguntando ao usuário qual wifi ele deseja ver a senha
        print("\nDigite \"exit\" para cancelar!")
        wifi_name = input("Digite o Nome Do Wifi Desejado: ")
        if wifi_name == "exit":
            print("Saindo...")
            break
        
        # Capturando informações da rede wifi selecionada
        output = subprocess.check_output([
            "netsh", "wlan", "show", "profile", wifi_name, "key" "=" "clear"
        ], encoding='cp858')
        
        # Capturando a senha salva
        for lines in output.split('\n'):
            if "Conteúdo da Chave" in lines:
                # capturando a senha
                position = lines.find(":")
                password = lines[position+2:]
                # exibindo a senha
                print("Senha ==> "+password)
        moreInfo = input(
            "Deseja ver Informações completas deste wifi?[s/n]: \n>>> ")
        moreInfo = moreInfo.upper()
        if moreInfo == 'S':
            print(output)
    except:
        print("Erro, verifique se o nome do wifi foi digitado corretamente!!\n")
