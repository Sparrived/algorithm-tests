"""
插入排序的实现
Insertion Sort Algorithm Implementation

插入排序是一种简单直观的排序算法。它的基本思想是：将待排序的元素逐个插入到已排序的序列中，直到所有元素均排序完毕。

流程图：
https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Insertion_sort_001.PNG/640px-Insertion_sort_001.PNG

时间复杂度： O(n^2)，额外空间复杂度： O(1)
"""

from utils import swap_with_bit, get_array_info, UNSORTED_ARRAY

def insertion_sort(arr: list) -> list:
    """插入排序算法, 将数组按升序排序，返回排序后的数组的副本
    
    Args:
        arr (list): 待排序的数组

    Returns:
        排序后的数组副本
    """
    n, arr_copy = get_array_info(arr)
    if not arr_copy:
        return arr
    # 此时 0~0 已排序
    for i in range(1, n): # 从第二个元素开始遍历
        # 从 0~i-1 已排序的序列中找到合适的位置插入 arr[i]
        key = arr_copy[i] # 记录当前元素
        j = i - 1
        while j >= 0 and arr_copy[j] > key: # 从后向前遍历已排序部分，寻找插入位置，当 arr_copy[j] > key 时，将 arr_copy[j] 后移
            swap_with_bit(arr_copy, j + 1, j)
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy

def viewed_insertion_sort(arr: list) -> list:
    """插入排序算法的可视化版本, 将数组按升序排序，返回排序后的数组的副本

    Args:
        arr (list): 待排序的数组

    Returns:
        排序后的数组副本
    """
    print(f"Initial Array: {arr}")
    n, arr_copy = get_array_info(arr)
    if not arr_copy:
        return arr
    for i in range(1, n):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and arr_copy[j] > key:
            swap_with_bit(arr_copy, j + 1, j)
            j -= 1
        arr_copy[j + 1] = key
        print(f"Step {i}: {arr_copy}")
    return arr_copy


if __name__ == "__main__":
    viewed_insertion_sort(UNSORTED_ARRAY)