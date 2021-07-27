import random
import EEA
import DSA_Parameter
import prime
import Exponentiation


# parameter

n = DSA_Parameter.choose_q(2**4)
p = DSA_Parameter.choose_p(n,2**7)
g = DSA_Parameter.choose_g(p,n)

'''
p = 383
g = 227
n = 191
'''
x = random.randrange(2, p)

# problem : g^x = h  =>  find x
h = Exponentiation.mns(g,x,p)
print("[Problem] {}^x = {} over GF({}) : {}^{} = 1".format(g,h,p,g,n))

def pollard(p,g,n,h):
    #print("[Problem] {}^x = {} over GF({}) : {}^{} = 1".format(g,h,p,g,n))

    if g == h:
        root = 1
        print("x =", root, "(", Exponentiation.mns(g,root,p) == h, ")")
        return root

    def f(x):
        if x[0] % 3 == 1:
            return ((x[0]*h) % p,x[1],(x[2]+1) % n)
        if x[0] % 3 == 0:
            return (Exponentiation.mns(x[0],2 ,p),(2*x[1]) % n,(2*x[2]) % n)
        if x[0] % 3 == 2:
            return ((x[0]*g) % p,(x[1]+1) % n, x[2])


    cnt = 0
    while (1):
        #x1 = x2 = (1,0,0)
        a = random.randrange(0, n)
        b = random.randrange(0, n)
        x1 = x2 = (((Exponentiation.mns(g,a,p)*Exponentiation.mns(h,b,p))) % p, a, b)
        j = 0
        while(1):
            print (j, x1, x2)
            j = j + 1
            x1, x2 = f(x1), f(f(x2))
            if x1[0] == x2[0]:
                break
        print (j, x1, x2)
    
    
    
        T1, T2 = (x1[1] - x2[1]) % n, (x2[2] - x1[2]) % n
        if T2 == 0:
            print("Failure.")
            continue
        else:
            T2_inv = EEA.inverse(T2,n)
            root = (T1*T2_inv) % n
            print("x =", root, "(", Exponentiation.mns(g,root,p) == h, ")")
            return root