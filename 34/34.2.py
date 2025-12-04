# 读取初始参数
n, m, t = map(int, input().split())
# 读取初始矩阵，转为一维列表
data = []
for _ in range(n):
    row = list(map(int, input().split()))
    data.extend(row)
curr_row = n
curr_col = m

for _ in range(t):
    parts = list(map(int, input().split()))
    op = parts[0]
    if op == 1:
        # 重塑操作
        p, q = parts[1], parts[2]
        curr_row = p
        curr_col = q
    elif op == 2:
        # 转置操作
        new_data = []
        for j in range(curr_col):
            for i in range(curr_row):
                new_data.append(data[i * curr_col + j])
        data = new_data
        curr_row, curr_col = curr_col, curr_row
    elif op == 3:
        # 元素查询
        i, j = parts[1], parts[2]
        idx = i * curr_col + j
        print(data[idx])