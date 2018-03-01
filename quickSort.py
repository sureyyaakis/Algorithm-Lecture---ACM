""" This function takes last element as pivot, places the pivot element at its correct position in sorted array, 
and places all smaller (smaller than pivot)to left of pivot and all greater elements to right of pivot """

def quicksort(x):
	if len(x) < 2:
		return x
	else:
		pivot = x[0]
		less = [i for i in x[1:] if i <= pivot] # First element from the list(x)
		greater = [i for i in x[1:] if i > pivot] # Last element from the list(x)
		return quicksort(less) + [pivot] + quicksort(greater)

x = [1, 2, 3, 5, 4, 2, 7, 14, 4, 19, 9]
print(quicksort(x))
