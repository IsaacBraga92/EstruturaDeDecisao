#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
x = float(input("Digite o valor do primeiro produto: "))
y = float(input("Digite o valor do segundo produto: "))
z = float(input("Digite o valor do terceiro produto: "))

menor = x
# encontrando o menor
if x < y and x < z:
    menor = x
elif y < x and y < z:
    menor = y
else:
    menor = z

print(f"Os valores informados são, {x, y, z}")

print("O valor do menor produto é: ", menor)

