import pytest

from sorting_algorithm import *
from utils import *

@pytest.fixture
def unsorted_array():
    return get_random_array(1000, 1, 10000)


def test_selection_sort(unsorted_array):
    assert selection_sort(unsorted_array) == sorted(unsorted_array)


def test_insertion_sort(unsorted_array):
    assert insertion_sort(unsorted_array) == sorted(unsorted_array)


def test_bubble_sort(unsorted_array):
    assert bubble_sort(unsorted_array) == sorted(unsorted_array)


def test_optimized_bubble_sort(unsorted_array):
    assert optimized_bubble_sort(unsorted_array) == sorted(unsorted_array)


def test_merge_sort(unsorted_array):
    assert merge_sort(unsorted_array) == sorted(unsorted_array)