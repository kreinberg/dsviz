'''Double ended queue data structure.'''


from dsviz.bases import DataStructure
from dsviz.decorators import validate_types
from dsviz.drawers import DequeDrawer
from dsviz.iterators import QueueIter

import dsviz.util.file_utils as util


class DoubleEndedQueue(DataStructure):
    '''The double ended queue data structure.'''

    @validate_types(allowed_types={bool, int, float, str})
    def __init__(self, name, data_type, max_size=16):
        '''Constructor for a double ended queue.

        Args:
            name: An identifier for the queue.
            data_type: The type of data that the queue will store.
            max_size: An optional argument to determine an upper limit for the
                size of the queue.
        '''
        super().__init__(name, data_type, min(max_size, 16))

        self.queue = []

    def enqueue_front(self, item):
        '''Enqueues an item to the front of the queue.

        Args:
            item: The item to be enqueued to the front of the queue.

        Raises:
            TypeError: If the type of the item being enqueued is not supported
                by the queue.
            IndexError: If the max size limit has been reached.
        '''
        if type(item) != self.data_type:
            raise TypeError('The item being enqueued is of invalid type.')
        if len(self) == self.max_size:
            raise IndexError('The max size limit of the queue has been reached.')

        self.queue.insert(0, item)

    def enqueue_back(self, item):
        '''Enqueues an item to the back of the queue.

        Args:
            item: The item to be enqueued to the back of the queue.

        Raises:
            TypeError: If the type of the item being enqueued is not supported
                by the queue.
            IndexError: If the max size limit has been reached.
        '''
        if type(item) != self.data_type:
            raise TypeError('The item being enqueued is of invalid type.')
        if len(self) == self.max_size:
            raise IndexError('The max size limit of the queue has been reached.')

        self.queue.append(item)

    def dequeue_front(self):
        '''Dequeues an item from the front of the queue.

        Returns:
            The item in the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        '''
        if self.is_empty():
            raise IndexError('The queue is empty.')

        return self.queue.pop(0)

    def dequeue_back(self):
        '''Dequeues an item from the back of the queue.

        Returns:
            The item in the back of the queue.

        Raises:
            IndexError: If the queue is empty.
        '''
        if self.is_empty():
            raise IndexError('The queue is empty.')

        return self.queue.pop()

    def peek_front(self):
        '''Examines the item in the front of the queue without removing it.

        Returns:
            The item in the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        '''
        if self.is_empty():
            raise IndexError('The queue is empty.')

        return self.queue[0]

    def peek_back(self):
        '''Examines the item in the back of the queue without removing it.

        Returns:
            The item in the back of the queue.

        Raises:
            IndexError: If the queue is empty.
        '''
        if self.is_empty():
            raise IndexError('The queue is empty.')

        return self.queue[-1]

    def render(self, path=''):
        '''Renders the current state of the queue.

        Args:
            path: The path where the rendered image will be saved.
        '''
        image = DequeDrawer.draw(self)
        if path:
            util.save_file(image, path, self.name)
        image

    def is_empty(self):
        '''Returns true if the queue is empty.'''
        return len(self) == 0

    def __len__(self):
        '''Returns the size of the queue.'''
        return len(self.queue)

    def __iter__(self):
        '''Returns an iterator for the deque.'''
        return QueueIter(self)
