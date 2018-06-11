#!/usr/bin/env python


import pytest

from dsviz import ArrayStack


## Fixtures

@pytest.fixture
def empty_int_stack():
    return ArrayStack('', int)


@pytest.fixture
def empty_str_stack():
    return ArrayStack('', str)


@pytest.fixture
def full_int_stack():
    st = ArrayStack('', int, 4)
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    return st


## Data structure tests

def test_constructor_with_default_size_limit():
    int_stack = ArrayStack('my int stack', int)
    assert int_stack.max_size == 16


def test_constructor_with_custom_size_limit():
    str_stack = ArrayStack('my str stack', str, 8)
    assert str_stack.max_size == 8


def test_constructor_with_excessive_size_limit():
    bool_stack = ArrayStack('my bool stack', bool, 17)
    assert bool_stack.max_size == 16


def test_constructor_with_invalid_size_limit():
    with pytest.raises(IndexError):
        float_stack = ArrayStack('my float stack', float, -1)


def test_constructor_with_invalid_type():
    with pytest.raises(TypeError):
        list_stack = ArrayStack('my list stack', list)


def test_push(empty_int_stack):
    empty_int_stack.push(50)
    empty_int_stack.push(40)
    empty_int_stack.push(-70)
    assert len(empty_int_stack) == 3


def test_push_with_invalid_type(empty_str_stack):
    with pytest.raises(TypeError):
        empty_str_stack.push(20)


def test_push_with_full_stack(full_int_stack):
    with pytest.raises(IndexError):
        full_int_stack.push(1)


def test_pop(full_int_stack):
    assert len(full_int_stack) == 4
    val1 = full_int_stack.pop()
    val2 = full_int_stack.pop()
    val3 = full_int_stack.pop()
    val4 = full_int_stack.pop()
    assert full_int_stack.is_empty()
    assert val1 == 4
    assert val2 == 3
    assert val3 == 2
    assert val4 == 1


def test_pop_with_empty_stack(empty_int_stack):
    with pytest.raises(IndexError):
        empty_int_stack.pop()


def test_peek(full_int_stack):
    val1 = full_int_stack.peek()
    val2 = full_int_stack.peek()
    assert val1 == val2 == 4
    assert len(full_int_stack) == 4


def test_peek_with_empty_stack(empty_int_stack):
    with pytest.raises(IndexError):
        empty_int_stack.peek()


## Render tests

from dsviz import PROJECT_ROOT

import os
import random
import string


@pytest.fixture
def random_int_stack():
    st = ArrayStack('TEST Example Integer Stack', int)
    for _ in range(random.randint(1, 16)):
        st.push(random.randint(-10000000000000, 100000000000))
    return st


@pytest.fixture
def random_str_stack():
    st = ArrayStack('TEST Example String Stack', str)
    for _ in range(random.randint(1, 16)):
        random_string = ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(random.randint(1, 20)))
        st.push(random_string)
    return st


@pytest.fixture
def random_float_stack():
    st = ArrayStack('TEST Example Float Stack', float)
    for _ in range(random.randint(1, 16)):
        st.push(random.random() * random.randint(-10000000, 10000000))
    return st


@pytest.fixture
def save_path():
    return os.path.join(PROJECT_ROOT, os.pardir, 'images')


def test_render_int_stack(random_int_stack, save_path):
    random_int_stack.render(save_path)


def test_render_str_stack(random_str_stack, save_path):
    random_str_stack.render(save_path)


def test_render_float_stack(random_float_stack, save_path):
    random_float_stack.render(save_path)
