"""
选择排序的实现
Selection Sort Algorithm Implementation

选择排序是一种简单直观的排序算法。它的基本思想是：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

流程图：
https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif

时间复杂度： O(n^2)，额外空间复杂度： O(1)
"""

from pathlib import Path
import sys

if __package__ in {None, ""}:  # 允许脚本独立运行
    project_root = Path(__file__).resolve().parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

from utils import *


def selection_sort(arr: list) -> list:
    """选择排序算法, 将数组按升序排序，返回排序后的数组
    
    Args:
        arr (list): 待排序的数组
    
    Returns:
        排序后的数组
    """
    n, arr_copy = get_array_info(arr)
    if not arr_copy:
        return arr
    for i in range(n):
        min_index = i # 记录i位置的索引
        for j in range(i + 1, n): # 从i+1位置开始遍历，寻找最小值
            if arr_copy[j] < arr_copy[min_index]: # 找到更小的值，更新min_index
                min_index = j
        swap_with_bit(arr_copy, i, min_index) # 交换位置
    return arr_copy


def viewed_selection_sort(arr: list) -> list:
    """选择排序算法的可视化版本, 将数组按升序排序，返回排序后的数组
    
    Args:
        arr (list): 待排序的数组
    
    Returns:
        排序后的数组
    """
    print(f"Initial Array: {arr}")
    n, arr_copy = get_array_info(arr)
    if not arr_copy:
        return arr
    for i in range(n):
        min_index = i # 记录i位置的索引
        for j in range(i + 1, n): # 从i+1位置开始遍历，寻找最小值
            if arr_copy[j] < arr_copy[min_index]: # 找到更小的值，更新min_index
                min_index = j
        swap_with_bit(arr_copy, i, min_index) # 交换位置
        print(f"Step {i + 1}: {arr_copy}") # 输出当前步骤和数组状态
    return arr_copy


@time_mixin
def selection_sort_with_mixin(arr: list) -> list:
    """带有时间统计的选择排序算法包装器"""
    return selection_sort(arr)

@time_mixin
def viewed_selection_sort_with_mixin(arr: list) -> list:
    """带有时间统计的可视化选择排序算法包装器"""
    return viewed_selection_sort(arr)

if __name__ == "__main__":
    print("=" * 20 + " Selection Sort " + "=" * 20)
    run_test(selection_sort_with_mixin)
    print("=" * 20 + " Viewed Selection Sort " + "=" * 20)
    run_test(viewed_selection_sort_with_mixin, UNSORTED_ARRAY)