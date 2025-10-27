# 通过 Python 实现的算法测试

这是我的一个学习仓库，旨在将学习的算法通过 Python 语言实现。

## 📋 项目简介

本项目使用 Python 3.12+ 实现各种经典算法，每个算法都包含：
- 详细的中文注释和说明
- 时间复杂度和空间复杂度分析
- 可视化输出版本
- 实际运行示例

## 🚀 快速开始

### 环境要求

- Python 3.12 或更高版本
- 推荐使用虚拟环境

### 安装

强烈推荐使用 [uv](https://github.com/astral-sh/uv) 管理 Python 环境与依赖

```bash
# 克隆仓库
git clone https://github.com/Sparrived/algorithm-tests.git
cd algorithm-tests

# 推荐使用 uv 管理环境
uv sync
```

### 运行示例

```bash
# 运行选择排序示例
uv run sorting-algorithm/selection_sort.py
```

## 📚 目前学习进度

### 🔄 学习中

- **排序算法 (sorting-algorithm)**
  - ✅ 选择排序 (Selection Sort)
  - ✅ 冒泡排序 (Bubble Sort)
  - ✅ 插入排序 (Insertion Sort)

### 📝 计划学习

- 排序算法
  - [ ] 快速排序 (Quick Sort)
  - [ ] 归并排序 (Merge Sort)
  - [ ] 堆排序 (Heap Sort)
- 搜索算法
  - [ ] 二分查找 (Binary Search)
  - [ ] 深度优先搜索 (DFS)
  - [ ] 广度优先搜索 (BFS)
- 数据结构
  - [ ] 链表 (Linked List)
  - [ ] 栈 (Stack)
  - [ ] 队列 (Queue)
  - [ ] 树 (Tree)

### ✅ 已完成

- 暂无

## 📂 仓库结构

```
algorithm-tests/
├── README.md                      # 项目说明文档
├── pyproject.toml                 # 项目配置文件
└── sorting-algorithm/             # 排序算法目录
  ├── README.md                 # 排序算法说明文档
  ├── selection_sort.py         # 选择排序实现
  ├── bubble_sort.py            # 冒泡排序实现
  ├── insertion_sort.py         # 插入排序实现
  └── utils.py                  # 工具函数
```

## 🤝 贡献

如果你在代码中发现错误，欢迎提交 Issue 或 Pull Request！

## 📄 许可证

本项目仅用于学习目的。

## 📧 联系方式

如有问题或建议，欢迎通过 Issue 与我交流。

---

**持续更新中... 💪**