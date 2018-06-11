'''Doubly linked list data structure.'''


from dsviz.bases import DataStructure
from dsviz.decorators import validate_types
from dsviz.drawers import DLLDrawer
from dsviz.iterators import LLIter
from dsviz.nodes import DLLNode

import dsviz.util.file_utils as util


class DoublyLinkedList(DataStructure):
    '''The doubly linked list data structure.'''

    @validate_types(allowed_types={bool, int, float, str})
    def __init__(self, name, data_type, max_size=16):
        '''Constructor for a doubly linked list.

        Args:
            name: An identifier for the linked list.
            data_type: The type of data that the linked list will store.
            max_size: An optional argument to determine an upper limit for
                the size of the linked list.
        '''
        super().__init__(name, data_type, min(max_size, 16))

        self.head = None
        self.size = 0

    def get_head(self):
        '''Getter method for the head of the linked list.'''
        return self.head

    def prepend(self, value):
        '''Prepends an item to the start of the linked list.

        Args:
            value: The value of the item to be prepended to the linked list.

        Raises:
            TypeError: If the type of the item being prepended is not supported
                by the linked list.
            IndexError: If the max size limit has been reached.
        '''
        if type(value) != self.data_type:
            raise TypeError('The item being prepended is of invalid type.')
        if len(self) == self.max_size:
            raise IndexError('The max size limit of the linked list has been reached.')

        if self.get_head() == None:
            self.head = DLLNode(value)
            self.size += 1
            return None

        new_node = DLLNode(value)
        self.head.set_prev(new_node)
        new_node.set_next(self.head)
        self.head = new_node

        self.size += 1

    def append(self, value):
        '''Appends an item to the end of the linked list.

        Args:
            value: The value of the item to be appended to the linked list.

        Raises:
            TypeError: If the type of the item being appended is not supported
                by the linked list.
            IndexError: If the max size limit has been reached.
        '''
        if type(value) != self.data_type:
            raise TypeError('The item being appended is of invalid type.')
        if len(self) == self.max_size:
            raise IndexError('The max size limit of the linked list has been reached.')

        if self.get_head() == None:
            self.head = DLLNode(value)
            self.size += 1
            return None

        new_node = DLLNode(value)
        curr = self.get_head()
        while curr.get_next() != None:
            curr = curr.get_next()
        curr.set_next(new_node)
        new_node.set_prev(curr)

        self.size += 1

    def insert(self, position, value):
        '''Inserts an item to the linked list at a given position.

        Args:
            position: The index where the item is to be inserted.
            value: The value of the item to be inserted to the linked list.

        Raises:
            TypeError: If the type of the item being inserted is not supported
                by the linked list.
            IndexError: If the max size limit has been reached or the given
                position is out of bounds.
        '''
        if type(value) != self.data_type:
            raise TypeError('The item being inserted is of invalid type.')
        if len(self) == self.max_size:
            raise IndexError('The max size limit of the linked list has been reached.')
        if position < 0 or position >= self.size:
            raise IndexError('Index is out of bounds.')

        if position == 0:
            self.prepend(value)
            return None

        curr = self.get_head()
        for _ in range(position - 1):
            curr = curr.get_next()

        new_node = DLLNode(value)
        new_node.set_next(curr.get_next())
        curr.set_next(new_node)
        new_node.set_prev(curr)
        if new_node.get_next() != None:
            new_node.get_next().set_prev(new_node)

        self.size += 1

    def delete(self, value):
        '''Deletes an item from the linked list with the given value.

        Args:
            value: The value of the item(s) to be deleted from the linked list.

        Raises:
            TypeError: If the type of the item being deleted is not supported
                by the linked list.
        '''
        print('deleting:', value)
        if type(value) != self.data_type:
            raise TypeError('The item being deleted is of invalid type.')

        if self.get_head() == None:
            return None

        curr = self.get_head()
        deleted_node = False

        ## If the head is to be deleted
        if curr.get_data() == value:
            deleted_node = True
            if not curr.get_next():
                self.head = None
            else:
                curr.get_next().set_prev(None)
                self.head = curr.get_next()
                curr.set_next(None)
        else:
            while curr.get_next() != None:
                ## If the node being deleted is in the middle of the list
                if curr.get_data() == value:
                    deleted_node = True
                    curr.get_prev().set_next(curr.get_next())
                    curr.get_next().set_prev(curr.get_prev())
                    curr.set_next(None)
                    curr.set_prev(None)
                    deleted_node = True
                    break
                curr = curr.get_next()
            ## If the node being deleted is at the end of the list
            if not deleted_node and curr.get_data() == value:
                deleted_node = True
                curr.get_prev().set_next(None)
                curr.set_prev(None)

        self.size -= 1 if deleted_node else 0


    def search(self, value):
        '''Searches for an item in the linked list with the given value.

        Returns:
            The index where the first occurence of an item with the given value.
                If no item with given value exists, it returns -1.

        Raises:
            TypeError: If the type of the item being searched is not supported
                by the linked list.
        '''
        if type(value) != self.data_type:
            raise TypeError('The item being searched is of invalid type.')

        position = 0
        curr = self.head
        for val in self:
            if value == val:
                return position
            position += 1

        return -1

    def render(self, path=''):
        '''Renders the current state of the linked list.

        Args:
            path: The path where the rendered image will be saved.
        '''
        image = DLLDrawer.draw(self)
        if path:
            util.save_file(image, path, self.name)

    def is_empty(self):
        '''Returns true if the linked list is empty.'''
        return len(self) == 0

    def __len__(self):
        '''Returns the size of the linked list.'''
        return self.size

    def __iter__(self):
        '''Returns an iterator for the linked list.'''
        return LLIter(self)
