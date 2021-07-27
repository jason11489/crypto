import Exponentiation
import Prime_Power_Order
import CRT
import Factorization
import PHA_Parameter

q,g,x,h,n = PHA_Parameter.parameter()
npe = Factorization.fac(n)
xk = []
print("[Problem] {}^x = {} over GF({}) : {}^{} = 1".format(g,h,q,g,n))

for j in range(0,len(npe)):
    pnej = n//Exponentiation.mns1(npe[j][0],npe[j][1])
    gj = Exponentiation.mns(g,pnej,q)
    hj = Exponentiation.mns(h,pnej,q)
    xj = ((Prime_Power_Order.ppo(q,npe[j][0],npe[j][1],gj,hj)),Exponentiation.mns1(npe[j][0],npe[j][1]))
    xk.append(xj)

root = CRT.crt(xk)

print("x =", root, "(", Exponentiation.mns(g,root,q) == h, ")")






