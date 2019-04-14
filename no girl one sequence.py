'''The  of a sequence that contains positive integers  is given as .

You are provided a sequence of positive integers  and two integers  and  . You are required to select an integer  and add  to all elements of the . This provides you a new sequence of positive integers.

If you have selected the  through an optimal way, then determine the maximum score of ?

Input format

First line: Three integers  representing the number of elements available in the  sequence and the allowed range of  
Second line: 
Output format

Print an integer that represents the maximum score of .

SAMPLE INPUT 
2 1 2
1 3
SAMPLE OUTPUT 
2'''
def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
    return x 

t=[int(i) for i in input().split()]
n=t[0]

l=t[1]
r=t[2]
p=[int(i) for i in input().split()]
score=0
for x in range (l,r+1):
    arr=[]
    for j in range(n):
        arr.append(p[j]+ x)
    print(arr)
    num1 = arr[0] 
    num2 = arr[1] 
    gcd = find_gcd(num1, num2) 
    for k in range(2, len(arr)): 
        gcd = find_gcd(gcd, arr[k]) 
    if gcd>score:
        score=gcd
print(score)
    
