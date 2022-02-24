#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

salarioHora = float(input("Informe o seu salario por hora: "))
horasMensal = int(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = salarioHora*horasMensal

inss = salario_bruto*1.1-salario_bruto
fgts = salario_bruto*1.11-salario_bruto
sindicato = salario_bruto*1.03-salario_bruto
if salario_bruto <= 900:
    print("Isento de desconto")
elif salario_bruto <= 1500:
    ir = salario_bruto * 1.05 - salario_bruto
    total_descontos = ir + inss
    salario_liquido = salario_bruto - total_descontos - sindicato
    print("Salario Bruto", salario_bruto)
    print("Sindicato: ", sindicato)
    print("Valor imposto de renda: ", ir)
    print("Valor INSS: ", inss)
    print("Valor FGTS: ", fgts)
    print("Total de descontos: ", total_descontos)
    print("Salario Liquido: ", salario_liquido)
elif salario_bruto <=2500:
    ir = salario_bruto * 1.1 - salario_bruto
    total_descontos = ir + inss
    salario_liquido = salario_bruto - total_descontos - sindicato
    print("Salario Bruto", salario_bruto)
    print("Valor imposto de renda: ", ir)
    print("Valor INSS: ", inss)
    print("Valor FGTS: ", fgts)
    print("Total de descontos: ", total_descontos)
    print("Salario Liquido: ", salario_liquido)
else:
    ir = salario_bruto * 1.2 - salario_bruto
    total_descontos = ir + inss
    salario_liquido = salario_bruto - total_descontos - sindicato
    print("Salario Bruto", salario_bruto)
    print("Valor imposto de renda: ", ir)
    print("Valor INSS: ", inss)
    print("Valor FGTS: ", fgts)
    print("Total de descontos: ", total_descontos)
    print("Salario Liquido: ", salario_liquido)
