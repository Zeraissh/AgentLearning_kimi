# 第 3 步笔记：Git 基本流程

## 三个区域（理解这个就理解了 Git 的一半）

```
工作目录  --git add-->  暂存区  --git commit-->  本地仓库  --git push-->  远程仓库
(你改文件)              (装箱待寄)              (本地存档)                 (GitHub)
```

`git status` 是你最常用的命令，随时告诉你文件处在哪个区域。

## 日常循环（每天写代码都是这几步）

```bash
git status                  # 看状态
git add <文件>              # 装箱（git add -A 装全部）
git commit -m "信息"        # 本地存档
git push                    # 寄到 GitHub
```

反向操作：

```bash
git pull                    # 把远程的新提交拉下来（多设备/协作时用）
git log --oneline           # 看提交历史
git diff                    # 看还没 add 的改动
```

## 分支（branch）——本次实操的完整流程

分支的意义：在不影响 main 的情况下开发新东西，完成了再合并回来。

```bash
git switch -c 分支名        # 创建并切换到新分支
# ... 在新分支上改文件、add、commit ...
git switch main             # 切回 main（分支上的文件在 main 上看不到）
git merge 分支名            # 把分支的提交合并进 main
git branch -d 分支名        # 合并完成后删除分支
```

本次实操：`practice/git-flow` 分支上新增文件 → 切回 main 文件"消失" → merge 后文件出现
→ 删除分支。这就是以后每个功能的开发流程。

## 要点

- **小步提交**：每完成一个小功能就 commit，提交信息写清做了什么（动词开头，如 `add:`、`fix:`、`docs:`）
- **push 前 `git status`**：确认没有遗漏未提交的文件
- **`.gitignore` 生效前已提交的文件不会被忽略**，需要 `git rm --cached <文件>` 先移出
- 误创建了分支（如本次的 `help`）：先 `git log main..分支名` 确认无独有提交，再 `git branch -d 分支名`

## 后续进阶（阶段 1 再深入）

- 撤销：`git restore`、`git reset`（改历史，慎用）
- 协作：fork、Pull Request——阶段 4 给开源项目提 PR 时会用到
- 冲突解决：merge 报 conflict 时怎么处理
