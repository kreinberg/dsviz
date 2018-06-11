'''Array stack data structure.'''


from dsviz.bases import DataStructure
from dsviz.decorators import validate_types
from dsviz.drawers import StackDrawer
from dsviz.iterators import StackIter

import dsviz.util.file_utils as util


class ArrayStack(DataStructure):
    '''The stack data structure. The stack uses a Python list as a container.'''

    @validate_types(allowed_types={bool, int, float, str})
    def __init__(self, name, data_type, max_size=16):
        '''Constructor for a stack.

        Args:
            name: An identifier for the stack.
            data_type: The type of data that the stack will store.
            max_size: An optional argument to determine an upper limit for the
                size of the stack.
        '''
        super().__init__(name, data_type, min(max_size, 16))

        self.stack = []

    def push(self, item):
        '''Pushes an item to the stack.

        Args:
            item: The item to be pushed to the stack.

        Raises:
            TypeError: If the type of the item being pushed is not supported by
                the stack.
            IndexError: If the max size limit has been reached.
        '''
        if type(item) != self.data_type:
            raise TypeError('The item being pushed is of invalid type.')
        if len(self) == self.max_size:
            raise IndexError('The max size limit of the queue has been reached.')

        self.stack.append(item)

    def pop(self):
        '''Pops an item from the top of the stack.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        '''
        if self.is_empty():
            raise IndexError('The stack is empty.')

        return self.stack.pop()

    def peek(self):
        '''Examines the item at the top of the stack without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        '''
        if self.is_empty():
            raise IndexError('The stack is empty.')

        return self.stack[-1]

    def render(self, path=''):
        '''Renders the current state of the stack.

        Args:
            path: The path where the rendered image will be saved.
        '''
        image = StackDrawer.draw(self)
        if path:
            util.save_file(image, path, self.name)
        return image

    def is_empty(self):
        '''Returns true if the stack is empty.'''
        return len(self) == 0

    def __len__(self):
        '''Returns the size of the stack.'''
        return len(self.stack)

    def __iter__(self):
        '''Returns an iterator for the stack.'''
        return StackIter(self)
