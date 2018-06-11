'''Data structure base class.'''


import abc
import six


@six.add_metaclass(abc.ABCMeta)
class DataStructure(object):
    '''The base class for all dsviz data structures.'''

    def __init__(self, name, data_type, max_size):
        '''Constructor for a data structure.

        Args:
            name: An identifier for the data structure.
            data_type: The type of data that the data structure will store.
            max_size: The upper limit for the size of the data structure.

        Raises:
            IndexError: If the max size paramater is non-positive.
        '''
        if max_size < 1:
            raise IndexError('Max size parameter must be non-positive.')

        self.name = name
        self.data_type = data_type
        self.max_size = max_size

    @abc.abstractmethod
    def render(self, path, description=''):
        '''Renders an image representation of the current state of the data
        structure.

        Args:
            path: The path where the image will be saved.
            description: An optional argument that describes the data structure
                being rendered.
        '''
        raise NotImplementedError

    @abc.abstractmethod
    def is_empty(self):
        '''Returns true is the data structure is empty.'''
        raise NotImplementedError

    @abc.abstractmethod
    def __len__(self):
        '''Returns the size of the data structure.'''
        raise NotImplementedError
