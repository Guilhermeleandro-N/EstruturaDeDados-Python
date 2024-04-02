import random 

def main():
    
    smaller= int(input("Informe o menor valor: "))
    larger = int(input("Informe o maior valor: "))
    myNumber = random.randint(smaller, larger)
    
    count = 0
    while True:
        count += 1
        userNumber = int(input("Qual seu chute? "))
        if userNumber<myNumber:
            print("Valor muito baixo!")
        elif userNumber>myNumber:
            print("Valor muito alto!")
        else:
            print(f"Você acertou em {count} tentativas!")
            break
          
if __name__ == "__main__":
    main()
        
