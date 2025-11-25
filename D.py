t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    num=[x for x in a if x%2==1]
    if len(num)==0:
        print(0)
    else:
        num.sort()
        mid=(len(num))//2
        he=sum(a)-sum(num[:mid]) 
        print(he)  