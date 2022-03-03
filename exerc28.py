# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
# limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
# desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
# usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
# pagamento, valor do desconto e valor a pagar.

tipo_carne = input("Informe o tipo de carne a ser comprada [File duplo, Alcatra, Picanha]: ").lower()
peso = float(input("Informe quantos quilos de carne serão comprados: "))
pagamento = input("O pagamento será feito no cartão Tabajara ou dinheiro? [Cartão Tabajara ou Dinheiro]: ").lower()

if tipo_carne == 'file duplo':
    if peso < 5:
        valor_total = peso * 4.9
    else:
        valor_total = peso * 5.8
elif tipo_carne == 'alcatra':
    if peso < 5:
        valor_total = peso * 5.9
    else:
        valor_total = peso * 6.8
if tipo_carne == 'picanha':
    if peso < 5:
        valor_total = peso * 6.9
    else:
        valor_total = peso * 7.8

desconto: float = (valor_total*1.1-valor_total)

if pagamento == 'cartão tabajara':
    valor_total = valor_total - desconto

print(f"O cliente comprou {peso} de {tipo_carne} e pagou com {pagamento}, teve desconto de {desconto} e valor total da compra foi de R$:{valor_total}")

