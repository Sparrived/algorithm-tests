"""
选择排序的实现
Selection Sort Algorithm Implementation

选择排序是一种简单直观的排序算法。它的基本思想是：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

流程图：
https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif

时间复杂度： O(n^2)，额外空间复杂度： O(1)
"""

import time


UNSORTED_ARRAY = [64, 25, 12, 22, 11, 90, 34, 78, 56]

def selection_sort(arr: list) -> list:
    """选择排序算法, 将数组按升序排序，返回排序后的数组
    
    Args:
        arr (list): 待排序的数组
    
    Returns:
        排序后的数组
    """
    n = len(arr)
    for i in range(n):
        min_index = i # 记录i位置的索引
        for j in range(i + 1, n): # 从i+1位置开始遍历，寻找最小值
            if arr[j] < arr[min_index]: # 找到更小的值，更新min_index
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] # 交换位置
    return arr


def viewed_selection_sort(arr: list) -> list:
    """选择排序算法的可视化版本, 将数组按升序排序，返回排序后的数组
    
    Args:
        arr (list): 待排序的数组
    
    Returns:
        排序后的数组
    """
    print(f"Initial Array: {arr}")
    n = len(arr)
    for i in range(n):
        min_index = i # 记录i位置的索引
        for j in range(i + 1, n): # 从i+1位置开始遍历，寻找最小值
            if arr[j] < arr[min_index]: # 找到更小的值，更新min_index
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] # 交换位置
        print(f"Step {i + 1}: {arr}") # 输出当前步骤和数组状态
    return arr



if __name__ == "__main__":
    start_time = time.time()
    sorted_array = viewed_selection_sort(UNSORTED_ARRAY.copy())
    end_time = time.time()
    print(f"Selection Sort took {end_time - start_time:.6f} seconds")
    print("Unsorted Array:", UNSORTED_ARRAY)
    print("Sorted Array:", sorted_array)