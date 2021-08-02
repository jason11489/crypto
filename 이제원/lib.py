'''
1. xgcd()
2. qsort()
3. binSearch()
4. crt()

'''

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


# crt(r개의 임의의 정수들이 모인 리스트, m: r개의 쌍으로 서로소인 모듈러값을 모아놓은 리스트).
def crt(a, m):
    M, x = 1, 0
    MM = inv =[0]

    # 연립선형합동식의 개수.
    r = len(a)

    # M: r개의 모듈러값 [m1, m2, ..., mr]을 모두 곱한 것.
    for j in range(0, r):
        M = M * m[j]

    for j in range(0, r):
        # MM = M / m[j]
        MM = M // m[j]

        # inv: m[j]에 대한 MM의 역원.
        inv = xgcd(MM, m[j])
        # x: 결과값
        x = x + (a[j] * MM * inv)

    # 최종 결과값
    return x % M


## CRT TEST
# a, m = [3, 10, 0], [17, 16, 15]  
# print(crt(a, m))