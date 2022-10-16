#6. Faça uma função que divida uma fila em duas outras filas, uma
#contendo elementos de chave par e outra de chave ímpar. Faça um
#programa para testar a função implementadas.


def filas(fila):
    
    fila_impare= [] 
    fila_pares= []

    for elemeto in fila:
        if elemeto % 2 == 0: #se o elemento divide por dois e se resto e 0
            fila_pares.append(elemeto)
      
        else: # se não
            fila_impare.append(elemeto)
    print(fila)
    print(fila_impare)
    print(fila_pares)
    


fila_test = [1,2,3,4,5,6,7,8,9,10]
#x=12

#while x > len(fila_test):
#    elemet = input("Digite um Numero: ")
#    fila_test.append(elemet)   

filas(fila_test)
