"""Crie um programa que leia um número do usuário e determine se esse número é par ou ímpar.
"""
numero=int(input("Informe um número inteiro:\n"))
if (numero%2==1):
    print(f"O número {numero} é impar")
else:
    print(f"O número {numero} é par")