t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    maxpoint=0
    arr=[[0,0]]
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    for i in range(1,n+1):
        if ((arr[i][0]-arr[i-1][0])%2==1 and abs(arr[i][0]-arr[i-1][0])==1) or ((arr[i][0]-arr[i-1][0])%2==0 and abs(arr[i][0]-arr[i-1][0])==0):
            maxpoint+=(arr[i][0]-arr[i-1][0])
        else:
            maxpoint=maxpoint+(arr[i][0]-arr[i-1][0])-1
    maxpoint=maxpoint+m-arr[-1][0]
    print(maxpoint)    


