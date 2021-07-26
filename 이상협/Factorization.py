import math
import prime

def fac(n):
    if n == 1:
        return [(1,1)]
    i = 0
    x = []
    pm = 2   
    while(1):
        if prime.prime(pm) == True:
            if n % pm == 0:        
                cnt = 0   
                while(1):
                    n = n//pm
                    cnt += 1
                    if n % pm != 0:
                        break
                x.append((pm,cnt))
        pm += 1
        if n == 1:
            break

    return x