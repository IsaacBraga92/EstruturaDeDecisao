#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Informe o turno que você estuda. (M-matutino ou V-Vespertino ou N- Noturno): ").upper()

if turno == 'M':
    print("Turno Matutino")
elif turno == 'V':
    print("Turno Vespertino")
elif turno == 'N':
    print("Turno Noturno")
else:
    print("Invalido")