"""Crie um programa que leia uma lista de números do usuário e exiba o maior número dessa lista.
"""
x=int(input("Quantos números você ira informar: "))
lista=[]
for c in range(x):
    n=float(input("Informe o valor:"))
    lista.append(n)
lista.sort()
print(f"O menor valor informado é {lista[0]}.")