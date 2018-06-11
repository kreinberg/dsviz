'''Utilities for file I/O.'''


import os


def name_to_fname(name):
    '''Converts the name for a data structure to a file name.

    Args:
        name: The name of the data structure.

    Returns:
        A valid file name for the data structure's image.
    '''
    return name.replace(' ', '_').lower() + '.png'


def save_file(image, path, name):
    '''Saves image data to the filesystem.

    Args:
        image: The image to be saved.
        path: The path where the image will be saved.
        name: The name of the data structure.

    Raises:
        ValueError: If the given path is not a valid directory.
    '''
    if path != '' and not os.path.isdir(path):
        raise ValueError('Invalid directory.')
    fname = name_to_fname(name)
    abs_path = os.path.join(path, fname)
    image.save(abs_path, 'PNG')
