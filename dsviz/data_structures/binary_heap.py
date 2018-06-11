'''Binary heap data structure.'''


from dsviz.bases import DataStructure
from dsviz.decorators import validate_types
from dsviz.drawers import HeapDrawer
from dsviz.iterators import HeapIter

import dsviz.util.file_utils as util

import heapq


class BinaryHeap(DataStructure):
    '''Binary heap data structure.'''

    class MaxHeapComparable(object):
        '''Comparable object for max heap implementation.'''

        def __init__(self, value):
            self.value = value

        def __lt__(self, other):
            return self.value > other.value

        def __eq__(self, other):
            return self.value == other.value


    @validate_types(allowed_types={int, float, str})
    def __init__(self, name, data_type, max_size=32, min_heap=True):
        '''Constructor for a binary heap.

        Args:
            name: An identifier for the heap.
            data_type: The type of data that the heap will store.
            max_size: The upper limit for the size of the heap.
            min_heap: A boolean that if true will store min values.
        '''
        super().__init__(name, data_type, min(max_size, 32))

        self.heap = []
        self.min_heap = min_heap

    def insert(self, item):
        '''Inserts an item to the heap.

        Args:
            item: The item being inserted to the heap.

        Raises:
            TypeError: If the type of the item being inserted is not supported
                by the heap.
        '''
        if type(item) != self.data_type:
            raise TypeError('The item being inserted is of invalid type.')
        if len(self) == self.max_size:
            raise IndexError('The max size limit of the heap has been reached.')

        if self.min_heap:
            heapq.heappush(self.heap, item)
        else:
            heapq.heappush(self.heap, self.MaxHeapComparable(item))

    def extract(self):
        '''Extracts an item at the top of the heap.

        Returns:
            The item at the top of the heap.

        Raises:
            IndexError: If the heap is has no values.
        '''
        if self.is_empty():
            raise IndexError('The heap has no values.')

        if self.min_heap:
            return heapq.heappop(self.heap)
        else:
            return heapq.heappop(self.heap).value

    def peek(self):
        '''Examines the item at the top of the heap.

        Returns:
            The item at the top of the heap.

        Raises:
            IndexError: If the heap has no values.
        '''
        if self.is_empty():
            raise IndexError('The heap has no values.')

        if self.min_heap:
            return self.heap[0]
        return self.heap[0].value

    def render(self, path=''):
        '''Renders the current state of the heap.

        Args:
            path: The path where the rendered image will be saved.
        '''
        image = HeapDrawer.draw(self)
        if path:
            util.save_file(image, path, self.name)
        return image

    def is_empty(self):
        '''Returns true if the heap is empty.'''
        return len(self) == 0

    def __len__(self):
        '''Returns the size of the heap.'''
        return len(self.heap)
