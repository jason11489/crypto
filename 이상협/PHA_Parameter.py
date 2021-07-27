import random
import prime
import Exponentiation

def parameter():
    p = prime.random_choice(2**10)
    g = random.randrange(2,p-1)
    x = random.randrange(2,p//2)
    h = Exponentiation.mns(g,x,p)
    n = 1
    gn = g
    while(1):
        if Exponentiation.mns(gn, n, p) == 1:
            break
        n += 1
    return p,g,x,h,n
