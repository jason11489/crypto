import matplotlib.pyplot as plt

n,k,L,p=365,50,[],1

for i in range(1, k+1):
    p = p*(n-(i-1))/n
    L += [[i,1-p]]


x,y=[],[]

for i in L:
    x+=[i[0]]
    y+=[i[1]]

plt.plot(x,y, 'b.')
plt.title("(k,Pk)")
plt.show()


for i in L:
    print([i[0],i[1]])