"""练习 9：函数综合。

任务：
    1. 写函数 greet(name, greeting="你好")：返回一句问候语（注意是 return 不是 print）
       默认参数调用一次，自定义问候语调用一次，都打印出来
    2. 写函数 total(*nums)：接收任意多个数字，返回它们的和
       测试：total(1, 2)、total(1, 2, 3, 4, 5)、total()
    3. 写函数 make_profile(name, **info)：把 name 和任意关键字参数存进一个字典返回
       测试：make_profile("小明", age=15, city="佛山")
    4. 思考一下：练习 8 里的 lambda x: x[1] 现在能看懂了吗？
       把它改写成一个普通函数（def），用在 sorted 的 key 里

提示：*nums 打包成元组，**info 打包成字典
"""

# 在下面写你的代码：
def greet(name: str, greeting: str = "你好") -> str:
      return f"{greeting}, {name}!"

def total(*nums: int) -> int:
      return sum(nums)

def make_profile(name: str, **info) -> dict:
      profile = {"name": name}
      profile.update(info)
      return profile

def sort_by_second_element(lst: list[tuple]) -> list[tuple]:
      return sorted(lst, key=lambda x: x[1])

name = "小明"
print(greet(name))
print(greet(name, "早上好"))
print(total(1, 2))
print(total(1, 2, 3, 4, 5))
print(total())
print(make_profile("小明", age=15, city="佛山"))
print(sort_by_second_element([(1, 3), (2, 2), (3, 1)]))
