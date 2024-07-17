"""Crie um programa que leia uma lista de números do usuário e exiba o produto desses números.
"""
lista=[]
cont=0
produto=1
x=int(input("Quantos números você ira informar? "))
for c in range(x):
    y=int(input("Informe um valor: "))
    lista.append(y)
    produto*=y
for c in lista:
    if cont<x-1:
        print(f"{c} X ", end="")
    elif cont<x:
        print(f" {c} =", end="")
    cont+=1
print(f" {produto}")