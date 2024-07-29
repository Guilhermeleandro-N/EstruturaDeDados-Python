notas=[0]*10
soma=0
for c in range(10):
    notas[c]=float(input(f"Valor da nota do aluno {c+1}: "))
for c in notas:
    soma+=c
media=soma/10
print(f"A soma das notas de todos os alunos foi: {round(soma,2)}.\nA media das notas dos dez alunos foi: {round(media,2)}!")