#7. Implemente um procedimento para inverter a ordem dos
#elementos de uma lista encadeada usando uma pilha. Faça um
#programa para testar a função implementada.

# Para Type annotation
from typing import List
import random

# Pilha de Numeros com type annotation
pilha: List[int] = []  # {1}

# Adicionando Numeros no topo da pilha
for n in range(0,10):
    pilha.append(int(input("Digite 10 numeros: "))) 
print("Numeros dentro da lista: ",pilha,"\n")
     
# Obtendo o elemento mais novo
#mostrando a Pilha
for n in pilha[::-1]:
    print("Mostrando na Pilha: ",n)

#ordem normal
print("Ordem Normal: ",pilha,"\n")

#ordem inversa
pilha.reverse()
print("Ordem Invertida: ",pilha)

#monstrando pilha
for n in pilha[::-1]:
    print("Mostrando na Pilha: ",n)