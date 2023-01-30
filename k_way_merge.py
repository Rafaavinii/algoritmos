def montarHeap(arr, n):
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

def heapify(arr, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2 

    if esq < n and arr[maior][0] >= arr[esq][0]:
        maior = esq

    if dir < n and arr[maior][0] >= arr[dir][0]:
        maior = dir

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i] 

        heapify(arr, n, maior)

def inserirHeap(a, n, x):
    a.append(x)
    filho = n
    pai = (n-1) // 2

    while pai >= 0:
        if a[pai][0] >= a[filho][0]:
            a[pai], a[filho] = a[filho], a[pai]
            filho = pai
            pai = (pai // 2)-1
        else:
            pai = -1

def RemoveMaxHeap(a, n):
    if n == 0:
        return "heap vazio"

    else:
        aux = a[0]
        a[0] = a[n-1]
        a[n-1] = aux
        z = a.pop()
        n = n-1
        heapify(a, n, 0)
        return z

def k_way_merge(lista):
 
    ordenados = []
    
    while lista:
        v = RemoveMaxHeap(lista, len(lista))
        key = v.pop(0)
        ordenados.append(key)
        if len(v) > 0:
            inserirHeap(lista, len(lista), v)


    return ordenados

lista = [[1, 5, 8], [8, 9, 9, 10, 20], [3, 7, 8, 9, 11], [2, 5, 8, 9, 20]]
print(k_way_merge(lista))
