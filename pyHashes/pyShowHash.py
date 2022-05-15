
import hashlib

print('\n=== PY GERADOR DE HASHES ===')

msg = input("\nMENSAGEM: ")

# Métodos para criar hashes


def sha512(msg):
    return hashlib.sha512(str(msg).encode("utf-8")).hexdigest()


def sha256(msg):
    return hashlib.sha256(str(msg).encode("utf-8")).hexdigest()


def sha1(msg):
    return hashlib.sha1(str(msg).encode("utf-8")).hexdigest()


def md5(msg):
    return hashlib.md5(str(msg).encode("utf-8")).hexdigest()


# Menu Selecionar tipo de Hash
option = 0
while option < 5:
    print("\nSelecione o algoritmo de Hash Desejado: ")
    print("1) SHA-512")
    print("2) SHA-256")
    print("3) SHA-1")
    print("4) MD5")
    print("5) SAIR")
    option = int(input(">>> "))

    # Executando o Hash
    match option:
        case 1:
            print(sha512(msg))
        case 2:
            print(sha256(msg))
        case 3:
            print(sha1(msg))
        case 4:
            print(md5(msg))
        case 5:
            print("Saindo...")
