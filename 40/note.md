# 40.2 思考
## 40.2采用了逆向计算的逻辑

### 40.2.py 代码实现


#### 核心逻辑：这是逆向变换的核心，基于异或运算的可逆性： 若 A ⊕ B = C，则 B = A ⊕ C

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def f(b, k):
    mod = 1 << 9  # 2^9 = 512
    return ((b * b + k * k) % mod) ^ k

def reverse_g(y, k):
    # 先将y截断为低9位
    y = y & 0x1ff  # 0x1ff是9位全1的掩码
    # 将y拆分为新的高3位、中3位、低3位（9位二进制）
    y_bin = bin(y)[2:].zfill(9)  # 补前导0到9位
    y_a = int(y_bin[:3], 2)  # 新的高3位（对应原b）
    y_b = int(y_bin[3:6], 2) # 新的中3位
    y_c = int(y_bin[6:], 2)  # 新的低3位
    
    # 逆向计算原a、b、c
    b = y_a & 0x7  # 确保b是3位二进制数（0-7）
    fb = f(b, k) & 0x7  # 只使用fb的低3位
    c = (y_b ^ fb) & 0x7  # 确保c是3位二进制数（0-7）
    fc = f(c, k) & 0x7  # 只使用fc的低3位
    a = (y_c ^ fc) & 0x7  # 确保a是3位二进制数（0-7）
    
    # 拼接原a、b、c为x
    x_bin = bin(a)[2:].zfill(3) + bin(b)[2:].zfill(3) + bin(c)[2:].zfill(3)
    return int(x_bin, 2)

n, m = map(int, input().split())
k_list = list(map(int, input().split()))
a_list = list(map(int, input().split()))

result = []
for a in a_list:
    current = a
    # 逆向执行m次变换（从k_m到k_1）
    for k in reversed(k_list):
        current = reverse_g(current, k)
    result.append(current)

print(' '.join(map(str, result)))
```