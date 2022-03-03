#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

n1 = int(input("Informe a primeira nota do aluno: "))
n2 = int(input("Informe a segunda nota do aluno: "))
n3 = int(input("Informe a terceira nota do aluno: "))
media = (n1+n2+n3)/3

if media ==10:
    print(f"Aluno obteve a media {media}!")
    print("Aluno Aprovado com distinção!")
elif 7 < media < 10:
    print(f"Aluno obteve a media {media}!")
    print("Aluno Aprovado!")
elif media <7:
    print(f"Aluno obteve a media {media}!")
    print("Aluno Reprovado!")
