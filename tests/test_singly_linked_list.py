#!/usr/bin/env python


import pytest

from dsviz import SinglyLinkedList


## Fixtures

@pytest.fixture
def empty_int_sll():
    return SinglyLinkedList('', int)


@pytest.fixture
def empty_str_sll():
    return SinglyLinkedList('', str)


@pytest.fixture
def int_sll():
    sll = SinglyLinkedList('', int)
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    return sll


@pytest.fixture
def full_int_sll():
    sll = SinglyLinkedList('', int, 4)
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    return sll


## Data structure tests

def test_constructor_with_default_size_limit():
    int_sll = SinglyLinkedList('my int sll', int)
    assert int_sll.max_size == 16


def test_constructor_with_custom_size_limit():
    str_sll = SinglyLinkedList('my str sll', str, 15)
    assert str_sll.max_size == 15


def test_constructor_with_excessive_size_limit():
    float_sll = SinglyLinkedList('my float sll', float, 20)
    assert float_sll.max_size == 16


def test_constructor_with_invalid_size_limit():
    with pytest.raises(IndexError):
        int_sll = SinglyLinkedList('my int sll', int, -1)


def test_constructor_with_invalid_type():
    with pytest.raises(TypeError):
        set_sll = SinglyLinkedList('my set sll', set)


def test_prepend(empty_int_sll):
    empty_int_sll.prepend(5)
    empty_int_sll.prepend(3)
    empty_int_sll.prepend(-1)
    assert len(empty_int_sll) == 3
    expected = [-1, 3, 5]
    for list_val, expected_val in zip(empty_int_sll, expected):
        assert list_val == expected_val


def test_prepend_with_invalid_type(empty_str_sll):
    with pytest.raises(TypeError):
        empty_str_sll.prepend(5)


def test_prepend_with_full_sll(full_int_sll):
    with pytest.raises(IndexError):
        full_int_sll.prepend(20)


def test_append(empty_str_sll):
    empty_str_sll.append('foo')
    empty_str_sll.append('bar')
    empty_str_sll.append('123')
    assert len(empty_str_sll) == 3
    expected = ['foo', 'bar', '123']
    for list_val, expected_val in zip(empty_str_sll, expected):
        assert list_val == expected_val

def test_append_with_invalid_type(empty_int_sll):
    with pytest.raises(TypeError):
        empty_int_sll.append('asdf')


def test_append_with_full_sll(full_int_sll):
    with pytest.raises(IndexError):
        full_int_sll.append(1)


def test_insert(int_sll):
    int_sll.insert(0, -1)
    int_sll.insert(2, 5)
    int_sll.insert(3, -5)
    assert len(int_sll) == 7
    expected = [-1, 1, 5, -5, 2, 3, 4]
    for list_val, expected_val in zip(int_sll, expected):
        assert list_val == expected_val


def test_insert_with_invalid_type(int_sll):
    with pytest.raises(TypeError):
        int_sll.insert(0, 'a')


def test_insert_with_full_sll(full_int_sll):
    with pytest.raises(IndexError):
        full_int_sll.insert(2, 5)


def test_insert_with_invalid_position(int_sll):
    with pytest.raises(IndexError):
        int_sll.insert(7, 5)
    with pytest.raises(IndexError):
        int_sll.insert(-1, 3)


def test_delete(full_int_sll):
    full_int_sll.delete(5)
    assert len(full_int_sll) == 4
    full_int_sll.delete(3)
    assert len(full_int_sll) == 3
    full_int_sll.delete(4)
    assert len(full_int_sll) == 2
    full_int_sll.delete(1)
    assert len(full_int_sll) == 1
    full_int_sll.delete(2)
    assert full_int_sll.is_empty()


def test_delete_with_invalid_type(int_sll):
    with pytest.raises(TypeError):
        int_sll.delete('a')


def test_search(int_sll):
    assert int_sll.search(5) == -1
    assert int_sll.search(3) == 2


def test_search_with_invalid_type(int_sll):
    with pytest.raises(TypeError):
        int_sll.search(3.3)


def test_iter(int_sll):
    expected = [1, 2, 3, 4]
    for list_val, expected_val in zip(int_sll, expected):
        assert list_val == expected_val


## Render tests

from dsviz import PROJECT_ROOT

import os
import random
import string


@pytest.fixture
def random_int_sll():
    sll = SinglyLinkedList('TEST Example Integer SLL', int)
    for _ in range(random.randint(1, 16)):
        sll.append(random.randint(-999, 999))
    return sll


@pytest.fixture
def random_str_sll():
    sll = SinglyLinkedList('TEST Example String SLL', str)
    for _ in range(random.randint(1, 16)):
        random_string = ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(random.randint(1, 5)))
        sll.append(random_string)
    return sll


@pytest.fixture
def random_float_sll():
    sll = SinglyLinkedList('TEST Example Float SLL', float)
    for _ in range(random.randint(1, 16)):
        sll.append(random.random() * random.randint(-1000, 1000))
    return sll


@pytest.fixture
def save_path():
    return os.path.join(PROJECT_ROOT, os.pardir, 'images')


def test_render_int_sll(random_int_sll, save_path):
    random_int_sll.render(save_path)


def test_render_str_sll(random_str_sll, save_path):
    random_str_sll.render(save_path)


def test_render_float_sll(random_float_sll, save_path):
    random_float_sll.render(save_path)
