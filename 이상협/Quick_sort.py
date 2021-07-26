def partition(A, low, high):
    piv = A[high]
    i = low - 1
    for j in range (low, high):
        if A[j] < piv:
            i = i+1
            A[i], A[j] = A[j], A[i]
            print(A)
    
    A[i+1], A[high] = A[high], A[i+1]
    print(A)
    return i+1

def quickSort(A, low, high):
    if low < high:
        m = partition(A, low, high)
        print("m =",m)
        quickSort(A, low, m-1)
        quickSort(A, m+1, high)

