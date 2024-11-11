def partition(arr, low, high):
    
    pivot = arr[high]     # Choose the pivot

    i = low - 1 # Index of smaller element and indicates the right position of pivot found so far 
    
    # Traverse arr[low..high] and move all smaller elements to the left side. Elements from low to i are smaller after every iteration
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    # Move pivot after smaller elements and return its position
    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    if low < high:
        
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        
        # Recursion calls for smaller elements and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)-1

    quickSort(arr, 0, n)
    
    for val in arr:
        print(val, end=" ") 