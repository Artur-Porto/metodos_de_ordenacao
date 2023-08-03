def arg_bubble_sort(L):

    n = len(L)
    indices = list(range(n))
    for i in range(n-1):
        for j in range(n - i - 1): 
            if L[j] > L[j+1]:
                aux = L[j]    
                L[j] = L[j+1]  
                L[j+1] = aux 
               #--------------------------------------------------- 
                aux = indices[j] 
                indices[j]     = indices[j + 1] 
                indices[j +1] = aux 
              #--------------------------------------------
    return [L,indices]

L = [5,5,2,234,5,7,8,8,4345,3,22,32,454,5,46]
print("Lista original: ", L)
[L,I] = arg_bubble_sort(L)
print("Lista ordenada: ", L)
print("Indices (argsort): ", I)






