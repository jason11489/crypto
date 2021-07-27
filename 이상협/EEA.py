def inverse(a,p):
    t0, t1 = a,p
    u0,u1 = 1,0
    while t1 != 0:
        t2,t0 = t0,t1
        q,t1 = t2//t1,t2%t1
        u2,u0 = u0,u1
        u1 = u2-q*u1
    if u0 < 0:
        u0 = u0 + p
    return u0
