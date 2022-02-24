#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
#a sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento    Conceito:
#Entre 9.0 e 10.0           A
#Entre 7.5 e 9.0            B
#Entre 6.0 e 7.5            C
#Entre 4.0 e 6.0            D
#Entre 4.0 e ZERO           E

n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
print(f"As notas foram: {n1,n2}")
media = (n1+n2)/2
print("A media do aluno é: ", media)
if media>=9.0:
    print("O conceito do aluno é A!")
    print("Aprovado!")
elif 7.5 <= media < 9.0:
    print("O conceito do aluno é B!")
    print("Aprovado!")
elif 6.0 <= media <7.5:
    print("O conceito do aluno é C!")
    print("Aprovado!")
elif 4.0 <= media <6.0:
    print("O conceito do aluno é D!")
    print("Reprovado!")
else:
    print("O conceito do aluno é E!")
    print("Reprovado!")
