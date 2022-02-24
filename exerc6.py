#Faça um Programa que leia três números e mostre o maior deles.

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
z = float(input("Digite o terceiro número: "))

if x>y and x>z:
    print(f"O número {x}, é maior que {y} e {z}")
elif y>x and y>z:
    print(f"O número {y}, é maior que {x} e {z}")
else:
    print(f"O número {z}, é maior que {y} e {x}")
