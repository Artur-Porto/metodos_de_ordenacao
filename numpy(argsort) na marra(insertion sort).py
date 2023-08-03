

def arg_insertion_sort(L):

  n = len(L) # 1 Atribuição

  indices = list(range(n)) #######################################
  for i in range(1,n): #  n-1 Execuções

        id_nova_carta = i # n-1 Execuções

        while ( (id_nova_carta > 0) and (L[id_nova_carta] < L[id_nova_carta - 1]) ):
              # Como a lista já se encontra ordenada, esta malha nunca será utilizada

              # Efetuação de trocas ------------------------------------------------
              aux = L[id_nova_carta]
              L[id_nova_carta] = L[id_nova_carta - 1]
              L[id_nova_carta - 1] = aux

              aux = indices[id_nova_carta] ##############
              indices[id_nova_carta]     = indices[id_nova_carta - 1] #########
              indices[id_nova_carta - 1] = aux ##########
              #---------------------------------------------------------------------

              id_nova_carta -= 1 # Atualização da posição da carta na mão.
              
  return [L, indices]


L = [5,5,2,234,5,7,8,8,4345,3,22,32,454,5,46]
print("Lista original: ", L)
[L, I] = arg_insertion_sort(L)
print("Lista ordenada: ", L)
print("Indices (argsort): ", I)



