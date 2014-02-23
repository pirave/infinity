from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import six

import numpy as np

from matplotlib.path import Path
from nose.tools import assert_raises


def test_readonly_path():
    path = Path.unit_circle()

    def modify_vertices():
        path.vertices = path.vertices * 2.0

    assert_raises(AttributeError, modify_vertices)


def test_point_in_path():
    # Test #1787
    verts2 = [(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]

    path = Path(verts2, closed=True)
    points = [(0.5, 0.5), (1.5, 0.5)]

    assert np.all(path.contains_points(points) == [True, False])


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'], exit=False)
