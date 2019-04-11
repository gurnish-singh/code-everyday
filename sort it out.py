
'''You are given a alphanumeric string of length N, you have to sort the string
in a way that output string contains alphabets where the input string has
alphabets, and numbers where the input string has numbers.
Alphabets and numbers must be sorted independently in increasing order.
Score = max(0, x), where 
INPUT:
first line of input contains a number t denoting number of test cases.
first line of each test case contains the alphanumeric string.
OUTPUT:
print the sorted string as specified above.
CONSTRAINTS:
1<=t<=10
10<=N<=105
Input string only contains UPPERCASE English Alphabets and numbers.
SAMPLE INPUT 
2
QWERTY1234
R53A7D8F78
SAMPLE OUTPUT 
EQRTWY1234
A35D7F7R88'''
from heapq import heapify as h,heappop as hp
'''
heapq.heapify(x)
Transform list x into a heap, in-place, in linear time.
heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant.
If the heap is empty, IndexError is raised.
To access the smallest item without popping it, use heap[0].'''
n=int(input())
for i in range (n):
    x,y=[],[]
    p=input()
    for a in p:
        if a.isdigit():
            x.append(a)
        else:
            y.append(a)
    h(x)#x is sorted and stored
    h(y)
    u='' #empty string
    for i in p:
        if i.isdigit():
            u+=hp(x)
        else:
            u+=hp(y)
    print(u)
