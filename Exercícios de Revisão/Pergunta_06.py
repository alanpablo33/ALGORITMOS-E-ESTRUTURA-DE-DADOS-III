#6. Faça uma função que divida uma fila em duas outras filas, uma
#contendo elementos de chave par e outra de chave ímpar. Faça um
#programa para testar a função implementadas.

from collections import deque

fila1=deque([])
fila2=deque([])
fila=deque([])

for i in range(10):
    x = int(input("Digite os 10 Valores Numericos: "))
    fila.append(x)

    if x %2==0:
        fila2.append(x)
        
    else:
        fila1.append(x)
        
print("Todos os Elementos da FILA: ", fila)
print("Adicionando um elemento a fila PAR: ", fila2)
print("Adicionando um elemento a fila IMPAR: ", fila1)

#remoção de valores da Fila
#Primeiros a Chegar , Primeiros a Sair
fila.popleft()
fila.popleft()
