def main6():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    a = list(map(int, data[1:2 + n]))
    b = list(map(int, data[2 + n:2 + 2 * n]))

    # 计算正常情况下的前缀和
    prefix = [0] * (n + 2)
    for i in range(n + 1):
        prefix[i + 1] = prefix[i] - a[i] + (b[i - 1] if i > 0 else 0)

    # 计算前缀最小值
    pre_min = [0] * (n + 2)
    pre_min[0] = 0
    for i in range(1, n + 2):
        pre_min[i] = min(pre_min[i - 1], prefix[i])

    # 计算后缀最小值
    suf_min = [0] * (n + 2)
    suf_min[n + 1] = float('inf')
    for i in range(n, -1, -1):
        suf_min[i] = min(prefix[i + 1], suf_min[i + 1])

    result = []
    for i in range(n):
        # 当第i个区域没有补给时
        # 第i+1步之后的能量都会减少b[i]
        min_energy = min(
            pre_min[i + 1],  # i步之前的最小值
            prefix[i + 1] + (suf_min[i + 1] - b[i] - prefix[i + 1])  # i步之后的最小值（调整后）
        )
        w = max(a[0], -min_energy)
        result.append(str(w))

    print(" ".join(result))


main6()
