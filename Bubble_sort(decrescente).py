def bubble_sort_dec(L):

    n = len(L)

    for i in range(n-1):
        for j in range(n - i - 1): 
            if L[j] < L[j+1]:
                aux = L[j]    
                L[j] = L[j+1]  
                L[j+1] = aux 

    return L
from time import time
from numpy import random as rd

lista_0 = list(rd.uniform(-1,1,10))
lista_1 = list(rd.uniform(-1,1,100))
lista_2 = list(rd.uniform(-1,1,1000))
lista_3 = list(rd.uniform(-1,1,10000))
lista_4 = list(rd.uniform(-1,1,100000))
lista_5 = list(rd.uniform(-1,1,1000000))
lista_6 = list(rd.uniform(-1,1,10000000))

tempo_inicial = time()
retorno       = bubble_sort_dec(lista_2)
tempo_final   = time()

print("Tempo gasto para executar f:", tempo_final - tempo_inicial, "segundos.")


