def buscaBinaria(A, esquerda, direita, item):

    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    
    if A[meio] == item:
        return meio

    elif A[meio] > item:
        return buscaBinaria(A, esquerda, meio - 1, item)
    else:
        return buscaBinaria(A, meio + 1, direita, item)
