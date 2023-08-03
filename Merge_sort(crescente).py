def merge(lista_esquerda,lista_direita):
    n_esquerda=len(lista_esquerda)
    n_direita=len(lista_direita)
    #verificando os elementos das listas ate que uma das duas acabe
    i_esq=0
    i_dir=0
    lista_mesclada=[]
    while i_esq<n_esquerda and i_dir<n_direita :
        if lista_esquerda[i_esq]<=lista_direita[i_dir]:
            menor_valor=lista_esquerda[i_esq]
            i_esq=i_esq+1
        else:
            menor_valor=lista_direita[i_dir]
            i_dir=i_dir+1
        lista_mesclada.append(menor_valor)
    #preenchendo a lista mesclada com os valores restantes da lista ainda não acabada:
        if i_esq==n_esquerda:
            for i in range(i_dir,n_direita):
                lista_mesclada.append(lista_direita[i])
        if i_dir==n_direita:
            for i in range(i_esq,n_esquerda):
                lista_mesclada.append(lista_esquerda[i])
    return lista_mesclada

def merge_sort(L):
    n=len(L)
    if n==1:
        return L
    #dividir a Lista no meio
    ponto_medio=n//2
    lista_esquerda=L[0:ponto_medio]
    lista_direita=L[ponto_medio:n]
    #aplicar o algoritmo nas duas metades geradas
    lista_esquerda_ordenada=merge_sort(lista_esquerda)
    lista_direita_ordenada=merge_sort(lista_direita)
    #agrupar as listas ordenadas com o merge
    L=merge(lista_esquerda_ordenada, lista_direita_ordenada)
    return L
L=[5,4,3,2,1]
print(merge_sort(L))



