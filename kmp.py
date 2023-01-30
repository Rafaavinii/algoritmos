def ComputaNext(P, k, next):
    next[0] = 0
    next[1] = 0

    for i in range(2, k):
        j = next[i-1]
        while P[i] != P[j] and j > 0:
            j = next[j]
            next[i] = j


def KMP(T, n, P, m):

	next = [0]*m

	ComputaNext(P, m, next)

	j = 0
	i = 0
	index = -1

	while index == -1 and i < n:

		if P[j] == T[i]:
			i += 1
			j += 1

		else:

			j = next[j-1]
			if j == 0:
				j = 1
				i +=1

		if j == m:
			index = i-m
	
	return index
