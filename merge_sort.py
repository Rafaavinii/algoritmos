def mergeSort(x, esq, dir):
	if esq < dir:
		meio = (esq + dir) // 2

		mergeSort(x, esq, meio)
		mergeSort(x, meio + 1, dir)
		intercala(x, esq, meio, dir)
		
def intercala(x, esq, meio, dir):
	tamA = meio - esq + 1
	tamB = dir - meio

	left = [0] * (tamA)
	right = [0] * (tamB)

	for i in range(0, tamA):
		left[i] = x[esq + i]

	for j in range(0, tamB):
		right[j] = x[meio + 1 + j]

	i = 0
	j = 0
	k = esq

	while i < tamA and j < tamB:
		if left[i] <= right[j]:
			x[k] = left[i]
			i += 1
		else:
			x[k] = right[j]
			j += 1
		k += 1


	while i < tamA:
		x[k] = left[i]
		i += 1
		k += 1

	while j < tamB:
		x[k] = right[j]
		j += 1
		k += 1
