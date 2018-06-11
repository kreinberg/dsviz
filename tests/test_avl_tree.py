#!/usr/bin/env python


import pytest


from dsviz import AVLTree


## Fixtures

@pytest.fixture
def empty_int_avl_tree():
    return AVLTree('', int)


@pytest.fixture
def empty_str_avl_tree():
    return AVLTree('', str)


@pytest.fixture
def full_int_avl_tree():
    avl = AVLTree('', int, 6)
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    avl.insert(40)
    avl.insert(50)
    avl.insert(25)
    return avl


## Data structures tests

def test_constructor_with_default_size_limit():
    int_avl = AVLTree('my int avl', int)
    assert int_avl.max_size == 32


def test_constructor_with_custom_size_limit():
    str_avl = AVLTree('my str avl', str, 20)
    assert str_avl.max_size == 20


def test_constructor_with_excessive_size_limit():
    float_avl = AVLTree('my float avl', float, 40)
    assert float_avl.max_size == 32


def test_constructor_with_invalid_size_limit():
    with pytest.raises(IndexError):
        int_avl = AVLTree('my int avl', int, -1)


def test_constructor_with_invalid_type():
    with pytest.raises(TypeError):
        bool_avl = AVLTree('my bool avl', bool)


def test_insert(empty_str_avl_tree):
    empty_str_avl_tree.insert('a')
    empty_str_avl_tree.insert('b')
    empty_str_avl_tree.insert('c')
    assert len(empty_str_avl_tree) == 3
    assert empty_str_avl_tree.get_root().get_data() == 'b'
    assert empty_str_avl_tree.get_root().get_left().get_data() == 'a'
    assert empty_str_avl_tree.get_root().get_right().get_data() == 'c'


def test_insert_with_invalid_type(empty_int_avl_tree):
    with pytest.raises(TypeError):
        empty_int_avl_tree.insert(1.123)


def test_delete(full_int_avl_tree):
    assert len(full_int_avl_tree) == 6
    full_int_avl_tree.delete(120)
    assert len(full_int_avl_tree) == 6
    full_int_avl_tree.delete(40)
    full_int_avl_tree.delete(50)
    full_int_avl_tree.delete(10)
    assert len(full_int_avl_tree) == 3
    assert full_int_avl_tree.search(25)
    full_int_avl_tree.delete(25)
    assert len(full_int_avl_tree) == 2
    assert not full_int_avl_tree.search(40)
    assert not full_int_avl_tree.search(50)
    assert not full_int_avl_tree.search(10)
    assert not full_int_avl_tree.search(25)
    full_int_avl_tree.delete(30)
    assert full_int_avl_tree.get_root().get_data() == 20
    full_int_avl_tree.delete(20)
    assert full_int_avl_tree.is_empty()


def test_delete_with_invalid_type(full_int_avl_tree):
    with pytest.raises(TypeError):
        full_int_avl_tree.delete('abc')


def test_search(full_int_avl_tree):
    assert full_int_avl_tree.search(20)
    assert not full_int_avl_tree.search(77)


def test_search_with_invalid_type(full_int_avl_tree):
    with pytest.raises(TypeError):
        full_int_avl_tree.search(True)


def test_iter(full_int_avl_tree):
    values = []
    for node_value in full_int_avl_tree:
        values.append(node_value)
    assert values == sorted(values)


## Render tests

from dsviz import PROJECT_ROOT

import os
import random
import string


@pytest.fixture
def random_int_avl_tree():
    avl = AVLTree('TEST Example Integer AVL Tree', int)
    for _ in range(random.randint(1, 32)):
        avl.insert(random.randint(-999, 999))
    return avl


@pytest.fixture
def random_str_avl_tree():
    avl = AVLTree('TEST Example String AVL Tree', str)
    for _ in range(random.randint(1, 32)):
        random_string = ''.join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(random.randint(1, 5)))
        avl.insert(random_string)
    return avl


@pytest.fixture
def random_float_avl_tree():
    avl = AVLTree('TEST Example Float AVL Tree', float)
    for _ in range(random.randint(1, 32)):
        avl.insert(random.random() * random.randint(-999, 999))
    return avl


@pytest.fixture
def save_path():
    return os.path.join(PROJECT_ROOT, os.pardir, 'images')


def test_render_int_avl_tree(random_int_avl_tree, save_path):
    random_int_avl_tree.render(save_path)


def test_render_str_avl_tree(random_str_avl_tree, save_path):
    random_str_avl_tree.render(save_path)


def test_render_float_avl_tree(random_float_avl_tree, save_path):
    random_float_avl_tree.render(save_path)
