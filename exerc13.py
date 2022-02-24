#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

x = int(input("Informe do dia da semana (1-Domingo, 2-Segunda-Feira, 3-Terça-Feira, 4-Quarta-Feira, 5-Quinta-Feira, 6-Sexta-Feira, 7-Sábado): "))

if x == 1:
    print("Domingo")
elif x==2:
    print("Segunda-Feira")
elif x==3:
    print("Terça-Feira")
elif x==4:
    print("Quarta-Feira")
elif x==5:
    print("Quinta-Feira")
elif x==6:
    print("Sexta-Feira")
elif x==7:
    print("Sábado")
else:
    print("Inválido")
