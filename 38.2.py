from collections import deque

# 读取输入
n, k = map(int, input().split())
x, y = map(int, input().split())

# 定义8个方向的坐标变化
directions = [
    (1, 2), (1, -2),
    (-1, 2), (-1, -2),
    (2, 1), (2, -1),
    (-2, 1), (-2, -1)
]

# 已访问的方格集合（初始包含起始位置）
visited = set()
visited.add((x, y))
# BFS队列：每个元素是 (当前x, 当前y, 当前步数)
q = deque()
q.append((x, y, 0))

while q:
    cx, cy, step = q.popleft()
    # 如果当前步数已达k，不再继续扩展
    if step >= k:
        continue
    # 遍历8个方向
    for dx, dy in directions:
        nx = cx + dx
        ny = cy + dy
        # 判断新位置是否在场地内，且未被访问过
        if 1 <= nx <= n and 1 <= ny <= n and (nx, ny) not in visited:
            visited.add((nx, ny))
            q.append((nx, ny, step + 1))

# 已访问集合的大小就是可达的方格总数
print(len(visited))