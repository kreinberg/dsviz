'''Iterator class for the array stack.'''


class StackIter(object):
    '''An iterator for the array stack data structure.'''

    def __init__(self, iterable):
        '''Constructor for a stack iterator.

        Args:
            iterable: The stack to be iterated.
        '''
        self._iterable = iterable
        self._iterator = self._get_iter(iterable)

    @staticmethod
    def _get_iter(iterable):
        '''A generator that yields elements of the array stack from top to
            bottom.

        Args:
            iterable: The stack to be iterated.
        '''
        for value in iterable.stack[::-1]:
            yield value

    def __iter__(self):
        '''iter method overloader.'''
        return self

    def __next__(self):
        '''next method overloader.'''
        return next(self._iterator)
