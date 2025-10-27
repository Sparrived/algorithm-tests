import pytest
import time

from sorting_algorithm import *
from utils import *
from typing import Callable

@pytest.fixture
def unsorted_array():
    return get_random_array(1000, 1, 10000)

def time_mixin(func: Callable, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"{func.__name__} Time: {end_time - start_time} seconds")
    return result


def test_selection_sort(unsorted_array):
    sorted_array = time_mixin(selection_sort, unsorted_array)
    true_sorted = time_mixin(sorted, unsorted_array)
    assert sorted_array == true_sorted


def test_insertion_sort(unsorted_array):
    sorted_array = time_mixin(insertion_sort, unsorted_array)
    true_sorted = time_mixin(sorted, unsorted_array)
    assert sorted_array == true_sorted


def test_bubble_sort(unsorted_array):
    sorted_array = time_mixin(bubble_sort, unsorted_array)
    true_sorted = time_mixin(sorted, unsorted_array)
    assert sorted_array == true_sorted
