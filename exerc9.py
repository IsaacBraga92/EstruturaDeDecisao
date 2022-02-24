#Faça um Programa que leia três números e mostre-os em ordem decrescente.

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
z = float(input("Digite o terceiro número: "))

print(f"Os números informados são: {x,y,z}")

if y>x:
    aux = x
    x=y
    y=aux
if z>x:
    aux = x
    x=z
    z=aux
if z>y:
    aux=y
    y=z
    z=aux

print(f"Os números em ordem decrescente ficam: {x,y,z}")
