n, m = map(int, input().split())
a = list(map(int, input().split()))
# 调整a的下标为元素值（元素1对应a[1]，元素2对应a[2]...）
# 原a是a1到an，所以在列表前加一个占位符（索引0不用）
a = [0] + a  

# 读取m个S集合：存储每个S的元素集合和异或哈希
S_list = []
for _ in range(m):
    parts = list(map(int, input().split()))
    size = parts[0]
    elements = parts[1:]
    # 计算异或哈希
    xor_sum = 0
    for num in elements:
        xor_sum ^= a[num]
    S_list.append( (set(elements), xor_sum) )

# 读取m个T集合：存储每个T的元素集合和异或哈希
T_list = []
for _ in range(m):
    parts = list(map(int, input().split()))
    size = parts[0]
    elements = parts[1:]
    # 计算异或哈希
    xor_sum = 0
    for num in elements:
        xor_sum ^= a[num]
    T_list.append( (set(elements), xor_sum) )

# 逐查询判断
for i in range(m):
    S_set, S_xor = S_list[i]
    T_set, T_xor = T_list[i]
    # 实际集合是否相等
    actual_equal = (S_set == T_set)
    # 异或哈希是否相等
    hash_equal = (S_xor == T_xor)
    # 只有当“哈希相等”和“实际相等”同时成立 或 同时不成立时，小C的方法才正确
    if actual_equal == hash_equal:
        print("correct")
    else:
        print("wrong")