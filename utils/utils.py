import random
from typing import Optional

def swap_with_bit(arr: list, i: int, j: int) -> None:
    """使用位运算交换数组中两个索引位置的元素，异或运算速度较快且不需要额外空间
    
    Args:
        arr (list): 数组
        i (int): 第一个元素的索引
        j (int): 第二个元素的索引
    """
    if arr[i] is not arr[j]: # 避免i和j在同一个地址导致结果为0
        arr[i] = arr[i] ^ arr[j]
        arr[j] = arr[i] ^ arr[j]
        arr[i] = arr[i] ^ arr[j]

def get_array_info(arr: list) -> tuple[int, Optional[list]]:
    """获取数组的长度和副本，如果数组为空或只有一个元素，返回None作为副本
    
    Args:
        arr (list): 数组

    Returns:
        包含数组长度和数组副本的元组
    """ 
    if not arr or len(arr) < 2: # arr没有元素或一个元素的情况下不需要排序
        return 0, None
    return len(arr), arr.copy()

def get_random_array(size: int, min_value: int, max_value: int, seed: Optional[int] = None) -> list[int]:
    """生成一个指定大小和范围的随机数组

    Args:
        size (int): 数组大小
        min_value (int): 最小值
        max_value (int): 最大值
        seed (Optional[int]): 随机数种子

    Returns:
        list[int]: 生成的随机数组
    """
    if seed is not None:
        random.seed(seed)
    return [random.randint(min_value, max_value) for _ in range(size)]

UNSORTED_ARRAY = get_random_array(10, 1, 100, seed=42)