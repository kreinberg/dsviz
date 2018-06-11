'''Iterator class for linked lists.'''


class LLIter(object):
    '''An iterator for linked list data structures.'''

    def __init__(self, iterable):
        '''Constructor for a linked list iterator.

        Args:
            iterable: The linked list to be iterated.
        '''
        self._iterable = iterable
        self._iterator = self._get_iter(iterable)

    @staticmethod
    def _get_iter(iterable):
        '''A generator that yields elements of the linked list.

        Args:
            iterable: The linked list to be iterated.
        '''
        curr = iterable.get_head()
        while curr:
            data = curr.get_data()
            curr = curr.get_next()
            yield data

    def __iter__(self):
        '''iter method overloader.'''
        return self

    def __next__(self):
        '''next method overloader.'''
        return next(self._iterator)
