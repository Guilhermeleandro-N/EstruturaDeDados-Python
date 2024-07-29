rodoviaria=[[0,524,521,882],
            [524,0,434,586],
            [521,434,0,429],
            [882,586,429,0]]
while True:
    print("Insira o mesmo valor em sequência para finalizar o programa!")
    origem=(int(input("Qual a cidade de origem?\n1.  Vitória\n2. Nelo Horizonte\n3.  Rio de Janeiro\n4.  São Paulo\n")))-1
    destino=(int(input("Qual a cidade de destino?\n1.  Vitória\n2. Nelo Horizonte\n3.  Rio de Janeiro\n4.  São Paulo\n")))-1
    if (rodoviaria[origem][destino]!=0):
        print(f"Serão {rodoviaria[origem][destino]}km de viagem ")
        input("Aperte qualquer tecla para continuar.")
    else:
        break
print("Fim do programa!")