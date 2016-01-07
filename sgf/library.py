import os
import h5py
import numpy as np

import sgf.read

doctest_dir = r'sgf_store\hikaru_sgfs'
doctest_file = 'sgfhdf5_doctest.hdf5'

class Library():
    """SGF Library object

    >>> Library(doctest_dir, doctest_file)['chap075.sgf'][:10]
    array([ 72, 288, 300,  42,  59,  97,  61,  62,  80,  41])
    """
    def __init__(self, direc, file):
        while True:
            try:
                self._library_file = h5py.File(os.path.join(direc, file), 'r')
                break
            except OSError:
                sgf.read.create_pro_hdf5(direc=direc, file=file)

    def __getitem__(self, item):
        """

        :param item: str
        :return: h5py.dataset
        >>> Library(doctest_dir, doctest_file)['chap116.sgf']
        <HDF5 dataset "chap116.sgf": shape (262,), type "<i4">
        """
        return self._library_file[item]

    def __len__(self):
        """Return number of stored sgfs

        :return: int
        >>> len(Library(doctest_dir, doctest_file))
        3
        """
        return len(self._library_file)

    def __iter__(self):
        """Return iterator over stored go games

        :return: iter
        >>> for sgf_name in Library(doctest_dir, doctest_file):
        ...     print(sgf_name)
        chap075.sgf
        chap116.sgf
        chap170a.sgf
        """
        return iter(self._library_file)

    def sgf_attributes(self, sgf_name):
        """Return the dictionary of sgf attributes

        :param sgf_name: str
        :return: dict
        >>> l = Library(doctest_dir, doctest_file).sgf_attributes('chap116.sgf')
        >>> l['EV'], l['PB'], l['PW'], l['SZ'], l['KM'], l['RE']
        ('22nd Meijin League', 'Rin Kaiho', 'Yoda Norimoto', '19', '5.50', 'W+0.50')
        """
        return dict(self[sgf_name].attrs)

    def sgf_moves(self, sgf_name):
        """Generate the moves of a given game

        :param sgf_name: str
        :return: int
        >>> for idx, move in enumerate(Library(doctest_dir, doctest_file).sgf_moves('chap075.sgf')):
        ...     if idx < 10:
        ...         print(move)
        72
        288
        300
        42
        59
        97
        61
        62
        80
        41
        """
        for move in list(self[sgf_name]):
            yield move