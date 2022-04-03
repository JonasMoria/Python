
import os

repetir = "S"

while repetir == "S":

    print("\n=== PY PING ===")
    ip_host = input("IP/HOST => ")
    
    #Executando o Ping
    os.system('ping -n 6 {}'.format(ip_host))

    repetir = input("Executar Novamente?[S/N] => ").upper()
    if repetir == "N":
        break
print("....")