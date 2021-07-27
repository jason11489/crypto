import prime
import random
import Exponentiation

def choose_q(x):
    prime_list = prime.primesInRange(x//2,x)
    q = random.choice(prime_list)
    return q

def choose_p(q, x):
    p_list = []
    i = 1
    while(i < x):
        t = (q * i) + 1
        if prime.prime(t):
            p_list.append(t)
        i += 1

    random_p = random.choice(p_list)
    return random_p

def choose_g(p, q):
    while(1):
        h = random.randrange(2,p-1)
        t = (p-1)//q
        g = Exponentiation.mns(h,t,p)
        if g == 1:
            continue
        else:
            return g
