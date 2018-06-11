'''Iterator class for trees.'''


class TreeIter(object):
    '''An iterator for tree data structures.'''

    def __init__(self, iterable):
        '''Constructor for a tree iterator.

        Args:
            iterable: The tree to be iterated.
        '''
        self._iterable = iterable
        self._iterator = self._get_iter(iterable)

    @staticmethod
    def _get_iter(iterable):
        '''A generator that yields elements of the tree in-order.

        Args:
            iterable: The tree to be iterated.
        '''
        node = iterable.get_root()
        st = []
        while len(st) > 0:
            if node != None:
                st.append(node)
                node = node.get_left()
            else:
                if len(st) > 0:
                    node = st.pop()
                    yield node.get_data()
                    node = node.get_right()

    def __iter__(self):
        '''iter method overloader.'''
        return self

    def __next__(self):
        '''next method overloader.'''
        return next(self._iterator)
