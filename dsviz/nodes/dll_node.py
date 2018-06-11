'''Node used for the doubly linked lists.'''


class DLLNode(object):
    '''Doubly linked list node.'''

    def __init__(self, data=None, _next=None, prev=None):
        '''Constructor for a doubly linked list node.

        Args:
            data: Data to be stored in the node.
            _next: The next node in the list.
            prev: The previous node in the list.
        '''
        self.data = data
        self._next = _next
        self.prev = prev

    def set_data(self, data):
        '''Setter for the node's data.'''
        self.data = data

    def set_next(self, _next):
        '''Setter for the node's next node.'''
        self._next = _next

    def set_prev(self, prev):
        '''Setter for the node's previous node.'''
        self.prev = prev

    def get_data(self):
        '''Getter for the node's data.'''
        return self.data

    def get_next(self):
        '''Getter for the node's next node.'''
        return self._next

    def get_prev(self):
        '''Getter for the node's previous node.'''
        return self.prev

    def __str__(self):
        '''Returns a string representing the node's data.'''
        return str(self.data)
