#right-to-left
def r2l(g, n, M):
    
    t = [1, g]

    l = len(bin(n)) - 2 # l: bit length
    n = list(map(int, str(bin(n)[2:]))) # n을 이진수로 변환 후 리스트에 저장.

    for j in range(l-1, -1, -1):
        t[0] = (t[0] * (t[1] ** n[j])) % M
        t[1] = (t[1] ** 2) % M
    return t[0]
    
#left-to-right modular exponentiation
def l2r(g, n, M):
  
    t = 1

    l = len(bin(n)) - 2 # l: bit length
    n = list(map(int, str(bin(n)[2:]))) # n을 이진수로 변환 후 리스트에 저장.

    for j in range(0, l):
        t = (t ** 2) % (M)
        t = (t * (g ** n[j])) % (M)

    return t

#montgomery ladder   
def mns(x,n,m):
    t = [1, x]
    e = format(n,'b')
    for i in range(0,len(e)):
        t[1-int(e[i])] = (t[0] * t[1]) % m
        t[int(e[i])] = (t[int(e[i])]**2) % m
    return t[0]

def mns1(x,n):
    t = [1, x]
    e = format(n,'b')
    for i in range(0,len(e)):
        t[1-int(e[i])] = t[0] * t[1]
        t[int(e[i])] = t[int(e[i])]**2
    return t[0]

'''
제원이꺼
def mns(g, n, M):
    t = [1, g]

    l = len(bin(n)) - 2 # l: bit length
    n = list(map(int, str(bin(n)[2:]))) # n을 이진수로 변환 후 리스트에 저장.

    for j in range(0, l):
        t[1-n[j]] = (t[0] * t[1]) % M
        t[n[j]] = (t[n[j]] ** 2) % M

    return t[0]
'''