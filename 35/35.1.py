n=int(input())

for _ in range(n):

    s=list(input())

    count=0

    if len(s)>=6:
        count=0

    if count==0:
        a=b=c=0
        for i in range(len(s)):

            if s[i].isalpha()==1:
                a=1
            if s[i].isnumeric()==1:
                b=1
            if s[i]=='*' or s[i]=='#':
                c=1

            if a and b and c:
                count=1

    if count==1:
        dic = {}

        for j in range(len(s)):
           if s[j] in dic:
               dic[s[j]]+=1
               if dic[s[j]]>2:
                   count=count-1
                   break
           else:
               dic[s[j]]=1
        count=count+1

    print(count)





