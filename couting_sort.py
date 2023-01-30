def countingSort(A, n, k):
	c = [0]*(k+1)

	for j in range(0, n):
		c[A[j]] = c[A[j]]+1

	c[0] = c[0]-1
	for i in range(1, k+1):
		c[i] = c[i] + c[i-1]
	
	B = [None]*len(A)
	for j in range(len(A)-1, -1, -1):
		B[c[A[j]]] = A[j]
		c[A[j]] = c[A[j]]-1
	
	return B
