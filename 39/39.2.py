n, L = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

# 定义5x9模板（0=黑色区域，1=白色区域）
template = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0],
]

valid_ks = set()

# 遍历所有可能的5x9子矩阵的左上角位置（0-based）
for i in range(n - 4):  # 子矩阵起始行，确保结束行i+4 < n
    for j in range(n - 8):  # 子矩阵起始列，确保结束列j+8 < n
        # 提取当前5x9子矩阵的灰度值
        submatrix = []
        for x in range(5):
            # 从原矩阵中截取j到j+9列（共9列）
            row = A[i + x][j: j + 9]
            submatrix.append(row)

        # 分离黑色区域（模板0的位置）和白色区域（模板1的位置）的灰度值
        blacks = []  # 黑色区域的灰度值（需要 < k）
        whites = []  # 白色区域的灰度值（需要 ≥ k）
        for x in range(5):
            for y in range(9):
                val = submatrix[x][y]
                if template[x][y] == 0:
                    blacks.append(val)
                else:
                    whites.append(val)

        # 计算当前子矩阵的有效k范围：max(blacks) < k ≤ min(whites)
        max_black = max(blacks)
        min_white = min(whites)
        if max_black < min_white:
            # k的有效范围需同时满足：max_black < k ≤ min_white 且 0 ≤ k ≤ L-1
            start_k = max_black + 1
            end_k = min(min_white, L - 1)
            if start_k <= end_k:
                # 将范围内的所有k加入集合（自动去重）
                for k in range(start_k, end_k + 1):
                    valid_ks.add(k)

# 按升序输出所有有效阈值k
for k in sorted(valid_ks):
    print(k)