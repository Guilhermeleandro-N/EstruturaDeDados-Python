vet=[0]*10
par=[]
impar=[]
for c in range(10):
    vet[c]=int(input("Informe um valor: "))
for c in range(10):
    if vet[c]%2==0:
        par.append(vet[c])
    else:
        impar.append(vet[c])
for c in range(10):
    print(f"O valor no vetor de indice {c}: {vet[c]}")
for c in range(len(par)):
    print(f"{c+1} valor par informado: {par[c]} ")
for c in range(len(impar)):
    print(F"{c+1} valor impar informado: {impar[c]} ")
