import Quick_sort

def show_max(A):
    for i in range(0,len(A)):
        print(A[i])

def pivoting(mat):
      row_idx = list(range(len(mat)))
      col_idx = len(mat[0])
      pivot_mat = []
      for c in range(col_idx):
          rows_with_nonzero = [r for r in row_idx if mat[r][c] != 0]
          if rows_with_nonzero:
              pivot = rows_with_nonzero[0]
              for idx in rows_with_nonzero:
                  pivot_mat.append(mat[idx])
                  row_idx.remove(idx)
      return pivot_mat

def zero_list(col):
    x = []
    for i in range(0, col):
        x.append(0)
    return x


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

    

def mat_add(A, B):
    x = []
    for i in range(0, len(A)):
        x.append((A[i] + B[i]))
    return x    

def mat_reduce(A, B):
    x = []
    for i in range(0, len(A)):
        x.append((A[i] - B[i]))
    return x    

def mat_mult(A, n):
    x = []
    for i in range(0, len(A)):
        x.append((n * A[i]))
    return x    

def mat_div(A, n):
    x = []
    if n == 0:
        return A
    for i in range(0, len(A)):
        x.append((A[i] / n))
    return x    

def gauss_jordan(A, m):
    for j in range(0,len(A[0])-1):
        A = pivoting1(A)
        print("j =", j)
        show_max(A)
        t = j
        while(1):
            if A[j][t] == 0:
                t += 1
            else:
                break
        A[j] = mat_div(A[j], A[j][t])
        for i in range(j + 1, len(A)):
            matA = mat_mult(A[j],A[i][j])
            A[i] = mat_reduce(A[i], matA)
    
    for j in range(1, len(A[0])):
        for i in range(0, j):
            matA = mat_mult(A[j],A[i][j])
            A[i] = mat_reduce(A[i],matA)

    for j in range(0, len(A)):
        A[j][len(A[0])-1] = A[j][len(A[0])-1]
    show_max(A)

    X = []
    for j in range(0, len(A)):
        for i in range(0, len(A[0])-1):
            if A[j][i] != 0:
                t = A[j][len(A[0])-1] % m
                X.append(t)
    
    return X


#E = [[2,2,1,0,0,100], [4,0,0,0,1,18], [0,1,1,0,1,12], [1,0,0,1,1,62], [1,2,0,0,1,143], [1,1,1,1,0,206]]
#E = [[1, 1, 0, 1, 0, 42], [1, 0, 2, 0, 0, 50], [0, 3, 1, 1, 0, 945], [1, 1, 0, 1, 0, 42], [1, 0, 2, 0, 0, 50], [1, 0, 2, 0, 0, 50]]
#E = [[0, 1, 0, 1, 0, 6], [1, 0, 1, 0, 0, 3], [1, 0, 0, 0, 1, 8], [3, 0, 0, 0, 0, 10], [1, 0, 0, 0, 1, 8], [1, 0, 0, 0, 1, 8]]
#E = [[0, 3, 1, 0, 0, 38], [3, 1, 0, 0, 0, 43], [0, 3, 0, 0, 0, 168], [4, 1, 0, 0, 0, 64], [2, 0, 0, 0, 0, 42], [6, 0, 0, 0, 0, 126]]
#E = [[5, 0, 1, 0, 0, 203], [2, 1, 0, 1, 0, 129], [1, 2, 1, 0, 0, 79], [0, 1, 2, 0, 0, 176], [0, 2, 2, 0, 0, 156], [4, 0, 1, 0, 0, 182]]
#print(gauss_jordan(E, 228))

#E = [[1,0,0],[0,0,0],[0,1,0],[0,0,0]]
#print(pivoting1(E))