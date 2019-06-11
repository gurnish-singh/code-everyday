'''
You are given an integer n and an integer k.

In one step you can do one of the following moves:

decrease n by 1;
divide n by k if n is divisible by k.
For example, if n=27 and k=3 you can do the following steps: 27→26→25→24→8→7→6→2→1→0.

You are asked to calculate the minimum number of steps to reach 0 from n.

Input
The first line contains one integer t (1≤t≤100) — the number of queries.

The only line of each query contains two integers n and k (1≤n≤1018, 2≤k≤1018).

Output
For each query print the minimum number of steps to reach 0 from n in single line.

Example
inputCopy
2
59 3
1000000000000000000 10
outputCopy
8
19
'''
for i in range (int(input())):
    a=[int(i) for i in input().split()]
    count=0
    while(a[0]!=0):
        if (a[0]%a[1]==0):
            a[0]=a[0]//a[1]
            count+=1
        else:
            rem=a[0]%a[1]
            a[0]-=rem
            count+=rem
    print(count)
