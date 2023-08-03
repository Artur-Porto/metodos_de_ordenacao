def quick_sort(L):
    n=len(L)
    if n<=1:
        return L
    pivo=L[n-1]
    sub_lista_da_esquerda=[]
    for i in range(n):
        if L[i]<pivo:
            sub_lista_da_esquerda.append(L[i])
    elementos_iguais_ao_pivo=[]
    for i in range(n):
        if L[i]==pivo:
            elementos_iguais_ao_pivo.append(L[i])
    sub_lista_da_direita=[]
    for i in range(n):
       if L[i]>pivo:
           sub_lista_da_direita.append(L[i])
    return quick_sort(sub_lista_da_esquerda)+elementos_iguais_ao_pivo+quick_sort(sub_lista_da_direita)
            
        
L=[5,4,3,2,1]
print(quick_sort(L))