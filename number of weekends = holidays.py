a=[31,28,31,30,31,30,31,31,30,31,30,31]
b=5
n=len(a)
for i in range (n):
    while(b<=a[i]):
        if b==a[i]:
            print(repr(b)+'.'+repr(i+1)+'.'+'2019')
            break
        elif b<a[i]and b!=0:
            print(repr(b)+'.'+repr(i+1)+'.'+'2019')
        if b<a[i]:
            b+=1
            print(repr(b)+'.'+repr(i+1)+'.'+'2019')
            b+=6
    b=b-a[i]
        
