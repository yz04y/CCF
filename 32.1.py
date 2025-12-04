# 读取输入
n, m = map(int, input().split())
warehouses = []
for _ in range(n):
    code = list(map(int, input().split()))
    warehouses.append(code)

# 遍历每个仓库，寻找上级
for i in range(n):
    current = warehouses[i]
    upper = 0  # 初始化为0（无上级）
    # 遍历所有仓库j（按编号从小到大，确保找到最小编号）
    for j in range(n):
        # 检查j的每一维是否都大于i的对应维
        valid = True
        for k in range(m):
            if warehouses[j][k] <= current[k]:
                valid = False
                break
        if valid:
            upper = j + 1  # 仓库编号是j+1（因为j是0-based索引）
            break  # 找到第一个满足条件的j，直接跳出
    print(upper)