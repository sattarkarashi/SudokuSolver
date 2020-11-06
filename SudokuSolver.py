import numpy as np


def SuDoSolver(sudo):
    def var(i):
        k=[]
        if i<3:
            k=[0,3]
        if i>2 and i<6:
            k=[3,6]
        if i>5:
            k=[6,9]
        return k

    def data(t):
        dat=[]
        for i in range(9):
            for j in range(9):
                if t[i,j]==0:
                    dat.append((i,j))
        return dat

    def emp(t,p,ph):
        k=[]
        d=data(t)


        for i in range(10):
            if not np.count_nonzero(t[p]==i) and not np.count_nonzero(t[:,ph]==i):
                if not np.count_nonzero(t[var(p)[0]:var(p)[1],var(ph)[0]:var(ph)[1]]==i):
                    k.append(i)

        return k


    d=data(sudo)
    s={}
    for k in d:
        s[k]=[]

    i=0
    while True:

        p=d[i][0]
        ph=d[i][1]
        lispos=emp(sudo,p,ph)

        for l in lispos:
            if l not in s[(p,ph)]:
                sudo[p,ph]=l
                s[(p,ph)].append(l)

                i+=1
                break
        else:
            s[(p,ph)]=[]
            sudo[p,ph]=0
            i-=1
        if i==-1:
            break

        if i>len(d)-1:
            print(sudo)
            break
