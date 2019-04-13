'''Annie is the talk of the town, who recently won the prize for being the most beautiful woman of her town.
Due to her achievement, she has become Dream girl of the youth.

So, many people in the town are trying to propose her, but She has her own demands and only if the demands are satisfied, she will accept the proposal.

She loves two types of chocolates A and B, and she wants someone to gift her D chocolates during the act of proposing.

You have an infinite supply of boxes of chocolates of type A and B, box of type A contains N chocolates whereas box of type B contains M chocolates.

You can gift her D chocolates by using boxes of both the types.(You cannot use any box partially).

Now, You have to find the number of ways in which you can impress her.

 

Input Format:

The first line of input consists of an integer T denoting the number of test cases.
Each test case consists of only one line containing three space separated integers
N(Number of chocolates in box of type A), M(Number of chocolates in box of type B) and D.

Output Format:
For each test case, print the answer in a separate line.
SAMPLE INPUT 
3
2 3 7
4 10 6
5 1 5
SAMPLE OUTPUT 
1
0
2'''
for i in range (int(input())):
    x=[int(j) for j in input().split()]
    a=x[0]
    b=x[1]
    d=x[-1]
    count =0
    for i in range (d+1):
        if a*i>d:
            break
        for j in range (d+1):
                    if b*j>d:
                        break
                    elif a*i+b*j>d:
                        break
                    elif a*i+b*j==d:
                        count+=1
                    
    print(count)
