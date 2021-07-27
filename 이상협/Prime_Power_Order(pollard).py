import Exponentiation
import Pollard_rho
import EEA

q = 11251
p = 5
n = 4
g = 5448
#g^511 = 6909 (mod 11251)
#g^15 = 5910 (mod 11251)
#g^100 = 1570 (mod 11251)
h = 5910

#q : GF(q), p^n : order, g : generator, g^x = h
def ppo(q,p,n,g,h):
    pn1 = Exponentiation.mns1(p,n-1)
    w = Exponentiation.mns(g,pn1,q)
    g_inv = EEA.inverse(g,q)

    x = []
    hp0 = Exponentiation.mns(h,pn1,q)
    x.append(Pollard_rho.pollard(q,w,p,hp0))

    for i in range(1, n):
        xk = 0
        pni = Exponentiation.mns1(p,n-1-i)
        for j in range(0, i):
            xk = xk + (x[j] * Exponentiation.mns1(p,j))
            #print("x{} = {}".format(i+j,xk))
        gni_inv = Exponentiation.mns(g_inv,xk,q)
        k = (h * gni_inv) % q
        hpi = Exponentiation.mns(k,pni,q)
        x.append(Pollard_rho.pollard(q,w,p,hpi))

    print("x = ",x)

    root = 0
    for j in range(0, n):
        root = root + (x[j] * Exponentiation.mns1(p,j))


    print("x =", root, "(", Exponentiation.mns(g,root,q) == h, ")")

    return root

ppo(q,p,n,g,h)