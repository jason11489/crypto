import Gauss
import DSA_Parameter
import random
import Exponentiation
import Factorization

'''
p, q, g = DSA_Parameter.parameter(2**10, 2**4)
x = random.randrange(1, p)
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
'''


#슈밤 p, q, g, E가 이거일때만 가능 아직 수정중....
p, q, g = 229, 228, 6
x = random.randrange(1, p)
h = Exponentiation.mns(g,x,p)
S = [2, 3, 5, 7, 11]
print("G = <{}> over GF({})({}^{} = {}), {}^x = {}". format(g, p, g, q, Exponentiation.mns(g,q,p), g, h))
E = [[2,2,1,0,0,100], [4,0,0,0,1,18], [0,1,1,0,1,12], [1,0,0,1,1,62], [1,2,0,0,1,143], [1,1,1,1,0,206]]
Xj = Gauss.gauss_jordan(E, q)

print("Xj =", Xj)

while(1):
    k = random.randrange(0,q)
    gk = Exponentiation.mns(g, k, p)
    ghk = (h * gk) % p
    hpe = Factorization.fac_IC(ghk, S)
    if hpe == "False":
            continue
    break
print("hg^k = hpe =",ghk, hpe)
Xe = 0
for i in range(0, len(hpe)):
    Xe = Xe + (Xj[i] * hpe[i])

x = (Xe - k) % q

print(x)