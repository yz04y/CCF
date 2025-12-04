S=list(input())

n=int(input())

dic = {}

for _ in range(n):
    s=list(input())
    dic[s[1]]=s[2]

m=int(input())
k=list(map(int,input().split()))

for j in range(m):
    A = []
    A = S.copy()
    for _ in range(k[j]):
        for i in range(len(A)):
            if A[i] in dic.keys():
                A[i] = dic[A[i]]

    print(''.join(A))





