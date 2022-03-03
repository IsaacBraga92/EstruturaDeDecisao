# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (
# resto da divisão).

numero = int(input("Digite um numero: "))

numero, resto = divmod(numero, 2)

if resto == 0:
    print("Número par!")
else:
    print("Numero impar")
