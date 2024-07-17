"""Crie um programa que leia uma lista de números do usuário e exiba somente os números menores do que 5.
"""
lista=[]
x=int(input("Quantos números você ira informar? "))
for c in range(x):
    y=int(input("Informe um valor: "))
    lista.append(y)
print("Os numeros menores que 5 informados: ")
for c in lista:
    if c<5:
        print(c)