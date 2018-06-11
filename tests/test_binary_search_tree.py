#!/usr/bin/env python


import pytest


from dsviz import BinarySearchTree


## Fixtures

@pytest.fixture
def empty_int_bst():
    return BinarySearchTree('', int)


@pytest.fixture
def empty_str_bst():
    return BinarySearchTree('', str)


@pytest.fixture
def full_int_bst():
    bst = BinarySearchTree('', int, 8)
    bst.insert(50)
    bst.insert(20)
    bst.insert(30)
    bst.insert(40)
    bst.insert(80)
    bst.insert(10)
    bst.insert(70)
    bst.insert(100)
    return bst


## Data structures tests

def test_constructor_with_default_size_limit():
    int_bst = BinarySearchTree('my int bst', int)
    assert int_bst.max_size == 32


def test_constructor_with_custom_size_limit():
    str_bst = BinarySearchTree('my str bst', str, 18)
    assert str_bst.max_size == 18


def test_constructor_with_excessive_size_limit():
    float_bst = BinarySearchTree('my float bst', float, 35)
    assert float_bst.max_size == 32


def test_constructor_with_invalid_size_limit():
    with pytest.raises(IndexError):
        int_bst = BinarySearchTree('my int bst', int, -20)


def test_constructor_with_invalid_type():
    with pytest.raises(TypeError):
        bool_bst = BinarySearchTree('my bool bst', bool)


def test_insert(empty_int_bst):
    empty_int_bst.insert(30)
    empty_int_bst.insert(20)
    empty_int_bst.insert(40)
    assert len(empty_int_bst) == 3
    assert empty_int_bst.get_root().get_data() == 30
    assert empty_int_bst.get_root().get_left().get_data() == 20
    assert empty_int_bst.get_root().get_right().get_data() == 40


def test_insert_with_invalid_type(empty_str_bst):
    with pytest.raises(TypeError):
        empty_str_bst.insert(5.5)


def test_delete(full_int_bst):
    assert len(full_int_bst) == 8
    full_int_bst.delete(1000)
    assert len(full_int_bst) == 8
    full_int_bst.delete(50)
    assert len(full_int_bst) == 7
    full_int_bst.delete(20)
    assert len(full_int_bst) == 6
    full_int_bst.delete(100)
    full_int_bst.delete(80)
    full_int_bst.delete(30)
    full_int_bst.delete(40)
    full_int_bst.delete(70)
    assert full_int_bst.get_root().get_data() == 10
    full_int_bst.delete(10)
    assert full_int_bst.is_empty()


def test_delete_with_invalid_type(full_int_bst):
    with pytest.raises(TypeError):
        full_int_bst.delete('a')


def test_search(full_int_bst):
    assert full_int_bst.search(20)
    assert not full_int_bst.search(90)


def teste_search_with_invalid_type(full_int_bst):
    with pytest.raises(TypeError):
        full_int_bst.search('a')


def test_iter(full_int_bst):
    values = []
    for node_value in full_int_bst:
        values.append(node_value)
    assert values == sorted(values)


## Render tests

from dsviz import PROJECT_ROOT

import os
import random
import string


@pytest.fixture
def random_int_bst():
    bst = BinarySearchTree('TEST Example Integer BST', int)
    for _ in range(random.randint(1, 32)):
        bst.insert(random.randint(-999, 999))
    return bst


@pytest.fixture
def random_str_bst():
    bst = BinarySearchTree('TEST Example String BST', str)
    for _ in range(random.randint(1, 32)):
        random_string = ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(random.randint(1, 5)))
        bst.insert(random_string)
    return bst


@pytest.fixture
def random_float_bst():
    bst = BinarySearchTree('TEST Example Float BST', float)
    for _ in range(random.randint(1, 32)):
        bst.insert(random.random() * random.randint(-999, 999))
    return bst


@pytest.fixture
def save_path():
    return os.path.join(PROJECT_ROOT, os.pardir, 'images')


def test_render_int_bst(random_int_bst, save_path):
    random_int_bst.render(save_path)


def test_render_str_bst(random_str_bst, save_path):
    random_str_bst.render(save_path)


def test_render_float_bst(random_float_bst, save_path):
    random_float_bst.render(save_path)
