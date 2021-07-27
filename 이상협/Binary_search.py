import math
NO_ELEMENT = 'NO_ELEMENT'



def b_search(list, target):
    size = len(list)
    if size < 1:
        return NO_ELEMENT
    mid = (size-1) >> 1
    if list[mid][1] == target:
        return list[mid][0]
    if list[mid][1] < target:
        return b_search(list[mid+1:],target)
    else:
        return b_search(list[:mid],target)



'''
def bin_search(A,target,low,high):
    if low > high:
        return NO_ELEMENT
    
    mid = math.ceil((low + high)/2)

    if target == A[mid]:
        return mid
    
    if target < A[mid]:
        return bin_search(A, target, low, mid - 1)
    else:
        return bin_search(A, target, mid + 1, high)


def bin_search1(A,target,low,high,t):
    if low > high:
        return NO_ELEMENT
    
    mid = math.ceil((low + high)/2)

    if target == A[mid][t]:
        return mid
    
    if target < A[mid][t]:
        return bin_search1(A, target, low, mid - 1,t)
    else:
        return bin_search1(A, target, mid + 1, high,t)
'''