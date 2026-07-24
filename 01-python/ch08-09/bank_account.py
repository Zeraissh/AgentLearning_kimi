"""练习 10：类——银行账户。

任务：实现一个 BankAccount 类：
    1. 初始化时传入户主名和初始余额（__init__）
    2. deposit(amount)：存钱，余额增加，打印流水
    3. withdraw(amount)：取钱，余额不足时打印提示并且不扣款
    4. get_balance()：返回当前余额
    5. 再写一个子类 SavingsAccount 继承 BankAccount，
       增加 add_interest(rate) 方法：按利率给余额加息（如 0.03 表示 3%）

测试流程：
    账户存入 1000 → 取 300 → 取 9999（应提示不足）→ 打印余额（应为 700）
    储蓄账户存入 1000 → 加 3% 利息 → 打印余额（应为 1030）

提示：类名用驼峰命名（BankAccount），方法名用下划线命名（get_balance）
"""

# 在下面写你的代码：

