#3. Faça um programa que leia 10 números, armazene em um vetor
#e imprima o maior valor, o menor valor e a média.

lista = [] # lista

i = 0

while i < 10: # ira pedir 10 valores ao user
    valor = int(input("Insira valores a lista: ")) # inserindo valor
    lista.append(valor) # inserindo a lista
    i= i+1

print("Valores dentro da Lista")
print(lista)
print("\n")

print("Maior Valor")
print(max(lista)) # função max percorre a lista e traz o maior valor 
print("\n")
print("Menor Valor")
print(min(lista)) # unção min percorre a lista e traz o maior valor
print("\n")

soma = sum(lista) # função sum soma valores dentro de uma lista
divsao = soma / 10
print("A media dos Valores é: %d" %divsao)



