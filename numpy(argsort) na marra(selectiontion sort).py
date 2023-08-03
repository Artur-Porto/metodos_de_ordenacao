def arg_selection_sort(L):

    n = len(L)
    indices = list(range(n))
    for i in range(n-1):
          posicao_do_menor = i
          for j in range(i+1,n):                
                if L[j] < L[posicao_do_menor]:
                      posicao_do_menor = j
          aux = L[posicao_do_menor]
          L[posicao_do_menor] = L[i]
          L[i] = aux

        #--------------------------------------------------- 
          aux = indices[posicao_do_menor] 
          indices[posicao_do_menor]     = indices[i] 
          indices[i] = aux 
        #--------------------------------------------

    return L,indices

L = [5,5,2,234,5,7,8,8,4345,3,22,32,454,5,46]
print("Lista original: ", L)
[L,I] = arg_selection_sort(L)
print("Lista ordenada: ", L)
print("Indices (argsort): ", I)




