b,c,l,r = map(int,input().split())

if l%2==0:
    x=l
else:
    x=l+1
s=0

while x<=r:
    f = x ** 2 + b * x + c
    s+=f
    x+=2

s=2*s
print(s)