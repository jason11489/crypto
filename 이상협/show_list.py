def show_list(L):
    cnt = 0
    while cnt < len(L):
        print("{}, ".format(L[cnt]), end = '')
        cnt = cnt + 1
        if(cnt%5 == 0):
            print("\n", end = '')
    print("\n")