"""练习 5：平方列表。

任务：
    1. 用 for 循环生成 1-10 的平方列表，打印
    2. 用列表推导式再生成一次，打印
    3. 用 sum() / max() / min() 打印这个列表的和、最大值、最小值

提示：
    - 循环版：先建空列表，循环里 append
    - 推导式版：[x**2 for x in range(1, 11)]
    - 两版输出应该完全一样，对照检查
"""

# 在下面写你的代码：
# 循环版
nums :list[int] = []
for x in range(1, 11):
    nums.append(x**2)
print("循环版平方列表:", nums)

# 推导式版
nums = [x**2 for x in range(1, 11)]
print("推导式版平方列表:", nums)

# 打印和、最大值、最小值
print("平方列表的和:", sum(nums))
print("平方列表的最大值:", max(nums))
print("平方列表的最小值:", min(nums))
