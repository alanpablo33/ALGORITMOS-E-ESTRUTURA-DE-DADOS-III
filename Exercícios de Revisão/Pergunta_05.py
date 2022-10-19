#5. Faça uma função exclua todas as chaves pares de uma lista
#encadeada. O valor de retorno deve ser o número de elementos
#excluídos. Faça um programa para testar a função implementada.

class NodoLista:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
       return '%s -> %s' % (self.dado, self.proximo)

class ListaEncadeada:
    """Esta classe representa uma lista encadeada."""
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

def insere_no_inicio(lista, novo_dado):
    # 1) Cria um novo nodo com o dado a ser armazenado.
    novo_nodo = NodoLista(novo_dado)

    # 2) Faz com que o novo nodo seja a cabeça da lista.
    novo_nodo.proximo = lista.cabeca

    # 3) Faz com que a cabeça da lista referencie o novo nodo.
    lista.cabeca = novo_nodo


def insere_depois(lista, nodo_anterior, novo_dado):
    assert nodo_anterior, "Nodo anterior precisa existir na lista."

    # Cria um novo nodo com o dado desejado.
    novo_nodo = NodoLista(novo_dado)

    # Faz o próximo do novo nodo ser o próximo do nodo anterior.
    novo_nodo.proximo = nodo_anterior.proximo

    # Faz com que o novo nodo seja o próximo do nodo anterior.
    nodo_anterior.proximo = novo_nodo

def busca(lista, valor):
    corrente = lista.cabeca
    while corrente and corrente.dado != valor:
        corrente = corrente.proximo
    return corrente

def remove(self, valor):
    assert self.cabeca, "Impossível remover valor de lista vazia."

    # Nodo a ser removido é a cabeça da lista.
    if self.cabeca.dado == valor:
        self.cabeca = self.cabeca.proximo
    else:
        # Encontra a posição do elemento a ser removido.
        anterior = None
        corrente = self.cabeca
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo
        # O nodo corrente é o nodo a ser removido.
        if corrente:
            anterior.proximo = corrente.proximo
        else:
            # O nodo corrente é a cauda da lista.
            anterior.proximo = None

def countt(lista): 
    count = 0
    for x in lista: 
        if (x % 2 == 0): 
            count = count + 1
    print(count) 

global lista
lista = ListaEncadeada()
print("Lista vazia:", lista)

insere_no_inicio(lista, 5)
print("Lista contém um único elemento:", lista)

nodo_anterior = lista.cabeca
insere_depois(lista, nodo_anterior, 3)
insere_depois(lista, nodo_anterior, 10)
insere_depois(lista, nodo_anterior, 1)
insere_depois(lista, nodo_anterior, 8)
insere_depois(lista, nodo_anterior, 9)
insere_depois(lista, nodo_anterior, 12)

print("Inserindo um novo elemento depois de um outro:", lista)
print("\n")


l=[]
for i in range(20):
    elemento = busca(lista, i )
    if elemento:
        print("Elemento {0} presente na lista!".format(i))
    else:
        l.append(0)
        print("Elemento {0} não encontrado.".format(i))
    
print("\n")

print("Removendo elementos Pares:")
lista_pares =[]
lista_impa = []

for i in range(20):
        if i % 2 == 0:
            
            x= remove(lista, i)
            print("Removendo o elemento {0}: {1}".format(i, lista))
            lista_pares.append(1)


        else:
            lista_impa.append(i)
print("\n")
print("Sobra {0}: {1}".format(i, lista))


x=(len(lista_pares))
y=(20 - len(l))
print("Valores Pares Removidos: ")
print(x-y)



    








        

        

        


    


