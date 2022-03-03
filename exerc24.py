# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado
# da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
op = input("Informe a operação a ser realizada [+,-,*,/]: ")


def verificar():
    if resultado // 1 == resultado:
        print("Inteiro!")
        if resultado % 2 == 0:
            print("Par!")
            if resultado > 0:
                print("Positivo!")
            else:
                print("Negativo!")
        else:
            print("Impar!")
    else:
        print("Decimal!")

if op == '+':
    resultado = n1+n2
    print(f"O resultado da operação é {resultado}")
    verificar()
elif op == '-':
    resultado = n1-n2
    print(f"O resultado da operação é {resultado}")
    verificar()
elif op == '*':
    resultado =n1*n2
    print(f"O resultado da operação é {resultado}")
    verificar()
elif op == '/':
    resultado = n1/n2
    print(f"O resultado da operação é {resultado}")
    verificar()
else:
    print("Operação inválida")