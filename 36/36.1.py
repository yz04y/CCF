n,k=map(int,input().split())


for _ in range(k):
    x,y,s=list(input().split())
    x=int(x)
    y=int(y)
    for i in range(len(s)):
        if s[i]=='f' and n>=y+1>=1:
            y=y+1
        if s[i]=='b' and n>=y-1>=1:
            y=y-1
        if s[i]=='l' and n>=x-1>=1:
            x=x-1
        if s[i]=='r' and n>=x+1>=1:
            x=x+1

    print(x,y)




