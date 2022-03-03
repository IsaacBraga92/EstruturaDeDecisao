#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.


dia = int(input("Digite um dia: "))
mes = int(input("Digite um mes: "))
ano = int(input("Digite um ano: "))

aux = True

if mes in [1,3,5,7,8,10,12]:
    if (dia<=31):
        aux = True
elif mes in [4,6,9,11]:
    if dia<=30:
        aux=True
elif mes in [2]:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if dia <=29:
            aux=True
    elif(dia>29):
        aux=True
if (aux):
    print(f"A data {dia}/{mes}/{ano} é válida")
else:
    print(f"A data {dia}/{mes}/{ano} é inválida")