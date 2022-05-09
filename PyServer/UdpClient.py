
from email.policy import strict
import socket

strCon = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket Criado com Sucesso!!")

host = 'localhost'
porta = 5433
mensagem = 'Olá,Servidor!!'

try:
    print("Cliente: "+mensagem)
    strCon.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = strCon.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: "+dados)
finally:
    print("Cliente: Saindo....")
    strCon.close()
