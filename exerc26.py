# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro, acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro, acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
# que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litro_alcool = 1.90
litro_gasolina = 2.50

quantidade_litro = int(input("Digite a quantidade de litros a serem compradas: "))
tipo_combustivel = input("Informe o tipo de combustível a ser comprado G-GASOLINA ou A-ÁLCOOL: ").upper()

if tipo_combustivel == 'G':
    valor_total = quantidade_litro * litro_gasolina
    print(f"O valor total da compra é {valor_total}")
elif tipo_combustivel == 'A':
    valor_total = quantidade_litro * litro_alcool
    print(f"O valor total da compra é {valor_total}")
else:
    print("Tipo de combustível não reconhecido!")
