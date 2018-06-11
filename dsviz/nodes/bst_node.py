'''Node used for binary search trees.'''


class BSTNode(object):
    '''Binary search tree node.'''

    def __init__(self, data=None, left=None, right=None, parent=None, height=1):
        '''Constructor for a binary search tree node.

        Args:
            data: Data to be stored in the node.
            left: The left child of the node.
            right: The right child of the node.
        '''
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height

    def set_data(self, data):
        '''Setter for the node's data.'''
        self.data = data

    def set_left(self, left):
        '''Setter for the node's left child.'''
        self.left = left

    def set_right(self, right):
        '''Setter for the node's right child.'''
        self.right = right

    def set_parent(self, parent):
        '''Setter for the node's parent.'''
        self.parent = parent

    def set_height(self, height):
        '''Setter for the node's height.'''
        self.height = height

    def get_data(self):
        '''Getter for the node's data.'''
        return self.data

    def get_left(self):
        '''Getter for the node's left child.'''
        return self.left

    def get_right(self):
        '''Getter for the node's right child.'''
        return self.right

    def get_parent(self):
        '''Getter for the node's parent.'''
        return self.parent

    def get_height(self):
        '''Getter for the node's height.'''
        return self.height

    def __str__(self):
        '''Returns a string representing the node's data.'''
        return str(self.data)
