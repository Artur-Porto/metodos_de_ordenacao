def bubble_sort(L):

    n = len(L)

    for i in range(n-1):
        for j in range(n - i - 1): 
            if L[j] > L[j+1]:
                aux = L[j]    
                L[j] = L[j+1]  
                L[j+1] = aux 

    return L

L=[5,4,3,2,1]
print(bubble_sort(L))
