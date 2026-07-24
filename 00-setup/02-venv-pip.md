# 第 2 步笔记：venv + pip 环境管理

## 为什么需要虚拟环境

不同项目依赖同一个包的不同版本时会互相冲突。venv 给每个项目一个独立的 Python 环境，
装的包互不影响。这是每个 Python 项目的标准第一步。

## 标准工作流（每个新项目都这样做）

```bash
# 1. 在项目目录创建虚拟环境（只需一次）
python -m venv .venv

# 2. 激活（Git Bash）
source .venv/Scripts/activate
#    激活后命令行前面会出现 (.venv)，which python 应指向项目里的 .venv
#    PowerShell 用：.venv\Scripts\Activate.ps1
#    CMD 用：.venv\Scripts\activate.bat

# 3. 装包（只装进当前环境）
pip install requests

# 4. 查看已装的包
pip list

# 5. 导出依赖清单（别人 clone 你的项目后靠它还原环境）
pip freeze > requirements.txt

# 6. 退出虚拟环境
deactivate
```

别人拿到项目后的还原流程：

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

## 要点

- `.venv/` **永远不提交 Git**（体积大、可重建），`.gitignore` 已包含；`requirements.txt` **必须提交**
- 激活只对当前终端窗口有效，新开窗口要重新激活
- VS Code 打开项目后，右下角选择解释器为 `.venv` 里的 Python，编辑器的终端会自动激活
- 本次实操：在 `00-setup/.venv` 中安装 requests 并成功请求 GitHub API（HTTP 200）

## 常用 pip 命令速查

| 命令 | 作用 |
|---|---|
| `pip install 包名` | 安装最新版 |
| `pip install 包名==1.2.3` | 安装指定版本 |
| `pip uninstall 包名` | 卸载 |
| `pip show 包名` | 查看包详情 |
| `pip list` | 列出所有已装包 |
| `pip freeze > requirements.txt` | 导出依赖清单 |
