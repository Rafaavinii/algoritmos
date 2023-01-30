def particao(A, esquerda, direita):

    pivo = A[esquerda]

    i = esquerda
    j = direita
    while i <= j:

        while A[i] <= pivo:
            i += 1
            if i == direita:
                break


        while pivo <= A[j]:
            j -= 1
            if j == esquerda:
                break


        if i >= j:
            break


        A[i], A[j] = A[j], A[i]


    pivo, A[j] = A[j], pivo


    return j

def quicksort(A, esquerda, direita):
    if esquerda < direita:
        indice_pivo = particao(A, esquerda, direita)
        quicksort(A, esquerda, indice_pivo - 1)
        quicksort(A, indice_pivo + 1, direita)
