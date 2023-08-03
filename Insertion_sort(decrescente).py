def insertion_sort_dec(L):

  n = len(L)

  for i in range(1,n): #  Não precisa considerar o caso i = 0, pois seria a 
                       # primeira carta apanhada do maço, sendo impossível
                       # realizar qualquer comparação.

        id_nova_carta = i #  Os elementos L[0],L[1],...,L[i-1] representam a mão do
                      # jogador, enquanto que L[i] é a nova carta que queremos
                      # alocar na mão já ordenada.

        while ( (id_nova_carta > 0) and (L[id_nova_carta] > L[id_nova_carta - 1]) ):

              # Efetuação de trocas ------------------------------------------------
              aux = L[id_nova_carta]
              L[id_nova_carta] = L[id_nova_carta - 1]
              L[id_nova_carta - 1] = aux
              #---------------------------------------------------------------------

              id_nova_carta -= 1 # Atualização da posição da carta na mão.

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
retorno       = insertion_sort_dec(lista_4)
tempo_final   = time()

print("Tempo gasto para executar f:", tempo_final - tempo_inicial, "segundos.")