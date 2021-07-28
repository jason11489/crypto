import dlp 
import exp

def ppo(g, h, p, e, q):
    x, y, r= 0, [1], 1
    w =  exp.modL2r(g, exp.l2r(p, e-1), q)
    inv_g =  dlp.xgcd(g, q)
    
    print("ord(w) is ", w)
    print("g의 역원", inv_g)

    for j in range(0, e):

        r =r * exp.modL2r(inv_g, ( y[j-1] * ( (exp.l2r(p, j) + 1) // p ) ), q)
        hh = exp.modL2r(h * r, exp.l2r(p, e-1-j), q)

        y.insert(j, dlp.bsgs(w, hh, q) % p)
        print("x[{}] 해: {}".format(j, dlp.bsgs(w, hh, q) % p))
        x = x + (y[j] * exp.l2r(p, j))

    return x

print("x =", ppo(5448, 6909, 5, 4, 11251))
print(exp.modL2r(5448, 511, 11251) == 6909)