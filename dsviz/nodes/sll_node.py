'''Node used for singly linked lists.'''


class SLLNode(object):
    '''Singly linked list node.'''

    def __init__(self, data=None, _next=None):
        '''Constructor for a singly linked list node.

        Args:
            data: Data to be stored in the node.
            _next: The next node in the list.
        '''
        self.data = data
        self._next = _next

    def set_data(self, data):
        '''Setter for the node's data.'''
        self.data = data

    def set_next(self, _next):
        '''Setter for the node's next node.'''
        self._next = _next

    def get_data(self):
        '''Getter for the node's data.'''
        return self.data

    def get_next(self):
        '''Getter for the node's next node.'''
        return self._next

    def __str__(self):
        '''Returns a string representing the node's data.'''
        return str(self.data)
