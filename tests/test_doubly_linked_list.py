#!/usr/bin/env python


import pytest

from dsviz import DoublyLinkedList


## Fixtures

@pytest.fixture
def empty_int_dll():
    return DoublyLinkedList('', int)


@pytest.fixture
def empty_str_dll():
    return DoublyLinkedList('', str)


@pytest.fixture
def int_dll():
    dll = DoublyLinkedList('', int)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    return dll


@pytest.fixture
def full_str_dll():
    dll = DoublyLinkedList('', str, 4)
    dll.append('abc')
    dll.append('def')
    dll.append('ghi')
    dll.append('jkl')
    return dll


## Data structure tests

def test_constructor_with_default_size_limit():
    int_dll = DoublyLinkedList('my int dll', int)
    assert int_dll.max_size == 16


def test_constructor_with_custom_size_limit():
    str_dll = DoublyLinkedList('my str dll', str, 9)
    assert str_dll.max_size == 9


def test_constructor_with_excessive_size_limit():
    float_dll = DoublyLinkedList('my float dll', float, 20)
    assert float_dll.max_size == 16


def test_constructor_with_invalid_size_limit():
    with pytest.raises(IndexError):
        float_dll = DoublyLinkedList('my float dll', float, -2)


def test_constructor_with_invalid_type():
    with pytest.raises(TypeError):
        list_dll = DoublyLinkedList('my list dll', list)


def test_prepend(empty_int_dll):
    empty_int_dll.prepend(5)
    empty_int_dll.prepend(3)
    empty_int_dll.prepend(-1)
    assert len(empty_int_dll) == 3
    expected = [-1, 3, 5]
    for list_val, expected_val in zip(empty_int_dll, expected):
        assert list_val == expected_val


def test_prepend_with_invalid_type(empty_str_dll):
    with pytest.raises(TypeError):
        empty_str_dll.prepend(123)


def test_prepend_with_full_dll(full_str_dll):
    with pytest.raises(IndexError):
        full_str_dll.prepend('asdf')


def test_append(empty_str_dll):
    empty_str_dll.append('foo')
    empty_str_dll.append('bar')
    empty_str_dll.append('123')
    assert len(empty_str_dll) == 3
    expected = ['foo', 'bar', '123']
    for list_val, expected_val in zip(empty_str_dll, expected):
        assert list_val == expected_val


def test_append_with_invalid_type(empty_int_dll):
    with pytest.raises(TypeError):
        empty_int_dll.append(1.1)


def test_append_with_full_dll(full_str_dll):
    with pytest.raises(IndexError):
        full_str_dll.append('asdf')


def test_insert(int_dll):
    int_dll.insert(0, -1)
    int_dll.insert(2, 5)
    int_dll.insert(3, -5)
    assert len(int_dll) == 7
    expected = [-1, 1, 5, -5, 2, 3, 4]
    for list_val, expected_val in zip(int_dll, expected):
        assert list_val == expected_val


def test_insert_with_invalid_type(int_dll):
    with pytest.raises(TypeError):
        int_dll.insert(1, 'a')


def test_insert_with_full_dll(full_str_dll):
    with pytest.raises(IndexError):
        full_str_dll.insert(2, 'a')


def test_insert_with_invalid_position(int_dll):
    with pytest.raises(IndexError):
        int_dll.insert(7, 1)
    with pytest.raises(IndexError):
        int_dll.insert(-1, 3)


def test_delete(full_str_dll):
    full_str_dll.delete('xyz')
    assert len(full_str_dll) == 4
    full_str_dll.delete('abc')
    assert len(full_str_dll) == 3
    full_str_dll.delete('ghi')
    assert len(full_str_dll) == 2
    full_str_dll.delete('jkl')
    assert len(full_str_dll) == 1
    full_str_dll.delete('def')
    assert full_str_dll.is_empty()


def test_delete_with_invalid_type(int_dll):
    with pytest.raises(TypeError):
        int_dll.delete('abc')


def test_search(int_dll):
    assert int_dll.search(5) == -1
    assert int_dll.search(3) == 2


def test_search_with_invalid_type(full_str_dll):
    with pytest.raises(TypeError):
        full_str_dll.search(3)


def test_iter(full_str_dll):
    expected = []
    for list_val, expected_val in zip(full_str_dll, expected):
        assert list_val == expected_val


## Render tests

from dsviz import PROJECT_ROOT

import os
import random
import string


@pytest.fixture
def random_int_dll():
    dll = DoublyLinkedList('TEST Example Integer DLL', int)
    for _ in range(random.randint(1, 16)):
        dll.append(random.randint(-999, 999))
    return dll


@pytest.fixture
def random_str_dll():
    dll = DoublyLinkedList('TEST Example String DLL', str)
    for _ in range(random.randint(1, 16)):
        random_string = ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(random.randint(1, 5)))
        dll.append(random_string)
    return dll


@pytest.fixture
def random_float_dll():
    dll = DoublyLinkedList('TEST Example Float DLL', float)
    for _ in range(random.randint(1, 16)):
        dll.append(random.random() * random.randint(-1000, 1000))
    return dll


@pytest.fixture
def save_path():
    return os.path.join(PROJECT_ROOT, os.pardir, 'images')


def test_render_int_dll(random_int_dll, save_path):
    random_int_dll.render(save_path)


def test_render_str_dll(random_str_dll, save_path):
    random_str_dll.render(save_path)


def test_render_float_dll(random_float_dll, save_path):
    random_float_dll.render(save_path)
