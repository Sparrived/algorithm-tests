# 排序算法 (sorting-algorithm)

**使用示例**:
```python
from sorting-algorithm.selection_sort import selection_sort

arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)  # [11, 12, 22, 25, 64]
```

## 选择排序 (Selection Sort)

**文件**: `sorting-algorithm/selection_sort.py`

**算法描述**: 
选择排序是一种简单直观的排序算法。它的基本思想是：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

**复杂度分析**:
- ⏱️ 时间复杂度: O(n²)
  - 最好情况: O(n²)
  - 平均情况: O(n²)
  - 最坏情况: O(n²)
- 💾 空间复杂度: O(1)
- 稳定性: 不稳定

**特点**:
- ✅ 实现简单，易于理解
- ✅ 原地排序，空间复杂度低
- ❌ 时间复杂度较高，不适合大数据集
- ❌ 不稳定排序

