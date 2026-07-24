"""练习 7：幸运数字（字典）。

任务：
    1. 创建字典 fav_numbers，存 5 个人名和各自的幸运数字
    2. 用 for 循环遍历字典，逐行打印："某某的幸运数字是 X"
    3. 查一次不存在的名字：用 get() 并给默认值，对比直接用 [] 查询会发生什么（可以注释掉会报错的那行）

提示：遍历字典用 for name, num in fav_numbers.items()
"""

# 在下面写你的代码：
fav_numbers :dict[str, int] = {
    "Alice": 7,
    "Bob": 3,
    "Charlie": 9,
    "David": 5,
    "Eve": 2
}
for name, num in fav_numbers.items():
    print(f"{name}的幸运数字是 {num}")

# 查一次不存在的名字
print("Frank的幸运数字是", fav_numbers.get("Frank", "未知"))
# print(fav_numbers["Frank"])  # 直接用 [] 查询会报错
