import Gauss_prime
import DSA_Parameter
import random
import Exponentiation
import Factorization

#q가 prime일때만 가능

p, q, g = DSA_Parameter.parameter(2**10, 2**4)
x = random.randrange(1, p) % q
h = Exponentiation.mns(g, x, p)
S = [2, 3, 5, 7, 11]

print("G = <{}> over GF({})({}^{} = {}), {}^x = {}". format(g, p, g, q, Exponentiation.mns(g,q,p), g, h))
E = []
for i in range (0, 6):
    while(1):
        k = random.randrange(0, q)
        gk = Exponentiation.mns(g, k, p)
        gpe = Factorization.fac_IC(gk, S)
        if gpe == "False":
            continue
        gpe.append(k)
        break
    E.append(gpe)


Xj = Gauss_prime.gauss_jordan(E, q)

print("Xj =", Xj)

while(1):
    k = random.randrange(0,q)
    gk = Exponentiation.mns(g, k, p)
    ghk = (h * gk) % p
    hpe = Factorization.fac_IC(ghk, S)
    if hpe == "False":
            continue
    break
print("k =", k)
print("hg^k = hpe =",ghk, hpe)
Xe = 0
for i in range(0, len(hpe)):
    Xe = Xe + (Xj[i] * hpe[i])

root = (Xe - k) % q
print("x = {}".format(x))
print("root = {}".format(root))