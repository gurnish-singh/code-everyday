'''
A string  is called a good string if and only if two consecutive letters are not the same. For example,  and   are good while  and  are not.

You are given a string . Among all the good substrings of  ,print the size of the longest one.

Input format

A single line that contains a string  ().

Output format

Print an integer that denotes the size of the longest good substring of .

SAMPLE INPUT 
ab
SAMPLE OUTPUT 
2'''
s=input()
count=1
count1=1
for i in range (len(s)-1):
    if (s[i]!=s[i+1]):
        count=count+1
    else:
        count1=max(count,count1)
        count=1
print (max(count,count1))
