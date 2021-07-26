import prime
import random
import Exponentiation

def choose_p(x):
    prime_list = prime.primesInRange(x//2,x)
    p = random.choice(prime_list)
    return p

def choose_q(p):
    q_list = []
    for i in range(2,p):
        if (p-1) % i == 0:
            q_list.append(i)

    random_q = random.choice(q_list)
    while (1):
        if prime.prime(random_q) == True:
            break
        else:
            random_q = random.choice(q_list)
        
    return random_q

def choose_g(p, q):
    while(1):
        h = random.randrange(2,p-1)
        t = (p-1)//q
        g = Exponentiation.mns(h,t,p)
        if g == 1:
            continue
        else:
            return g
