import math
import DLP_pollard_rho

def show_list (L):
    cnt = 0
    while (cnt < len(L)):
        print ("{}, ".format(L[cnt]), end = " ")
        cnt =cnt+1
    print("\n")


def dlp_power_ord(gen,target,P,mod):#P = [p,n]
    h = target
    g = DLP_pollard_rho.power_mod_naive(gen,P[0]**(P[1]-1),mod)
    g_inv = DLP_pollard_rho.inverse(g,mod)
    #print("g*g_inv = {}".format((g*g_inv)%mod))
    x = 0
    for i in range (0,P[1]):
        h = (target*DLP_pollard_rho.power_mod_naive(g_inv,x,mod))%mod
        h = DLP_pollard_rho.power_mod_naive(h,P[0]**(P[1]-i-1) ,mod )
        temp = DLP_pollard_rho.pollard(g,P[0],mod,h)
        x = x*P[0] + temp
        print('\t temp = {}'.format(temp))
        #show_list(X)

    return x

print (dlp_power_ord(5448,6909,[5,4],11251) )