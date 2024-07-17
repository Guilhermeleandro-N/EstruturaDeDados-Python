"""Crie um programa que leia uma lista de palavras do usuário e exiba somente as palavras que começam com a letra "a"."""
lista=[]
x=int(input("Quantas palavras você deseja informar?"))
for c in range(x):
    p=input("")
    lista.append(p)

print('As palavras digitadas que começam com "a" foram: ' )

for c in lista:
    if c[0]=="a":
        print(c)