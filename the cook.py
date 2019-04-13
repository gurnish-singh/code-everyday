'''Walter is a very famous cook living in a small town.
Pizzas made by him are always in high demand. 

When the head of the town came to know about Walter's cooking skills,
he planned to give him a big order.

Now, Walter is very busy preparing pizzas. A lot of this job has to be done and
time is very less since he is busy preparing pizzas and
no one is there to pack them in boxes. So, Walter wants you to help him to work efficiently.

There are  N distinct types of pizzas from 1 to N. You will be given M pizzas of N types randomly by Walter.

Your job is to pack these pizzas in boxes such that a box must only contain N distinct pizzas.

After every pizza that you receive you have to output " 1 "
if you were able to fill a box with N distinct pizzas else output " 0 " without quotes.

 

Input

The first line contains two integers N and M (  ) — the number of distinct pizzas and the number of total pizzas.

The second line contains M integers  () — the pizza number which is the sign of distinction.

Output

Print a line containing M digits. The i-th digit should be 1 if you were able to pack a box with N distinct pizzas else 0.

 

SAMPLE INPUT 
3 11
2 3 1 2 2 2 3 2 2 3 1
SAMPLE OUTPUT '''
00100000001from collections import Counter
p=[int(x) for x in input().split()]
nums=[int(x) for x in input().split()]
d={}
ans=''
num=1
for i in range(1,p[0]+1):
    d[i]=0 #occurance of every digit is zero
for i in nums:
    f=0
    d[i]+=1#and here it inc. accordingly
    for j in d.values():
       if j<num:
            f=1''' that is if the count of every number is greater than or
equal to 1 in initial case it will print 1 other wise zero'''
            break
    if f==1:
        ans+='0'
    else:
        ans+='1'
        num+=1
print (ans)

