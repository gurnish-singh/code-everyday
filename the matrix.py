'''Pratik is a huge fan of The Matrix. He says he can perform matrix operations in his mind.
So to test this his friend rohit gave him two matrices A(pxq) and B(qxr),
he asked pratik to multiply these matrices and
calculate sum of each row and each column and give the highest of these numbers as answer.
Score = max(0, x), where 
INPUT:
first line of input contains two space separated integers denoting p and q.
each of the next p lines contains q space separated integers
next line of input contains two space separated integers denoting q and r.
each of the next q lines contains r space separated integers
OUTPUT:
print the maximum of sum of each row and each column.
CONSTRAINTS:
0<=Aij,Bij<=99
3<=p,q,r<=100

SAMPLE INPUT 
3 3
8 9 1
5 2 3
4 6 5
3 3
1 2 3
4 5 6
7 8 9
SAMPLE OUTPUT 
234'''

import numpy as np
a=[int(i) for i in input().split()]
p=a[0]
q=a[1]
g=[]
g=np.zeros((p,q))
t=[]
t=np.zeros((p,q))
for i in range (p):
        t=[int(k) for k in input().split()]
        for j in range (q):
            g[i,j]=t[j]
print(g)
b=[int(i) for i in input().split()]
q=b[0]
r=b[1]
h=[]
h=np.zeros((q,r))
f=[]
f=np.zeros((q,r))
for i in range (q):
        f=[int(k) for k in input().split()]
        for j in range (r):
            h[i,j]=f[j]
print(h)
#----------------to calculte product of matrix--------------------
gh=np.dot(g,h)
print(gh)
#----------------to calculate sums--------------------------
summ=0
test=0
for i in range (p):
    test=0
    for j in range(r):
        test+=gh[i,j]
    if test>summ:
        summ=test
for i in range (r):
    test=0
    for j in range(p):
        test+=gh[j,i]
    if test>summ:
        summ=test
print (summ)
