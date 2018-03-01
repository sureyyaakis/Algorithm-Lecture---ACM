""" This function takes last element as pivot, places the pivot element at its correct position in sorted array, 
and places all smaller (smaller than pivot)to left of pivot and all greater elements to right of pivot """

def partition(arr,low,high):
	i = ( low-1 )		   # index of smaller element
	pivot = arr[high]	 # pivot

	for j in range(low , high):
	  if arr[j] <= pivot:
	    i = i+1
	    arr[i],arr[j] = arr[j],arr[i]

	arr[i+1],arr[high] = arr[high],arr[i+1]
	return ( i+1 )

def quickSort(arr,low,high):
	if low < high:

		# newpivot is partitioning index, arr[p] is now
		# at right place
		newpivot = partition(arr,low,high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, newpivot-1)
		quickSort(arr, newpivot+1, high)

arr = [10, 7, 8, 9, 1, 5, 101, 22, 9]
n = len(arr)
a = quickSort(arr,0,n-1)

print(arr)
