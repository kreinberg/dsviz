'''Iterator class for the binary heap data structure.'''


class HeapIter(object):
    '''An iterator for the binary heap data structure.'''

    def __init__(self, iterable):
        '''Constructor for a queue iterator.

        Args:
            itera
        '''
        self._iterable = iterable
        self._iterator = self._get_iter(iterable)

    @staticmethod
    def _get_iter(iterable):
        '''A generator that yields elements of the heap.

        Args:
            iterable: The heap to be iterated.
        '''
        for value in iterable.heap:
            yield value

    def __iter__(self):
        '''iter method overloader.'''
        return self

    def __next__(self):
        '''next method overloader.'''
        return next(self._iterator)
