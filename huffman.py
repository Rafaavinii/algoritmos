def montarHeap(arr, n):
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

def heapify(arr, n, i):
    menor = i
    esq = 2 * i + 1
    dir = 2 * i + 2 
 
    if esq < n and arr[menor].freq > arr[esq].freq:
        menor = esq
 
    if dir < n and arr[menor].freq > arr[dir].freq:
        menor = dir

    if menor != i:
        arr[i], arr[menor] = arr[menor], arr[i] 
 
        heapify(arr, n, menor)

def removerHeap(a, n):
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



def inserirHeap(a, n, x):
    a.append(x)
    filho = n
    pai = (n-1) // 2

    while pai >= 0:
        if a[pai].freq > a[filho].freq:
            a[pai], a[filho] = a[filho], a[pai]
            filho = pai
            pai = (pai // 2)-1
        else:
            pai = -1

class No:
    def __init__(self, char, freq, esquerda=None, direita=None):
        self.char = char
        self.freq = freq
        self.esquerda = esquerda
        self.direita = direita
        self.cod = ''



def arvoreHuffman(S, f):
    #inserindo todos os simbolos no heap de acordo com a frequência
    heap = []
    for i in range(len(S)):
        no = No(S[i], f[i])
        inserirHeap(heap, len(heap), no)

    T = []
    while len(heap) > 1:
        X = removerHeap(heap, len(heap))
        Y = removerHeap(heap, len(heap))
        Z = No(None, X.freq + Y.freq)
        Z.esquerda = X
        Z.direita = Y

        X.cod = 0
        Y.cod = 1

        inserirHeap(heap, len(heap), Z)
    
    return heap

def criarTabCodigo(node, codific, cod=''):
    valor = cod + str(node.cod)

    if node.esquerda != None:
        criarTabCodigo(node.esquerda, codific, valor)
    if node.direita != None:
        criarTabCodigo(node.direita, codific, valor)
  
    if node.esquerda == None and node.direita == None:
        codific[node.char] = valor

    return codific

def codificar(texto, tabela):
    cod = ''
    for char in texto:
        cod = cod + tabela[char]
    
    return cod

letras = ['A', 'B', 'C', 'R', 'D']
freque = [5, 2, 1, 2, 1]

codific = {}
heap = arvoreHuffman(letras, freque)
tabela = criarTabCodigo(heap[0], codific)
texto = 'ABRACADABRA'
cod = codificar(texto, tabela)
print(tabela)
print(cod)
