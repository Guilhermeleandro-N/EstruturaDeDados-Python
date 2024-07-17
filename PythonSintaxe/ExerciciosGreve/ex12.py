"""Crie um programa que leia uma lista de números do usuário e exiba somente os números ímpares.
"""
lista=[]
cont=0
x=int(input("Quantos números você ira informar?"))
for c in range(x):
    y=int(input("Informe um valor: "))
    lista.append(y)
for c in lista:
    if c%2==1:
        print(f"{c}")
