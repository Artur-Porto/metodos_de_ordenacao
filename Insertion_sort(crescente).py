def insertion_sort(L):

  n = len(L)

  for i in range(1,n): #  Não precisa considerar o caso i = 0, pois seria a 
                       # primeira carta apanhada do maço, sendo impossível
                       # realizar qualquer comparação.

        id_nova_carta = i #  Os elementos L[0],L[1],...,L[i-1] representam a mão do
                      # jogador, enquanto que L[i] é a nova carta que queremos
                      # alocar na mão já ordenada.

        while ( (id_nova_carta > 0) and (L[id_nova_carta] < L[id_nova_carta - 1]) ):

              # Efetuação de trocas ------------------------------------------------
              aux = L[id_nova_carta]
              L[id_nova_carta] = L[id_nova_carta - 1]
              L[id_nova_carta - 1] = aux
              #---------------------------------------------------------------------

              id_nova_carta -= 1 # Atualização da posição da carta na mão.

  return L

L=[5,4,3,2,1]
print(insertion_sort(L))