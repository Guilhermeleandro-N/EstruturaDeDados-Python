"""Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem decrescente.
"""
lista=[]
lista=[]
x=int(input("Quantos números você ira informar? "))
for c in range(x):
    y=int(input("Informe um valor: "))
    lista.append(y)
lista.sort(reverse=True)
print(lista)