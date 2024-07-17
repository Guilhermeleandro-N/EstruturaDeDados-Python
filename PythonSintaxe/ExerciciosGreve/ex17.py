"""Crie um programa que leia uma lista de números do usuário e exiba a soma dos números ímpares."""
lista=[]
soma=0
x=int(input("Quantos números você ira informar? "))
for c in range(x):
    y=int(input("Informe um valor: "))
    if y%2==1:
        lista.append(y)
        soma+=y
print(f"A soma dos numeros ímpares informados: {lista} é {soma}.")