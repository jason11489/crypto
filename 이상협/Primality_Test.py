import Exponentiation
import random
import prime
import EEA

def get_l(a):
    cnt = 0
    while(1):
        if (a&1 == 0):
            a, cnt = a>>1, cnt + 1
        else:
            return cnt

def is_composite(n, q, l, a):
    a = Exponentiation.mns(a,q,n)
    #print("a^(q) = {}".format(a))
    if(a%n == 1):
        return "NOT composite"
    for j in range(0,l):
        #print("a^(2^{}*q) = {}".format(j,a))
        if(a%n) == (n-1):
            return "NOT Composite"
        a = Exponentiation.mns(a,2,n)
    return "Composite"

def miller_rabin(n, k):
    l = get_l(n-1)
    q = (n-1) >> l
    #print("l = {}, q = {}".format(l,q))
    while(k > 0):
        a = random.randrange(2,n-1)
        #print("a = {}".format(a))
        ret = is_composite(n, q, l, a)
        if ret == "Composite":
            return "Composite"
        k = k - 1
    return "Probably Prime"
'''
n = random.randrange(1,10000)
#n = prime.random_choice(10000)

print("n = {}".format(n))
print(miller_rabin(n, 1))
print(prime.prime(n))
'''