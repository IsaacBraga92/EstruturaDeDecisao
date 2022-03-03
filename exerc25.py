# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita"
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
print("Responda SIM ou NAO para as perguntas")
telefone = input("Telefonou para a vítima?: ").upper()
local = input("Esteve no local do crime?: ").upper()
mora = input("Mora perto da vítima?: ").upper()
divida = input("Devia para a vítima?: ").upper()
trabalho = input("Já trabalhou com a vítima?: ").upper()

aux = 0
if telefone == 'SIM':
    aux += 1
if local == 'SIM':
    aux += 1
if mora == 'SIM':
    aux += 1
if divida == 'SIM':
    aux += 1
if trabalho == 'SIM':
    aux += 1

if aux == 2:
    print("Pessoa suspeita")
elif aux == 3 or aux == 4:
    print("Pessoa Cúmplice")
elif aux == 5:
    print("Pessoa Assassina")
else:
    print("Pessoa Inocente")
