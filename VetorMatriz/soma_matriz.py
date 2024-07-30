rodoviaria=[[0,524,521,882],
            [524,0,434,586],
            [521,434,0,429],
            [882,586,429,0]]
soma_sup=0
soma_inf=0
for c in range(4):
    print("")
    for l in range (4):
        if l>c:
            soma_sup+=rodoviaria[c][l]            
        elif c>l:
            soma_inf+=rodoviaria[c][l]        
print(f"\nSoma do triangulo superior: {soma_sup}\nSoma do triangulo inferior: {soma_inf}")
