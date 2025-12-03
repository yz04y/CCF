k=int(input())

for _ in range(k):
    x,y,z=map(int,input().split())
    m=(z-x)/y
    q=int(m*10)
    p=int((m*10-q)*10+1)
    print(q+1,p)
