def arg_quick_sort(L,indices = []):
    n=len(L)
    if n<=1:
        return L,indices ###
    
    if len(indices) == 0: ###
        indices = list(range(n)) ###
        
    pivo=L[n-1]
    #pivo_ind=indices[n-1] ###
    
    sub_lista_da_esquerda=[]
    sub_lista_ind_da_esquerda=[] ###
    
    for i in range(n):
        if L[i]<pivo:
            sub_lista_da_esquerda.append(L[i])
            sub_lista_ind_da_esquerda.append(indices[i]) ###
    elementos_iguais_ao_pivo=[]
    elementos_ind_iguais_ao_pivo=[] ###
    for i in range(n):
        if L[i]==pivo:
            elementos_iguais_ao_pivo.append(L[i])
            elementos_ind_iguais_ao_pivo.append(indices[i]) ###
    sub_lista_da_direita=[]
    sub_lista_ind_da_direita=[] ###
    for i in range(n):
       if L[i]>pivo:
           sub_lista_da_direita.append(L[i])
           sub_lista_ind_da_direita.append(indices[i]) ###
    lista_ordenada_esquerda, indices_esq = arg_quick_sort(sub_lista_da_esquerda, sub_lista_ind_da_esquerda)
    lista_ordenada_direita, indices_dir = arg_quick_sort(sub_lista_da_direita, sub_lista_ind_da_direita)

    return lista_ordenada_esquerda + elementos_iguais_ao_pivo + lista_ordenada_direita, indices_esq + elementos_ind_iguais_ao_pivo + indices_dir
                    
L=[5,5,2,234,5,7,8,8,4345,3,22,32,454,5,46]
[L,I]=arg_quick_sort(L)
print("L = ", L)
print("arg_quick_sort(L) = ", I)

