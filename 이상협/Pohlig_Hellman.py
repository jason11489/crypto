import Exponentiation
import Prime_Power_Order
import CRT
import Factorization
import PHA_Parameter

#<7> ord = 40 , GF(41)  7^x = 12 => x = 13
'''
q = 173
n = 172
g = 153
h = 93
'''
q,g,x,h,n = PHA_Parameter.parameter()
npe = Factorization.fac(n)
xk = []
for j in range(0,len(npe)):
    pnej = n//Exponentiation.mns1(npe[j][0],npe[j][1])
    gj = Exponentiation.mns(g,pnej,q)
    hj = Exponentiation.mns(h,pnej,q)
    xj = ((Prime_Power_Order.ppo(q,npe[j][0],npe[j][1],gj,hj)),Exponentiation.mns1(npe[j][0],npe[j][1]))
    xk.append(xj)

root = CRT.crt(xk)

print("x =", root, "(", Exponentiation.mns(g,root,q) == h, ")")