n,m=map(int,input().split())

b = []
dic = {}

page = {}

for j in range(n):
   a=list(map(int,input().split()))
   visited = {0:0}
   for i in range(len(a)-1):
        if a[i+1] not in visited:
            visited[a[i+1]] = 0
        if  visited[a[i+1]]==0:
            if a[i+1] not in page:
                page[a[i+1]] = 1
            else:
                page[a[i+1]] += 1
            visited[a[i+1]]=1
        if a[i+1] not in dic:
            dic[a[i+1]]=1
        else:
            dic[a[i+1]]+=1

for l in range(1,m+1):
    print(f"{page[l]} {dic[l]}")
