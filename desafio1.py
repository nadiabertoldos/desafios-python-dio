#quantidade_passos = int(input("Informe a quantidade de passos dados: "))

#if quantidade_passos < 0:
#    print("Informe um valor positivo")
#elif quantidade_passos == 0:
#    print ("Nenhum passo dado na floresta.")
#else:
#    for quantidade_passos in range(1, quantidade_passos+1):
#        if quantidade_passos == 1:
#            print(f"Explorador: {quantidade_passos} passo")
#        else: 
#            print(f"Explorador: {quantidade_passos} passos")



quantidade_passos = int(input())

def explorar(passos): 
    if passos < 0:
        print("Informe um valor positivo")
    elif passos == 0:
        print ("Nenhum passo dado na floresta.")
    else:
        for passos in range(1, passos+1):
            if passos == 1:
                print(f"Explorador: {passos} passo")
            else: 
                print(f"Explorador: {passos} passos")
                
saida = explorar(quantidade_passos)
