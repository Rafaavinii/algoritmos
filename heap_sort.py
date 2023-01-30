def montarHeap(arr, n):
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

def heapify(arr, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2 
 
    if esq < n and arr[maior] > arr[esq]:
        maior = esq
 
    if dir < n and arr[maior] > arr[dir]:
        maior = dir

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i] 
 
        heapify(arr, n, maior)

def heapSort(arr):
    n = len(arr)
 
    montarHeap(arr, n)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
