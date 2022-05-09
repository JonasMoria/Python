from email import message
import socket

strCon = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("\nSocket Criado com Sucesso!!")

host = 'localhost'
porta = 5432

strCon.bind((host, porta))
mensagem = 'Servidor: Olá,Cliente!'

while 1:
    dados, end = strCon.recvfrom(4096)
    if dados:
        print("enviando mensagem...")
        strCon.sendto(dados+(mensagem.encode()), end)
