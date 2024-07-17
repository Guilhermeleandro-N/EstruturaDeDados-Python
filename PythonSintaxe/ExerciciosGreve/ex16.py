"""Crie um programa que leia uma lista de números do usuário e exiba a soma dos números pares.
"""
lista=[]
soma=0

x=int(input("Quantos números você ira informar? "))
for c in range(x):
    y=int(input("Informe um valor: "))
    if y%2==0:
        lista.append(y)
        soma+=y
print(f"A soma dos numeros pares informados: {lista} é {soma}.")