"""
冒泡排序的实现
Bubble Sort Algorithm Implementation

冒泡排序是一种简单的排序算法。它的基本思想是：通过重复遍历待排序的数列，比较相邻元素并交换顺序不正确的元素，使得较大的元素逐渐“浮”到数列的顶端。以此类推，直到所有元素均排序完毕。

流程图：
https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Bubble_sort_animation_deutsch.gif/640px-Bubble_sort_animation_deutsch.gif

时间复杂度： O(n^2)，额外空间复杂度： O(1)
"""

UNSORTED_ARRAY = [64, 25, 12, 22, 11, 90, 34, 78, 56]

def swap_with_bit(arr, i: int, j: int) -> None:
    """使用位运算交换数组中两个索引位置的元素，异或运算速度较快且不需要额外空间
    
    Args:
        arr (list): 数组
        i (int): 第一个元素的索引
        j (int): 第二个元素的索引
    """
    if i != j: # 避免i和j在同一个地址导致结果为0
        arr[i] = arr[i] ^ arr[j]
        arr[j] = arr[i] ^ arr[j]
        arr[i] = arr[i] ^ arr[j]

def bubble_sort(arr: list) -> list:
    """冒泡排序算法, 将数组按升序排序，返回排序后的数组
    
    Args:
        arr (list): 待排序的数组
    
    Returns:
        排序后的数组
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1): # 遍历未排序部分
            if arr[j] > arr[j + 1]: # 如果当前元素大于下一个元素，交换它们
                swap_with_bit(arr, j, j + 1)
    return arr


def viewed_bubble_sort(arr: list) -> list:
    """冒泡排序算法的可视化版本, 将数组按升序排序，返回排序后的数组
    
    Args:
        arr (list): 待排序的数组
    
    Returns:
        排序后的数组
    """
    print(f"Initial Array: {arr}")
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1): # 遍历未排序部分
            if arr[j] > arr[j + 1]: # 如果当前元素大于下一个元素，交换它们
                swap_with_bit(arr, j, j + 1)
        print(f"Step {i + 1}: {arr}") # 输出当前步骤和数组状态
    return arr


def optimized_bubble_sort(arr: list) -> list:
    """优化后的冒泡排序算法, 将数组按升序排序，返回排序后的数组。通过优化减少不必要的比较次数，使得算法在最佳情况下达到O(n)的时间复杂度。"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swap_with_bit(arr, j, j + 1)
                swapped = True
        if not swapped:  # 如果本轮没有交换，提前结束
            break
    return arr

if __name__ == "__main__":
    import time

    start_time = time.time()
    sorted_array = bubble_sort(UNSORTED_ARRAY.copy())
    end_time = time.time()
    print(f"Sorted Array: {sorted_array}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

    print("\nVisualized Bubble Sort:")
    viewed_bubble_sort(UNSORTED_ARRAY.copy())