#!/usr/bin/env python


import pytest

from dsviz import BinaryHeap


## Fixtures

@pytest.fixture
def empty_int_min_heap():
    return BinaryHeap('', int)


@pytest.fixture
def empty_str_max_heap():
    return BinaryHeap('', str, 32, False)


@pytest.fixture
def full_str_min_heap():
    min_heap = BinaryHeap('', str, 6)
    min_heap.insert('abc')
    min_heap.insert('zzzzz')
    min_heap.insert('bar')
    min_heap.insert('foo')
    min_heap.insert('ba')
    min_heap.insert('cba')
    return min_heap


@pytest.fixture
def full_int_max_heap():
    max_heap = BinaryHeap('', int, 6, False)
    max_heap.insert(5)
    max_heap.insert(-500)
    max_heap.insert(20)
    max_heap.insert(17)
    max_heap.insert(18)
    max_heap.insert(0)
    return max_heap


## Data structure tests

def test_constructor_with_default_size_limit():
    int_min_heap = BinaryHeap('my int min heap', int)
    assert int_min_heap.max_size == 32


def test_constructor_with_custom_size_limit():
    float_max_heap = BinaryHeap('my float max heap', float, 7, False)
    assert float_max_heap.max_size == 7


def test_constructor_with_excessive_size_limit():
    str_min_heap = BinaryHeap('my str min heap', str, 33)
    assert str_min_heap.max_size == 32


def test_constructor_with_invalid_size_limit():
    with pytest.raises(IndexError):
        int_max_heap = BinaryHeap('my int max heap', int, -1, False)


def test_constructor_with_invalid_type():
    with pytest.raises(TypeError):
        bool_min_heap = BinaryHeap('my bool min heap', bool)


def test_insert(empty_int_min_heap):
    empty_int_min_heap.insert(5)
    empty_int_min_heap.insert(8)
    empty_int_min_heap.insert(7)
    assert len(empty_int_min_heap) == 3
    assert empty_int_min_heap.peek() == 5


def test_insert_with_invalid_type(empty_str_max_heap):
    with pytest.raises(TypeError):
        empty_str_max_heap.insert(1.1)


def test_extract_min_heap(full_str_min_heap):
    sorted_list = []
    while not full_str_min_heap.is_empty():
        sorted_list.append(full_str_min_heap.extract())
    assert sorted_list == sorted(sorted_list)


def test_extract_max_heap(full_int_max_heap):
    sorted_list = []
    while not full_int_max_heap.is_empty():
        sorted_list.append(full_int_max_heap.extract())
    assert sorted_list == sorted(sorted_list, reverse=True)


def test_extract_with_empty_heap(empty_int_min_heap):
    with pytest.raises(IndexError):
        empty_int_min_heap.extract()


def test_peek_min_heap(full_str_min_heap):
    old_len = len(full_str_min_heap)
    min_value = full_str_min_heap.peek()
    assert len(full_str_min_heap) == old_len
    values = []
    while not full_str_min_heap.is_empty():
        values.append(full_str_min_heap.extract())
    assert min_value == min(values)


def test_peek_max_heap(full_int_max_heap):
    old_len = len(full_int_max_heap)
    max_value = full_int_max_heap.peek()
    assert len(full_int_max_heap) == old_len
    values = []
    while not full_int_max_heap.is_empty():
        values.append(full_int_max_heap.extract())
    assert max_value == max(values)


def test_peek_with_empty_heap(empty_str_max_heap):
    with pytest.raises(IndexError):
        empty_str_max_heap.peek()


## Render tests

from dsviz import PROJECT_ROOT

import os
import random
import string


@pytest.fixture
def random_int_min_heap():
    min_heap = BinaryHeap('TEST Example Integer Min Heap', int)
    for _ in range(random.randint(1, 32)):
        min_heap.insert(random.randint(-999, 999))
    return min_heap


@pytest.fixture
def random_str_max_heap():
    max_heap = BinaryHeap('TEST Example String Max Heap', str, 32, False)
    for _ in range(random.randint(1, 32)):
        random_string = ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(random.randint(1, 5)))
        max_heap.insert(random_string)
    return max_heap


@pytest.fixture
def random_float_min_heap():
    min_heap = BinaryHeap('TEST Example Float Min Heap', float)
    for _ in range(random.randint(1, 32)):
        min_heap.insert(random.random() * random.randint(-999, 999))
    return min_heap


@pytest.fixture
def save_path():
    return os.path.join(PROJECT_ROOT, os.pardir, 'images')


def test_render_int_min_heap(random_int_min_heap, save_path):
    random_int_min_heap.render(save_path)


def test_render_str_max_heap(random_str_max_heap, save_path):
    random_str_max_heap.render(save_path)


def test_render_float_min_heap(random_float_min_heap, save_path):
    random_float_min_heap.render(save_path)
