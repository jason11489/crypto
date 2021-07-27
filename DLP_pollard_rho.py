import math
import random
def inverse(a,p):
    t0, t1 = a,p
    u0,u1 = 1,0
    while t1 != 0:
        t2,t0 = t0,t1
        q,t1 = t2//t1,t2%t1
        u2,u0 = u0,u1
        u1 = u2-q*u1
    if u0 < 0:
        u0 = u0 + p
    return u0

def f(x,gen,ord,mod,target):
    if (x[0]%3 == 0):
        x = [(x[0]*gen)%mod,(x[1]+1)%ord,x[2]]
    elif (x[0]%3 == 1):
        x = [(x[0]*target)%mod,x[1],(x[2]+1)%ord]
    elif (x[0]%3 == 2):
        x = [(x[0]*x[0])%mod,(2*x[1])%ord,(2*x[2])%ord]
    return x
    
def pollard(gen,ord,mod,target):
    x0,x1 = [1,0,0],[1,0,0]
    
    while (x0[0]!=x1[0] or x0[2] == x1[2]):
        x0,x1 = f(x0,gen,ord,mod,target),f(f(x1,gen,ord,mod,target),gen,ord,mod,target)
        print(x0,x1)
        print((power_mod_naive(gen,x0[1],mod)*power_mod_naive(target,x0[2],mod))%mod , end=" ")
        print((power_mod_naive(gen,x1[1],mod)*power_mod_naive(target,x1[2],mod))%mod)
        if (x0[0]==x1[0] and x0[2] == x1[2]):
            print('\n')
            a,b = random.randrange(0,ord),random.randrange(0,ord)
            x0 = x1 = [(power_mod_naive(gen,a,mod)*power_mod_naive(target,b,mod))%mod,a,b]

    A = (x1[1]-x0[1])%ord
    B = (x0[2]-x1[2])%ord
    B_inv = inverse(B,ord)
    x = (A*B_inv)%ord
    print ("the sol = {}".format(x))
    return x

def powmod_l2r(g,n,M):
    t = 1
    l = len(bin(n))-2
    print(len(bin(n)))
    n = list(map(int,str(bin(n)[2:])))
    print(n,l)
    for i in range(0,l):
        t = (t**2)%M
        t = t*(g^n[i])%M
    return M

def power_mod_naive(g,n,M):
    ret = 1
    i=0
    for i in range (0,n):
        ret = (ret*g)%M
    return ret

p = 383
q = 191
g = 227
x = 2
a = pollard(g,q,p,x)
print(a)
sol = power_mod_naive(g,a,p)
print(sol)
