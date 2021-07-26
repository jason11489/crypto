import EEA

#x : x = a1 (mod n1), x = a2(mod n2)...
#x : list [(a1, n1),(a2, n2), ... ]

def crt(x):
    Nj = []
    n = 1
    for i in range(0, len(x)):
        n = n*(x[i][1])
    
    for i in range(0, len(x)):
        Nj.append(n//x[i][1])
    
    xj = []
    for i in range(0,len(Nj)):
        xj.append(EEA.inverse(Nj[i],x[i][1]))
    
    root = 0
    for i in range(0,len(x)):
        t = (x[i][0] * Nj[i] * xj[i]) % n
        root = (root + t) % n
    
    return root
