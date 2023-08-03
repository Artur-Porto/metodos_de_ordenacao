def merge(lista_esquerda, ind_e, lista_direita, ind_d):

  n_esquerda = len(lista_esquerda)
  n_direita  = len(lista_direita)

  i_esq = 0
  i_dir = 0
  lista_mesclada  = []
  indice_mesclado = [] ###
  while i_esq < n_esquerda and i_dir < n_direita:

      id = -1 ###
      if lista_esquerda[i_esq] <= lista_direita[i_dir]:
          menor_valor = lista_esquerda[i_esq]
          id = ind_e[i_esq] ###
          i_esq = i_esq + 1
      else:
          menor_valor = lista_direita[i_dir]
          id = ind_d[i_dir] ###
          i_dir = i_dir + 1

      lista_mesclada.append(menor_valor)
      indice_mesclado.append(id) ###

  for i in range(i_esq, n_esquerda): 
      lista_mesclada.append(lista_esquerda[i])
      indice_mesclado.append(ind_e[i]) ###

  for i in range(i_dir, n_direita):
      lista_mesclada.append(lista_direita[i])
      indice_mesclado.append(ind_d[i]) ###

  return lista_mesclada, indice_mesclado ###

def arg_merge_sort(L, indices = []): ###

  n = len(L)

  if n <= 1:
    return L, indices ###

  if len(indices) == 0: ###
    indices = list(range(n)) ###

  ponto_medio = n // 2

  lista_esquerda = L[0:ponto_medio]
  lista_direita  = L[ponto_medio:n]

  ind_e = indices[0:ponto_medio] ###
  ind_d = indices[ponto_medio:n] ###

  lista_esquerda_ordenada, ind_e_ord = arg_merge_sort(lista_esquerda, ind_e) ###
  lista_direita_ordenada, ind_d_ord  = arg_merge_sort(lista_direita, ind_d) ###

  L, indices = merge(lista_esquerda_ordenada, ind_e_ord, lista_direita_ordenada, ind_d_ord) ###

  return L, indices ###

L=[5,5,2,234,5,7,8,8,4345,3,22,32,454,5,46]
[L, ind] = arg_merge_sort(L)
print("L = ", L)
print("arg_merge_sort(L) = ", ind)

