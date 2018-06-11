'''Binary search tree data structure.'''


from dsviz.bases import DataStructure
from dsviz.decorators import validate_types
from dsviz.drawers import BSTDrawer
from dsviz.iterators import TreeIter
from dsviz.nodes import BSTNode

import dsviz.util.file_utils as util


class BinarySearchTree(DataStructure):
    '''The binary search tree data structure.'''

    @validate_types(allowed_types={int, float, str})
    def __init__(self, name, data_type, max_size=32):
        '''Constructor for a binary search tree.

        Args:
            name: An identifier for the tree.
            data_type: The type of data that the tree will store.
        '''
        super().__init__(name, data_type, min(max_size, 32))

        self.root = None
        self.size = 0

    def get_root(self):
        '''Getter method for the root of the tree.'''
        return self.root

    def _insert(self, node, value):
        '''Helper method for insert operation.'''
        if node == None:
            self.size += 1
            return BSTNode(value)
        elif value < node.get_data():
            node.set_left(self._insert(node.get_left(), value))
        else:
            node.set_right(self._insert(node.get_right(), value))

        return node

    def insert(self, value):
        '''Inserts an item to the tree.

        Args:
            value: The value of the item to be inserted to the tree.

        Raises:
            TypeError: If the type of the item being inserted is not supported
                by the tree.
            IndexError: If the max size limit has been reached.
        '''
        if type(value) != self.data_type:
            raise TypeError('The item being inserted is of invalid type.')
        if len(self) == self.max_size:
            raise IndexError('The max size limit of the linked list has been reached.')

        self.root = self._insert(self.get_root(), value)

    def _min_value_node(self, node):
        '''Helper method that returns the minimum value node in a given subtree.'''
        curr = node
        while curr.get_left() != None:
            curr = curr.get_left()

        return curr

    def _delete(self, node, value):
        '''Helper method for delete operation.'''
        if node == None:
            return node
        elif value < node.get_data():
            node.set_left(self._delete(node.get_left(), value))
        elif value > node.get_data():
            node.set_right(self._delete(node.get_right(), value))
        else:
            if node.get_left() == None:
                temp = node.get_right()
                node = None
                return temp
            elif node.get_right() == None:
                temp = node.get_left()
                node = None
                return temp
            temp = self._min_value_node(node.get_right())
            node.set_data(temp.get_data())
            node.set_right(self._delete(node.get_right(), temp.get_data()))

        return node

    def delete(self, value):
        '''Deletes an item from the tree with the given value.

        Args:
            value: The value of the item to be deleted from the tree.

        Raises:
            TypeError: If the type of the item being deleted is not supported
                by the tree.
        '''
        if type(value) != self.data_type:
            raise TypeError('The item being deleted is of invalid type.')

        if self.search(value):
            self.size -= 1
        self.root = self._delete(self.get_root(), value)

    def _search(self, node, value):
        '''Helper method for search operation.'''
        if node == None:
            return False
        if node.get_data() == value:
            return True

        if node.get_data() < value:
            return self._search(node.get_right(), value)
        return self._search(node.get_left(), value)

    def search(self, value):
        '''Searches for an item in the tree.

        Args:
            value: The value of the item being searched for in the tree.

        Returns:
            A boolean representing whether or not the value was found in the
                tree.

        Raises:
            TypeError: If the type of the item being searched is not supported
                by the tree.
        '''
        if type(value) != self.data_type:
            raise TypeError('The item being searched is of invalid type.')

        return self._search(self.get_root(), value)

    def render(self, path=''):
        '''Renders the current state of the tree.

        Args:
            path: The path where the rendered image will be saved.
        '''
        image = BSTDrawer.draw(self)
        if path:
            util.save_file(image, path, self.name)
        return image

    def is_empty(self):
        '''Returns true if the tree is empty.'''
        return len(self) == 0

    def __len__(self):
        '''Returns the size of the tree.'''
        return self.size

    def __iter__(self):
        '''Returns an iterator for the tree.'''
        return TreeIter(self)
