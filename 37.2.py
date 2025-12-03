n, m = map(int, input().split())
A = list(map(int, input().split()))
# 调整A的索引，使A[1]对应投喂1个苹果的快乐值
A = [0] + A  # 此时A[0]=0, A[1]到A[m]是输入的快乐值

dp = [0] * (n + 1)
for j in range(1, n + 1):
    max_val = 0
    # 尝试投喂i个苹果（i不超过m，且不超过当前苹果数j）
    for i in range(1, min(m, j) + 1):
        if dp[j - i] + A[i] > max_val:
            max_val = dp[j - i] + A[i]
    dp[j] = max_val

print(dp[n])