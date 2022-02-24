#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# - Triângulo Equilátero: três lados iguais;
# - Triângulo Isósceles: quaisquer dois lados iguais;
# - Triângulo Escaleno: três lados diferentes;

ld1 = float(input("Informe o primeiro lado do triângulo: "))
ld2 = float(input("Informe o segundo lado do triângulo: "))
ld3 = float(input("Informe o terceiro lado do triângulo: "))

#Verificação se é um triângulo

if ld1+ld2 >ld3 and ld1+ld3>ld2 and ld2+ld3>ld1:
    print(f"As medidas {ld1,ld2,ld3} podem formar um triângulo!")
else:
    print(f"As medidas {ld1,ld2,ld3} não podem formar um triângulo!")

#Verificação do tipo do triângulo

if ld1==ld2 and ld2==ld3:
    print(f"As medidas {ld1,ld2,ld3}, formar um Triângulo Equilátero!")
elif ld1 != ld2 and ld2 != ld3 and ld3!=ld1:
    print(f"As medidas {ld1, ld2, ld3}, formar um Triângulo Escaleno!")
elif ld1==ld2 or ld1==ld3 or ld2==ld3:
    print(f"As medidas {ld1, ld2, ld3}, formar um Triângulo Isósceles!")
