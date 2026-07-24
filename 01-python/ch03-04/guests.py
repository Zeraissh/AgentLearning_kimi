"""练习 4：客人名单。

任务：
    1. 创建一个列表 guests，初始有 3 位客人
    2. 末尾追加 1 位（append）
    3. 在中间位置插入 1 位（insert）
    4. 删除 1 位（remove 或 pop，想清楚区别）
    5. 打印排序后的名单（不改变原列表，用 sorted）
    6. 打印名单总人数（len）

提示：每一步之后都 print 一次列表，观察它的变化——这是理解"原地修改"的最好方式
"""

# 在下面写你的代码：
guests :list[str] = ["Alice", "Bob", "Charlie"]
print("初始名单:", guests)
# 末尾追加 1 位
guests.append("David")
print("追加后的名单:", guests)

# 在中间位置插入 1 位
guests.insert(2, "Eve")
print("插入后的名单:", guests)

# 删除 1 位
guests.remove("Bob")
print("删除后的名单:", guests)

# 打印排序后的名单（不改变原列表）
print("排序后的名单:", sorted(guests))

# 打印名单总人数
print("名单总人数:", len(guests))
