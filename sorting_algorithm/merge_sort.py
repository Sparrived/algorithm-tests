"""
归并排序的实现
Merge Sort Algorithm Implementation

归并排序是一种分治法（Divide and Conquer）的排序算法。它的基本思想是：将待排序的数组分成两半，分别对这两半进行排序，然后再将它们合并在一起。

流程图：
https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/MergeSort.jpg/640px-MergeSort.jpg

时间复杂度： O(n log n)，额外空间复杂度： O(n)
"""

from pathlib import Path
import sys

if __package__ in {None, ""}:  # 允许脚本独立运行
    project_root = Path(__file__).resolve().parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

from utils import *

def merge_sort(arr: list) -> list:
    """归并排序算法, 将数组按升序排序，返回排序后的数组
    
    Args:
        arr (list): 待排序的数组
    
    Returns:
        排序后的数组
    """
    n, arr_copy = get_array_info(arr)
    if not arr_copy:
        return arr

    def merge(left: list, right: list) -> list:
        """合并两个有序数组"""
        merged = [] # 记录合并后的数组，其他语言应固定大小以提升性能
        pl = pr = 0 # 分别为left和right的指针
        L = len(left)
        R = len(right)
        while pl < L and pr < R: # 两个数组均未遍历完
            if left[pl] <= right[pr]:
                merged.append(left[pl])
                pl += 1
            else:
                merged.append(right[pr])
                pr += 1
        # 将剩余元素加入merged
        merged.extend(left[pl:] if pl < L else right[pr:])
        return merged

    def sort(sub_arr: list) -> list:
        """递归排序子数组"""
        if len(sub_arr) <= 1:
            return sub_arr
        mid = len(sub_arr) // 2
        left_half = sort(sub_arr[:mid])
        right_half = sort(sub_arr[mid:])
        return merge(left_half, right_half)

    return sort(arr_copy)

def viewed_merge_sort(arr: list) -> list:
    """归并排序算法的可视化版本, 将数组按升序排序，返回排序后的数组
    
    Args:
        arr (list): 待排序的数组
    
    Returns:
        排序后的数组
    """
    print(f"Initial Array: {arr}")
    n, arr_copy = get_array_info(arr)
    if not arr_copy:
        return arr

    def merge(left: list, right: list) -> list:
        """合并两个有序数组"""
        merged = [] # 记录合并后的数组，其他语言应固定大小以提升性能
        pl = pr = 0 # 分别为left和right的指针
        L = len(left)
        R = len(right)
        while pl < L and pr < R: # 两个数组均未遍历完
            if left[pl] <= right[pr]:
                merged.append(left[pl])
                pl += 1
            else:
                merged.append(right[pr])
                pr += 1
        # 将剩余元素加入merged
        merged.extend(left[pl:] if pl < L else right[pr:])
        print(f"Merging: {left} and {right} => {merged}")
        return merged

    def sort(sub_arr: list) -> list:
        """递归排序子数组"""
        if len(sub_arr) <= 1:
            return sub_arr
        mid = len(sub_arr) // 2
        left_half = sort(sub_arr[:mid])
        right_half = sort(sub_arr[mid:])
        return merge(left_half, right_half)

    sorted_arr = sort(arr_copy)
    print(f"Sorted Array: {sorted_arr}")
    return sorted_arr

@time_mixin
def merge_sort_with_mixin(arr: list) -> list:
    """带有时间统计的归并排序算法包装器"""
    return merge_sort(arr)

@time_mixin
def viewed_merge_sort_with_mixin(arr: list) -> list:    
    """带有时间统计的可视化归并排序算法包装器"""
    return viewed_merge_sort(arr)


if __name__ == "__main__":
    print("=" * 20 + " Merge Sort " + "=" * 20)
    run_test(merge_sort_with_mixin)
    print("=" * 20 + " Viewed Merge Sort " + "=" * 20)
    run_test(viewed_merge_sort_with_mixin, UNSORTED_ARRAY)