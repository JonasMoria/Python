
import random
import string

# Gerador de Senhas
print("\n=== Gerador de Senhas ===")

chars = ""

# Perguntando ao usuário o tipo de senha desejada
size = int(input("\nTamanho Da Senha: "))
lowerCase = input("Deseja adicionar Letras Minusculas? [s/n] \n>>>").lower()
upperCase = input("Deseja adicionar Letras Maiusculas? [s/n] \n>>>").lower()
numbers = input("Deseja adicionar Numeros? [s/n] \n>>>").lower()
simbols = input("Deseja adicionar Simbolos? [s/n] \n>>>").lower()


# Método para gerar a senha
def creatPass(size, chars, lower, upper, numbers, simbols):
    
    # Cores para formatação do texto
    RED   = "\033[1;31m" 
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"

    if size <= 0:
        print(RED+"Erro, Senha deve conter pelo menos 1 caractere"+RESET)
    if lower == 's':
        chars += string.ascii_lowercase
    if upper == 's':
        chars += string.ascii_uppercase
    if numbers == 's':
        chars += string.digits
    if simbols == 's':
        chars += "!@#%*()$?"

    rnd = random.SystemRandom()

    try:
        passwd = "".join(rnd.choice(chars) for i in range(size))
        return print("\nSENHA => "+ GREEN + str(passwd) + RESET)
    except:
        print(RED+"Erro, Selecione ao menos uma das opcoes!!"+RESET)



# Executando o método para criar senha
creatPass(size, chars, lowerCase, upperCase, numbers, simbols)