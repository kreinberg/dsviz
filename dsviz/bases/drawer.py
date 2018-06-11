'''Drawer base class.'''


import abc
import six


@six.add_metaclass(abc.ABCMeta)
class Drawer(object):
    '''The base class for all data structure drawers.'''

    @staticmethod
    @abc.abstractmethod
    def draw(data_structure, description):
        '''Draws an image of the given data structure.

        Args:
            data_structure: The data structure to be drawn.
            description: A description of the data structure.

        Returns:
            An image of the data structure.
        '''

        raise NotImplementedError
