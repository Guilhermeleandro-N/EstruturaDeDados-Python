"""Crie um programa que leia uma lista de números do usuário e exiba somente os números maiores do que 10.
"""
lista=[]
x=int(input("Quantos números você ira informar? "))
for c in range(x):
    y=int(input("Informe um valor: "))
    lista.append(y)
print("Os numeros maiores que 10 informados: ")
for c in lista:
    if c>10:
        print(c)