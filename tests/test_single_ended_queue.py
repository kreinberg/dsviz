#!/usr/bin/env python


import pytest

from dsviz import SingleEndedQueue


## Fixtures

@pytest.fixture
def empty_int_queue():
    return SingleEndedQueue('', int)


@pytest.fixture
def empty_str_queue():
    return SingleEndedQueue('', str)


@pytest.fixture
def full_int_queue():
    q = SingleEndedQueue('', int, 4)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    return q


## Data structure tests

def test_constructor_with_default_size_limit():
    int_queue = SingleEndedQueue('my int queue', int)
    assert int_queue.max_size == 16


def test_constructor_with_custom_size_limit():
    str_queue = SingleEndedQueue('my str queue', str, 4)
    assert str_queue.max_size == 4


def test_constructor_with_excessive_size_limit():
    bool_queue = SingleEndedQueue('my bool queue', bool, 18)
    assert bool_queue.max_size == 16


def test_constructor_with_invalid_size_limit():
    with pytest.raises(IndexError):
        float_queue = SingleEndedQueue('my float queue', float, -1)


def test_constructor_with_invalid_type():
    with pytest.raises(TypeError):
        list_queue = SingleEndedQueue('my list queue', list)


def test_enqueue(empty_int_queue):
    empty_int_queue.enqueue(5)
    empty_int_queue.enqueue(50)
    empty_int_queue.enqueue(-500)
    assert len(empty_int_queue) == 3


def test_enqueue_with_invalid_type(empty_str_queue):
    with pytest.raises(TypeError):
        empty_str_queue.enqueue(5)


def test_enqueue_with_full_queue(full_int_queue):
    with pytest.raises(IndexError):
        full_int_queue.enqueue(3)


def test_dequeue(full_int_queue):
    assert len(full_int_queue) == 4
    val1 = full_int_queue.dequeue()
    val2 = full_int_queue.dequeue()
    val3 = full_int_queue.dequeue()
    val4 = full_int_queue.dequeue()
    assert full_int_queue.is_empty()
    assert val1 == 1
    assert val2 == 2
    assert val3 == 3
    assert val4 == 4


def test_dequeue_with_empty_queue(empty_int_queue):
    with pytest.raises(IndexError):
        empty_int_queue.dequeue()


def test_peek(full_int_queue):
    val1 = full_int_queue.peek()
    val2 = full_int_queue.peek()
    assert val1 == val2 == 1
    assert len(full_int_queue) == 4


def test_peek_with_empty_queue(empty_int_queue):
    with pytest.raises(IndexError):
        empty_int_queue.peek()


## Render tests

from dsviz import PROJECT_ROOT

import os
import random
import string


@pytest.fixture
def random_int_queue():
    q = SingleEndedQueue('TEST Example Integer Queue', int)
    for _ in range(random.randint(1, 16)):
        q.enqueue(random.randint(-100000, 100000))
    return q


@pytest.fixture
def random_str_queue():
    q = SingleEndedQueue('TEST Example String Queue', str)
    for _ in range(random.randint(1, 16)):
        random_string = ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(random.randint(1, 20)))
        q.enqueue(random_string)
    return q


@pytest.fixture
def random_float_queue():
    q = SingleEndedQueue('TEST Example Float Queue', float)
    for _ in range(random.randint(1, 16)):
        q.enqueue(random.random() * random.randint(-100000, 100000))
    return q


@pytest.fixture
def save_path():
    return os.path.join(PROJECT_ROOT, os.pardir, 'images')


def test_render_int_queue(random_int_queue, save_path):
    random_int_queue.render(save_path)


def test_render_str_queue(random_str_queue, save_path):
    random_str_queue.render(save_path)


def test_render_float_queue(random_float_queue, save_path):
    random_float_queue.render(save_path)
