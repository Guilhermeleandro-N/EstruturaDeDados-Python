loteria=[["","x","x"],["","x",""],["x","",""],["x","","x"],
         ["x","x","x"],["","","x"],["x","x",""],["","","x"],
         ["","x",""],["x","x",""],["x","x","x"],["","x",""],
         ["","x",""],["x","x",""]]
vetTipoJogo=[0,0,0]
for l in loteria:
    aux=0
    for c in range(3):
       if l[c]=="x":
            aux+=1
    vetTipoJogo[aux-1]+=1
print(f"O número de...\nApostas simples foi {vetTipoJogo[0]}\nApostas duplas foi {vetTipoJogo[1]}\nApostas tripas foi {vetTipoJogo[2]}")
           

         
