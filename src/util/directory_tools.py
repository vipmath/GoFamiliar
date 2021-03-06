"""Directory tools"""

from os import walk, path
import fnmatch

def search_tree(directory='.', file_sig='*.*'):
    """Find all files in a directory tree.

    This code snippet was found at
    http://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python

    Working directory is assumed to be set to the containing folder of util.
    >>> matching_files = search_tree(directory='src/util/', file_sig='directory_tools.py')
    >>> matching_files
    ['src/util/directory_tools.py']
    >>> file_obj = open(matching_files[0])

    :param directory: string = root directory of search (default to working directory)
    :param file_sig: string = signature of files being sought
    :return: list = absolute linear locations of all found files
    """

    matches = []
    for root, dirnames, filenames in walk(directory):
        for filename in fnmatch.filter(filenames, file_sig):
            matches.append(path.join(root, filename))

    if matches == []:
        raise IOError('No files found')
    else:
        return matches
