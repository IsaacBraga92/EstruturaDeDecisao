#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir
#os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#A - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#B - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#C - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#D - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math

print("Vamos calcular uma equação de 2° Grau: ax2 + bx + c ")

a = float(input("Informe o valor de A: "))
if a ==0:
    print("A não pode ser igual a 0")
else:
    b = float(input("Informe o valor de B: "))
    c = float(input("Informe o valor de C: "))
    delta = b**2 -(4*a*c)
    if delta<0:
        print("Delta menor que 0, a equação não possui raizes reais")
    elif delta == 0:
        raiz = -b/(2*a)
        print("Delta igual a 0, a raiz é igual a: ", raiz)
    else:
        raiz1 = (-b + math.sqrt(delta))/(2*a)
        raiz2 = (-b - math.sqrt(delta))/(2*a)
        print(f"As raizes são respectivamente: {raiz1,raiz2} ")



