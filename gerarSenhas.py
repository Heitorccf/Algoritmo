import random

def generatePassword(pwlength):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    senhas = []

    for cont in pwlength:
        
        senha = "" 
        for cont2 in range(cont):
            next_letter_index = random.randrange(len(alphabet))
            senha = senha + alphabet[next_letter_index]
        
        senha = replaceWithNumber(senha)
        senha = replaceWithUppercaseLetter(senha)
        
        senhas.append(senha) 
    
    return senhas


def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword


def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        return pword



def main():
    
    numPasswords = int(input("Quantas senhas você deseja gerar? "))
    
    print("Gerando " +str(numPasswords)+" senhas")
    
    passwordLengths = []

    print("Mínimo de três caracteres")

    for i in range(numPasswords):
        length = int(input("Tamanho da senha #" + str(i+1) + " "))
        if length<3:
            length = 3
        passwordLengths.append(length)
    
    
    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print ("Senha #"+str(i+1)+" = " + Password[i])



main()