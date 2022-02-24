# Faça um Programa que leia três números e mostre o maior e o menor deles.

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
z = float(input("Digite o terceiro número: "))
maior = x
menor = x
# encontrando o maior
if x > y and x > z:
    maior = x
elif y > x and y > z:
    maior = y
else:
    maior = z
# encontrando o menor
if x < y and x < z:
    menor = x
elif y < x and y < z:
    menor = y
else:
    menor = z

print(f"Os números informados são, {x, y, z}")
print("O maior número é: ", maior)
print("O menor número é: ", menor)
