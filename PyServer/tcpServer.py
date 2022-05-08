
from distutils.log import error
import socket
from sqlite3 import connect
import sys


def main():
    try:
        strCon = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print("Falha Na Conexao ")
        print("Erro: {}".format(error))
        sys.exit()


    print("\nSocket Criado com Sucesso!!")


    hostAlvo = input("Host: ")
    portaAlvo = input("Porta: ")

    try:
        strCon.connect((hostAlvo, int(portaAlvo)))
        print("Cliente TCP conectado com sucesso no host: " +
            hostAlvo+" na porta: "+portaAlvo)
        strCon.shutdown(2)
    except socket.error as error:
        print("Erro ao Conectar ao host "+hostAlvo+" Na porta "+portaAlvo)
        print("Erro: {}".format(error))
        sys.exit()

if __name__ == "__main__":
    main()

