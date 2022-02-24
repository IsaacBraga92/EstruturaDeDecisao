#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual
#-salários até R$ 280,00 (incluindo) : aumento de 20%
#-salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#-salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#-salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#-o salário antes do reajuste;
#-o percentual de aumento aplicado;
#-o valor do aumento;
#-o novo salário, após o aumento.

salario = float(input("Informe o salario do servidor: "))

if salario <= 280.00:
    aumento = salario*1.2 - salario
    print(f"O salario antes do reajuste era: {salario}")
    print("Sofreu reajueste de 20%")
    print(f"O valor do aumento foi de: {aumento}")
    novo_salario = salario+aumento
    print(f"O novo salario é: {novo_salario}")
elif 280.00 < salario < 700.00:
    aumento = salario*1.15 - salario
    print(f"O salario antes do reajuste era: {salario}")
    print("Sofreu reajueste de 15%")
    print(f"O valor do aumento foi de: {aumento}")
    novo_salario = salario+aumento
    print(f"O novo salario é: {novo_salario}")
elif 700.00 < salario < 1500:
    aumento = salario * 1.1 - salario
    print(f"O salario antes do reajuste era: {salario}")
    print("Sofreu reajueste de 10%")
    print(f"O valor do aumento foi de: {aumento}")
    novo_salario = salario + aumento
    print(f"O novo salario é: {novo_salario}")
else:
    aumento = salario * 1.05 - salario
    print(f"O salario antes do reajuste era: {salario}")
    print("Sofreu reajueste de 5%")
    print(f"O valor do aumento foi de: {aumento}")
    novo_salario = salario + aumento
    print(f"O novo salario é: {novo_salario}")
