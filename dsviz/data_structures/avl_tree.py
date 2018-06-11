'''AVL tree data structure.'''


from dsviz.bases import DataStructure
from dsviz.decorators import validate_types
from dsviz.drawers import AVLTreeDrawer
from dsviz.iterators import TreeIter
from dsviz.nodes import BSTNode

import dsviz.util.file_utils as util


class AVLTree(DataStructure):
    '''The AVL tree data structure.'''

    @validate_types(allowed_types={int, float, str})
    def __init__(self, name, data_type, max_size=32):
        '''Constructor for an AVL tree.

        Args:
            name: An identifier for the tree.
            data_type: The type of data that the tree will store.
            max_size: The upper limit for the size of the tree.
        '''
        super().__init__(name, data_type, min(max_size, 32))

        self.root = None
        self.size = 0

    def get_root(self):
        '''Getter method for the root of the tree.'''
        return self.root

    def _rotate_left(self, z):
        '''Helper method for rotating a subtree left.'''
        y = z.get_right()
        t2 = y.get_left()

        ## Rotate left
        y.set_left(z)
        z.set_right(t2)

        ## Update heights
        z.set_height(
            1 + max(self._get_height(z.get_left()),
                self._get_height(z.get_right()))
        )
        y.set_height(
            1 + max(self._get_height(y.get_left()),
                self._get_height(y.get_right()))
        )

        return y

    def _rotate_right(self, z):
        '''Helper method for rotating a subtree right.'''
        y = z.get_left()
        t3 = y.get_right()

        ## Rotate right
        y.set_right(z)
        z.set_left(t3)

        ## Update heights
        z.set_height(
            1 + max(self._get_height(z.get_left()),
                self._get_height(z.get_right()))
        )
        y.set_height(
            1 + max(self._get_height(y.get_left()),
                self._get_height(y.get_right()))
        )

        return y

    def _get_height(self, node):
        '''Helper method for returning the height of a node.'''
        if node == None:
            return 0

        return node.get_height()

    def _get_balance(self, node):
        '''Helper method for returning the difference between two subtree heights.'''
        if node == None:
            return 0

        return self._get_height(node.get_left()) - self._get_height(node.get_right())

    def _insert(self, node, value):
        '''Helper method for insert operation.'''
        if node == None:
            self.size += 1
            return BSTNode(value)
        elif value < node.get_data():
            node.set_left(self._insert(node.get_left(), value))
        else:
            node.set_right(self._insert(node.get_right(), value))

        node.set_height(
            1 + max(self._get_height(node.get_left()),
                self._get_height(node.get_right()))
        )

        balance = self._get_balance(node)
        if balance > 1 and value < node.get_left().get_data():
            return self._rotate_right(node)
        if balance < -1 and value > node.get_right().get_data():
            return self._rotate_left(node)
        if balance > 1 and value > node.get_left().get_data():
            node.set_left(self._rotate_left(node.get_left()))
            return self._rotate_right(node)
        if balance < -1 and value < node.get_right().get_data():
            node.set_right(self._rotate_right(node.get_right()))
            return self._rotate_left(node)

        return node


    def insert(self, value):
        '''Inserts an item to the tree.

        Args:
            value: The value of the item to be inserted to the tree.

        Raises:
            TypeError: If the type of the item being inserted is not supported
                by the tree.
        '''
        if type(value) != self.data_type:
            raise TypeError('The item being inserted is of invalid type.')
        if len(self) == self.max_size:
            raise IndexError('The max size limit of the linked list has been reached.')

        self.root = self._insert(self.get_root(), value)

    def _min_value_node(self, node):
        '''Helper method that returns the minimum value node in a given subtree.'''
        curr = node
        while curr != None and curr.get_left() != None:
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
            self.size -= 1
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

        node.set_height(
            1 + max(self._get_height(node.get_left()),
                self._get_height(node.get_right()))
        )

        balance = self._get_balance(node)
        if balance > 1 and self._get_balance(node.get_left()) >= 0:
            return self._rotate_right(node)
        if balance < -1 and self._get_balance(node.get_right()) >= 0:
            return self._rotate_left(node)
        if balance > 1 and self._get_balance() < 0:
            node.set_left(self._rotate_left(node.get_left()))
            return self._rotate_right(node)
        if balance < -1 and self._get_balance() < 0:
            node.set_right(self._rotate_right(node.get_right()))
            return self._rotate_left(node)

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
        image = AVLTreeDrawer.draw(self)
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
