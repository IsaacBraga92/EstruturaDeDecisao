#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ").upper()

if letra.isalpha():

    if letra in 'A,E,I,O,U':
        print("A letra informada é uma vogal")
    else:
        print("A letra informada é uma consoante")

else:
    print("O caractere digitado não é uma letra!")
