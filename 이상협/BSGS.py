import math
import Quick_sort
import EEA
import Exponentiation
import show_list
import Binary_search
import DSA_Parameter
import random
NO_ELEMENT = 'NO_ELEMENT'


#GF(p), g^n = 1, g^x = h => find x
def dlp_bsgs(p,g,h):
    m = 1 + math.floor(math.sqrt(p-1))
    #print("m = {} = 0x{:x}".format(m, m))
    L, t = [], 1
    for j in range (0,m-1):
        L = L + [[j,t]]
        t = (t * g) % p
    print("L1 ="); show_list.show_list(L)
    L = Quick_sort.quick_sort1(L,0,len(L)-1,1)
    print("Sorted L1 = "); show_list.show_list(L)

    inv_g = EEA.inverse(g,p)
    w, t = Exponentiation.mns(inv_g,m,p), h
    root = "UNKNOWN"
    L2 = []

    for j in range(0,m-1):
        L2 = L2 + [[j,t]]
        i = Binary_search.b_search(L,t)
        if i != NO_ELEMENT:
            print("L2 ="); show_list.show_list(L2)
            print("(i,g^i) = ({},{})".format(i,Exponentiation.mns(g,i,p)))
            print("(j,hg^(-jm)) = ({},{})".format(j,t))
            root = (i + m*j)%(p-1) # p-1: group order
            break
        t = (t * w)%p

    print("x =", root, "(", Exponentiation.mns(g,root,p) == h, ")")
    return root


q = DSA_Parameter.choose_q(2**7)
p = DSA_Parameter.choose_p(q,2**8)
g = DSA_Parameter.choose_g(p,q) % q
'''
p = 223
g = 3
'''
x = random.randrange(2, q)
h = Exponentiation.mns(g,x,q)

print("[Problem] {}^x = {} over GF({})".format(g,h,q))
dlp_bsgs(q,g,h)