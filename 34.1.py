# 读取输入的第一行：n, m, p, q
n, m, p, q = map(int, input().split())

# 读取原矩阵并线性化为一维数组
flat = []
for _ in range(n):
    row = list(map(int, input().split()))
    flat.extend(row)

# 重塑为 p 行 q 列的矩阵
reshaped = []
for i in range(p):
    # 取一维数组中从 i*q 到 (i+1)*q 的元素作为新矩阵的一行
    reshaped_row = flat[i * q : (i + 1) * q]
    reshaped.append(reshaped_row)

# 输出结果
for row in reshaped:
    print(' '.join(map(str, row)))