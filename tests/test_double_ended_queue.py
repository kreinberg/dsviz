#!/usr/bin/env python


import pytest

from dsviz import DoubleEndedQueue


## Fixtures

@pytest.fixture
def empty_int_deque():
    return DoubleEndedQueue('', int)


@pytest.fixture
def empty_str_deque():
    return DoubleEndedQueue('', str)


@pytest.fixture
def full_int_deque():
    dq = DoubleEndedQueue('', int, 4)
    dq.enqueue_front(1)
    dq.enqueue_front(2)
    dq.enqueue_front(3)
    dq.enqueue_front(4)
    return dq


## Data structure tests


def test_constructor_with_default_size_limit():
    int_deque = DoubleEndedQueue('my int deque', int)
    assert int_deque.max_size == 16


def test_constructor_with_custom_size_limit():
    str_deque = DoubleEndedQueue('my str deque', str, 4)
    assert str_deque.max_size == 4


def test_constructor_with_excessive_size_limit():
    bool_deque = DoubleEndedQueue('my bool deque', bool, 18)
    assert bool_deque.max_size == 16


def test_constructor_with_invalid_size_limit():
    with pytest.raises(IndexError):
        float_deque = DoubleEndedQueue('my float deque', float, -1)


def test_constructor_with_invalid_type():
    with pytest.raises(TypeError):
        list_deque = DoubleEndedQueue('my list deque', list)


def test_enqueue_front(empty_int_deque):
    empty_int_deque.enqueue_front(3)
    empty_int_deque.enqueue_front(-3)
    empty_int_deque.enqueue_front(-4)
    assert len(empty_int_deque) == 3
    assert empty_int_deque.peek_front() == -4
    assert empty_int_deque.peek_back() == 3


def test_enqueue_front_with_invalid_type(empty_str_deque):
    with pytest.raises(TypeError):
        empty_str_deque.enqueue_front(True)


def test_enqueue_front_with_full_deque(full_int_deque):
    with pytest.raises(IndexError):
        full_int_deque.enqueue_front(5)


def test_enqueue_back(empty_str_deque):
    empty_str_deque.enqueue_back('a')
    empty_str_deque.enqueue_back('aaaa')
    empty_str_deque.enqueue_back('123')
    assert len(empty_str_deque) == 3
    assert empty_str_deque.peek_back() == '123'
    assert empty_str_deque.peek_front() == 'a'


def test_enqueue_back_with_invalid_type(empty_str_deque):
    with pytest.raises(TypeError):
        empty_str_deque.enqueue_back([])


def test_enqueue_back_with_full_deque(full_int_deque):
    with pytest.raises(IndexError):
        full_int_deque.enqueue_back(5)


def test_dequeue_front(full_int_deque):
    assert len(full_int_deque) == 4
    val1 = full_int_deque.dequeue_front()
    val2 = full_int_deque.dequeue_front()
    val3 = full_int_deque.dequeue_front()
    val4 = full_int_deque.dequeue_front()
    assert full_int_deque.is_empty()
    assert val1 == 4
    assert val2 == 3
    assert val3 == 2
    assert val4 == 1


def test_dequeue_front_with_empty_deque(empty_str_deque):
    with pytest.raises(IndexError):
        empty_str_deque.dequeue_front()


def test_dequeue_back(full_int_deque):
    assert len(full_int_deque) == 4
    val1 = full_int_deque.dequeue_back()
    val2 = full_int_deque.dequeue_back()
    val3 = full_int_deque.dequeue_back()
    val4 = full_int_deque.dequeue_back()
    assert full_int_deque.is_empty()
    assert val1 == 1
    assert val2 == 2
    assert val3 == 3
    assert val4 == 4


def test_dequeue_back_with_empty_deque(empty_int_deque):
    with pytest.raises(IndexError):
        empty_int_deque.dequeue_back()


def test_peek_front(full_int_deque):
    val1 = full_int_deque.peek_front()
    val2 = full_int_deque.peek_front()
    assert val1 == val2 == 4
    assert len(full_int_deque) == 4


def test_peek_front_with_empty_deque(empty_int_deque):
    with pytest.raises(IndexError):
        empty_int_deque.peek_front()


def test_peek_back(full_int_deque):
    val1 = full_int_deque.peek_back()
    val2 = full_int_deque.peek_back()
    assert val1 == val2 == 1
    assert len(full_int_deque) == 4


def test_peek_back_with_empty_deque(empty_int_deque):
    with pytest.raises(IndexError):
        empty_int_deque.peek_back()


## Render tests

from dsviz import PROJECT_ROOT

import os
import random
import string


@pytest.fixture
def random_int_deque():
    dq = DoubleEndedQueue('TEST Example Integer Deque', int)
    for _ in range(random.randint(1, 16)):
        dq.enqueue_front(random.randint(-10000, 10000))
    return dq


@pytest.fixture
def random_str_deque():
    dq = DoubleEndedQueue('TEST Example String Deque', str)
    for _ in range(random.randint(1, 16)):
        random_string = ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(random.randint(1, 20)))
        dq.enqueue_front(random_string)
    return dq


@pytest.fixture
def random_float_deque():
    dq = DoubleEndedQueue('TEST Example Float Deque', float)
    for _ in range(random.randint(1, 16)):
        dq.enqueue_front(random.random() * random.randint(-100000, 100000))
    return dq


@pytest.fixture
def save_path():
    return os.path.join(PROJECT_ROOT, os.pardir, 'images')


def test_render_int_deque(random_int_deque, save_path):
    random_int_deque.render(save_path)


def test_render_str_deque(random_str_deque, save_path):
    random_str_deque.render(save_path)


def test_render_float_deque(random_float_deque, save_path):
    random_float_deque.render(save_path)
