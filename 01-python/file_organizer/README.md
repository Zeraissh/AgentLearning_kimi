# 阶段 1 验收项目：file_organizer（命令行文件整理工具）

做一个命令行工具，把指定目录里的文件按扩展名分类移动到子目录。

## 功能要求

```bash
# 实际整理
python organizer.py <目录>

# 演练模式：只打印会做什么，不真的移动文件
python organizer.py <目录> --dry-run
```

- 分类规则：`jpg/png/gif` → `images/`；`txt/md/pdf` → `docs/`；`py/js` → `code/`；其他 → `others/`（规则写在字典里，方便以后扩展）
- 目标子目录不存在时自动创建
- 重名文件不覆盖：自动改名（如 `report.pdf` → `report_1.pdf`）
- 只处理文件，跳过子目录
- 每移动一个文件打印一行日志，最后打印汇总（每类多少个）

## 工程要求

- 代码拆成函数：分类规则、生成目标路径、移动文件、解析命令行参数（`argparse`）各自独立
- 至少 3 个 pytest 测试（提示：用 `tmp_path` fixture 造临时目录来测）
- 本 README 里写清用法（已帮你写了个大概，完成后按实际实现修订）
- 全程用 `file_organizer/` 自己的 git 提交记录开发过程，至少 3 次提交

## 验收清单

- [ ] 功能全部实现，两种模式都工作正常
- [ ] `pytest` 全绿
- [ ] 代码里每个函数有简短 docstring
- [ ] 找我做最终 code review

## 提示

- 标准库就够用：`pathlib`（路径）、`shutil`（移动文件）、`argparse`（命令行参数）
- 先写 `--dry-run` 模式会更容易调试——不用反复手动还原文件
- 卡在某一步超过 30 分钟就提问，提问格式见 `01-python/README.md`
