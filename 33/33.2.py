n,m=map(int,input().split())

p=list(input().split())
q=list(input().split())

p = [s.lower() for s in p ]
q = [x.lower() for x in q ]

p = set(p)
q = set(q)

p= list(p)
q =list(q)

num = len(p)+len(q)

count=0

dic = {}

for i in range (len(p)):
    if p[i] not in dic:
        dic[p[i]]=1
    else:
        dic[p[i]]+=1
for j in range (len(q)):
    if q[j] not in dic:
        dic[q[j]]=1
    else:
        dic[q[j]]+=1

for l in dic:
    if dic[l] == 2:
        count=count+1

print (count)
print (num-count)