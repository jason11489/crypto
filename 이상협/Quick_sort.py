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

def quick_sort(A, low, high):
    if low < high:
        m = partition(A, low, high)
        print("m =",m)
        quick_sort(A, low, m-1)
        quick_sort(A, m+1, high)
    return A




def partition1(A,low,high,r):
    pivot = A[high][r]
    i = low - 1
    for j in range(low,high):
        if A[j][r]<pivot:
            i += 1
            A[i],A[j]=A[j],A[i]
            #if i!= j:
             #   print(A)
    A[i+1],A[high]=A[high],A[i+1]
    #if i+1 != high:
        #print(A)
    return i+1

def quick_sort1(A,low,high,r):
    if low<high:
        m = partition1(A,low,high,r)
        #print('m = ',m)
        quick_sort1(A,low,m-1,r)
        quick_sort1(A,m+1,high,r)
    return A
