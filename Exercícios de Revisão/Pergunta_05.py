#5. Faça uma função exclua todas as chaves pares de uma lista
#encadeada. O valor de retorno deve ser o número de elementos
#excluídos. Faça um programa para testar a função implementada.

def exclua(lista_completa):
  lista_pares = []
  lista_impares = []

#percorra a lista
  for elemeto in lista_completa:
    if elemeto % 2 == 0: #se o elemento divide por dois e se resto e 0
     del elemeto # deletando elementos pares da lista
      
    else: # se não
     lista_impares.append(elemeto)

  print(lista_impares) # lista de elementos impares
  deletados= len(lista_completa)- len(lista_impares) # calculando quantidade de numeros pares deletados
  print("Quantidade deletada: %d " %deletados )


lista = [1,2,3,4,5,6,7,8,9,10]
exclua(lista)