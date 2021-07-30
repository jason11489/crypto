import random
import math

def PMN(g,n,M):
    ret = 1
    i=0
    for i in range (0,n):
        ret = (ret*g)%M
    return ret

def is_prime(N):
    for i in range(2,math.floor(math.sqrt(N)+1)):
        if (N%i == 0):
            #print("{} is prime?".format(N),end=" ")
            return False
    #print("{} is prime?".format(N),end=" ")            
    return True

def random_prime(low,high):
    N=4
    while(not is_prime(N)):
        N = random.randrange(low,high)
    return N

def factor(N):
    X = []
    for i in range(2,math.floor(math.sqrt(N))):
        if (N%i == 0):
            j = 0
            while(N%i == 0):
                N = math.floor(N/i)
                j = j+1
            X.append([i,j])
    if (N != 1):
        X.append([N,1])
    return X

def generator(N):
    g = random.randrange(2,N)
    return g

def order(g,N):
    i=1
    g_ = g
    while(g != 1):
        g = (g*g_)%N
        i = i+1
        #print("g^i = {}, i = {}".format(g,i))
    return i

def ppo_para(low,high):
    Q = [1,1]
    while (Q[1]<3 ):
        N = random_prime(low,high)
        g = generator(N)
        t = order(g,N)
        #print(factor(t))
        Q = factor(t)[0]
    gen = PMN(g,math.floor(t/(Q[0]**Q[1])) ,N)
    x = random.randrange(2, Q[0]**Q[1])
    target = PMN(gen,x,N)
    print("N = {}".format(N))
    print("order ={}^{}=  {}".format(Q[0],Q[1],Q[0]**Q[1]))
    print("generator = {}".format(gen))
    return gen, target, Q, N

g, h, P, N = ppo_para(1000000,2000000)
print("tne problem is finding x s.t. {}**x = {} mod {} with ord = {}^{} = {}".format(g,h,N,P[0],P[1],P[0]**P[1]))
