import EEA


def show_max(A):
    for i in range(0,len(A)):
        print(A[i])


def pivoting1(mat):
    pivot_mat = []
    col_idx = len(mat[0])
    for j in range(0, col_idx):
        row_idx = len(mat)
        i = 0
        cnt = 0
        while(cnt < row_idx):
            if mat[i][j] != 0:
                pivot_mat.append(mat[i])
                mat.remove(mat[i])
            else:
                i += 1
            cnt += 1
    

    if len(mat) != 0:
        pivot_mat = pivot_mat + mat
    return pivot_mat

def mat_add(A, B, m):
    x = []
    for i in range(0, len(A)):
        x.append((A[i] + B[i]) % m)
    return x    

def mat_reduce(A, B, m):
    x = []
    for i in range(0, len(A)):
        x.append((A[i] - B[i]) % m)
    return x    

def mat_mult(A, n, m):
    x = []
    for i in range(0, len(A)):
        x.append((n * A[i]) % m)
    return x

def mat_div(A, i, m):
    x = []
    if A[i] == 0:
        return A
    t = EEA.inverse(A[i], m)
    for j in range(0, len(A)):
        x.append((A[j]*t) % m)
    return x    

def gauss_jordan(A, m):
    X = []
    for j in range(0, len(A[0])-1):
        A = pivoting1(A)
        A[j] = mat_div(A[j], j, m)
        for i in range(j + 1, len(A)):
            B = mat_mult(A[j], A[i][j], m)
            A[i] = mat_reduce(A[i], B, m)

    for j in range(1, len(A[0]) - 1):
        for i in range(0, j):
            B = mat_mult(A[j], A[i][j], m)
            A[i] = mat_reduce(A[i], B, m)

    for j in range(0, len(A[0])-1):
        X.append(A[j][len(A[0])-1])

    return X
