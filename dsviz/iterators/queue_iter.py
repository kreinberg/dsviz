'''Iterator class for queue data structures.'''


class QueueIter(object):
    '''An iterator for all queue data structure.'''

    def __init__(self, iterable):
        '''Constructor for a queue iterator.

        Args:
            iterable: The queue to be iterated.
        '''
        self._iterable = iterable
        self._iterator = self._get_iter(iterable)

    @staticmethod
    def _get_iter(iterable):
        '''A generator that yields elements of the queue from front to back.

        Args:
            iterable: The queue to be iterated.
        '''
        for value in iterable.queue:
            yield value

    def __iter__(self):
        '''iter method overloader.'''
        return self

    def __next__(self):
        '''next method overloader.'''
        return next(self._iterator)
