def BinarySearch(arr,l,h,x):
    while l<=h:
        mid = l + (h-l)//2
        
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            l = mid+1
        else :
            h = mid-1
    return -1
    
    
if __name__ == '__main__':
    arr =[2,4,3,6,7,5,9,12,10]
    target = 10
    high = len(arr)-1
    low = 0
    arr.sort()

    print("Sorted Array : ", arr)

    result = BinarySearch(arr,low,high,target)
    if result != -1:
        print("The elemet is found at position at :",result)
    else:
        print("The element is not found!")
#𝑂(log n)
