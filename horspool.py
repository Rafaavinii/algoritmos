def computarDeslocamento(P, m, D):
    for k in range(256): 
        D.append(m)
    for k in range(m - 1): 
        D[ord(P[k])] = m - k - 1
    print(D)

def Horspool(P, m, T, n):
    D = []
    computarDeslocamento(P, m, D)
    i = m-1
    index = -1

    while i <= n-1 and index == -1:
        k = 0
        while k <= m-1 and P[m-1-k] == T[i-k]:
            k += 1
        
        if k == m:
            index = i-m+1
        else:
            i = i + D[ord(T[i])]
    
    return index
