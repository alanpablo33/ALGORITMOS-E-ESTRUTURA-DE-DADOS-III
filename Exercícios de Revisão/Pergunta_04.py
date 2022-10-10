#4. Faça um programa que leia duas matrizes de tamanho 10x10 de
#dois arquivos .txt e calcule a soma das duas matrizes. Imprima a
#matriz resultante.

import random
import numpy as np

m1 = np.random.randint(1,100, (10,10))
print(m1)
print("\n")
m2 = np.random.randint(1,100, (10,10))
print(m2)

try:
    matrix1= open("Matrix1.txt", "w")
    matrix1.write("aaaaaaaaaa")

    matrix2= open("Matrix2.txt", "w")
    matrix2.write("5764843784734")
    
finally:
    matrix1.close
    matrix2.close
