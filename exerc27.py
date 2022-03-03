# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
# R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo
# para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
# e escreva o valor a ser pago pelo cliente.


peso_morango = float(input("Informe a quantidade em quilos de morango comprado: "))
peso_maca = float(input("Informe a quantidade em quilos de maçã comprado: "))

if peso_morango < 5:
    valor_morango = peso_morango * 2.5
else:
    valor_morango = peso_morango * 2.2

if peso_maca < 5:
    valor_maca = peso_maca * 1.8
else:
    valor_maca = peso_maca * 1.5

valor_total = valor_maca + valor_morango
peso_total = peso_maca + peso_morango
if valor_total >= 25 or peso_total >= 8:
    valor_total = valor_total - (valor_total * 1.1 - valor_total)

print(f"O cliente comprou {peso_morango} quilos de morango, {peso_maca} quilos de maça, num peso total de {peso_total}.")
print(f"Num valor total de R$:{valor_total} de reais")
