from typing import Optional


def swap_with_bit(arr: list, i: int, j: int) -> None:
    """使用位运算交换数组中两个索引位置的元素，异或运算速度较快且不需要额外空间
    
    Args:
        arr (list): 数组
        i (int): 第一个元素的索引
        j (int): 第二个元素的索引
    """
    if i is not j: # 避免i和j在同一个地址导致结果为0
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