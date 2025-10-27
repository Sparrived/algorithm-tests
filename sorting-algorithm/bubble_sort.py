"""
冒泡排序的实现
Bubble Sort Algorithm Implementation

冒泡排序是一种简单的排序算法。它的基本思想是：通过重复遍历待排序的数列，比较相邻元素并交换顺序不正确的元素，使得较大的元素逐渐“浮”到数列的顶端。以此类推，直到所有元素均排序完毕。

流程图：
https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Bubble_sort_animation_deutsch.gif/640px-Bubble_sort_animation_deutsch.gif

时间复杂度： O(n^2)，额外空间复杂度： O(1)
"""

from utils import swap_with_bit, get_array_info, UNSORTED_ARRAY


def bubble_sort(arr: list) -> list:
    """冒泡排序算法, 将数组按升序排序，返回排序后的数组
    
    Args:
        arr (list): 待排序的数组
    
    Returns:
        排序后的数组
    """
    n, arr_copy = get_array_info(arr)
    if not arr_copy:
        return arr
    for i in range(n):
        for j in range(0, n - i - 1): # 遍历未排序部分
            if arr_copy[j] > arr_copy[j + 1]: # 如果当前元素大于下一个元素，交换它们
                swap_with_bit(arr_copy, j, j + 1)
    return arr_copy


def viewed_bubble_sort(arr: list) -> list:
    """冒泡排序算法的可视化版本, 将数组按升序排序，返回排序后的数组
    
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
        for j in range(0, n - i - 1): # 遍历未排序部分
            if arr_copy[j] > arr_copy[j + 1]: # 如果当前元素大于下一个元素，交换它们
                swap_with_bit(arr_copy, j, j + 1)
        print(f"Step {i + 1}: {arr_copy}") # 输出当前步骤和数组状态
    return arr_copy


def optimized_bubble_sort(arr: list) -> list:
    """优化后的冒泡排序算法, 将数组按升序排序，返回排序后的数组。通过优化减少不必要的比较次数，使得算法在最佳情况下达到O(n)的时间复杂度。"""
    n, arr_copy = get_array_info(arr)
    if not arr_copy:
        return arr
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                swap_with_bit(arr_copy, j, j + 1)
                swapped = True
        if not swapped:  # 如果本轮没有交换，提前结束
            break
    return arr_copy

if __name__ == "__main__":
    viewed_bubble_sort(UNSORTED_ARRAY)