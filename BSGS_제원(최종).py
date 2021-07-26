import math

NO = 'NO'

def xgcd(a,p):
    t0, t1 = a, p
    u0, u1 = 1, 0

    while(t1 != 0):
        t2, t0 = t0 , t1
        q, t1 = t2 // t1, t2 % t1
        u2, u0 = u0, u1
        u1 = u2 - q * u1
    if(u0 < 0):
        u0 = u0 + p
    return u0


# partition(A: array, low 배열의 첫 번째 원소, high 배열의 마지막 원소)
def partion(A, l, h):
    pivot = A[h][1]
    i = l - 1

    for j in range(l, h):
        if(A[j][1] < pivot):
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[h] = A[h], A[i+1]
    return i + 1

def qSort(A, l, h):
    if(l < h):
        m = partion(A, l, h)
        qSort(A, l, m-1)
        qSort(A, m + 1, h)

def binSearch(A, t, l, h):
    if(l > h):
        return NO

    m = (l + h) // 2

    if(t == A[m][1]):
        return A[m]

    if(t < A[m][1]):
        return binSearch(A, t, l, m-1)
    else:
        return binSearch(A, t, m+1, h)











def bsgs(g, h, n):  # bsgs(generator g, element h, order n)
    m = 1 + math.floor(math.sqrt(n))
    print("m=",m)
    
    l, tmp = [], 1

    for i in range(0, m):
        l.append([i, tmp])
        tmp = tmp * g % n

    print("L:", l)          # Show the L
    
    qSort(l, 0, len(l)-1)   # Sorting

    print("Sorted L:", l)   # Show the sorted L
    
    inv = xgcd(g, n) % n    # inv: inverse of g
    w = (inv ** m) % n
    tmp = h

    for j in range(0, m):
        c = binSearch(l, tmp, 0, len(l)-1)
        if(c[1] == tmp):
            i = c[0]
            print("Collision of Baby-Step ({}, {})".format(i, g**i))
            print("Collision of Giant-Step ({}, {})".format(j, tmp))

            return (i + j*m) % n
        else:
            tmp = tmp * w % n

print(bsgs(2, 61, 101))

print(bsgs(11, 12, 1009))

print(bsgs(2, 399, 773))
