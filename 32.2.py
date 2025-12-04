import math

def simplify(n, k):
    result = 1
    # 分解质因数
    i = 2
    while i * i <= n:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n = n // i
            # 判断指数是否≥k，是则乘入结果
            if cnt >= k:
                result *= (i ** cnt)
        i += 1
    # 处理剩余的质因数（n>1时）
    if n > 1:
        if 1 >= k:
            result *= n
    return result

# 读取输入
q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    print(simplify(n, k))
