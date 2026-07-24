"""练习 11：文件与异常。

任务：
    1. 把今天的学习心得（3 行文字）写入 notes.txt
    2. 读出来并打印
    3. 用 JSON 把 fav_numbers 字典（练习 7 那个）存进 numbers.json，再读回来打印
    4. 尝试读取一个不存在的文件 missing.txt，
       用 try/except 捕获 FileNotFoundError，打印友好的提示而不是让程序崩溃
    5. 尝试把 "abc" 转成 int，捕获 ValueError 并打印提示

提示：
    - 写文件：with open("notes.txt", "w", encoding="utf-8") as f: f.write(...)
    - JSON：import json; json.dump(data, f) / json.load(f)
    - 读写文本文件都加上 encoding="utf-8"，不然 Windows 上中文会变乱码
"""

# 在下面写你的代码：

