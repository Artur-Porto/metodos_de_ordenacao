def selection_sort(L):

    n = len(L)
    for i in range(n-1):
          posicao_do_menor = i
          for j in range(i+1,n):                
                if L[j] < L[posicao_do_menor]:
                      posicao_do_menor = j
          aux = L[posicao_do_menor]
          L[posicao_do_menor] = L[i]
          L[i] = aux


    return L
L=[38, 26, 50, 37, 82, 55, 59, 34, 58, 31]
print(selection_sort(L))
