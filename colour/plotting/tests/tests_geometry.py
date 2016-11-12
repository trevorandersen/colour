#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Defines unit tests for :mod:`colour.plotting.geometry` module.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest

from colour.plotting import quad, grid, cube

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2016 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['TestQuad',
           'TestGrid',
           'TestCube']


class TestQuad(unittest.TestCase):
    """
    Defines :func:`colour.plotting.geometry.quad` definition unit tests
    methods.
    """

    def test_quad(self):
        """
        Tests :func:`colour.plotting.geometry.quad` definition.
        """

        np.testing.assert_almost_equal(
            quad(),
            np.array([[0, 0, 0],
                      [1, 0, 0],
                      [1, 1, 0],
                      [0, 1, 0]]),
            decimal=7)

        np.testing.assert_almost_equal(
            quad('xz'),
            np.array([[0, 0, 0],
                      [1, 0, 0],
                      [1, 0, 1],
                      [0, 0, 1]]),
            decimal=7)

        np.testing.assert_almost_equal(
            quad('yz'),
            np.array([[0, 0, 0],
                      [0, 1, 0],
                      [0, 1, 1],
                      [0, 0, 1]]),
            decimal=7)

        np.testing.assert_almost_equal(
            quad('xy',
                 origin=np.array([0.2, 0.4]),
                 width=0.2,
                 height=0.4,
                 depth=0.6),
            np.array([[0.2, 0.4, 0.6],
                      [0.4, 0.4, 0.6],
                      [0.4, 0.8, 0.6],
                      [0.2, 0.8, 0.6]]),
            decimal=7)

        np.testing.assert_almost_equal(
            quad('xy',
                 origin=np.array([-0.2, -0.4]),
                 width=-0.2,
                 height=-0.4,
                 depth=-0.6),
            np.array([[-0.2, -0.4, -0.6],
                      [-0.4, -0.4, -0.6],
                      [-0.4, -0.8, -0.6],
                      [-0.2, -0.8, -0.6]]),
            decimal=7)


class TestGrid(unittest.TestCase):
    """
    Defines :func:`colour.plotting.geometry.grid` definition unit tests
    methods.
    """

    def test_grid(self):
        """
        Tests :func:`colour.plotting.geometry.grid` definition.
        """

        np.testing.assert_almost_equal(
            grid(),
            np.array([[[0, 0, 0],
                       [1, 0, 0],
                       [1, 1, 0],
                       [0, 1, 0]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            grid('xz'),
            np.array([[[0, 0, 0],
                       [1, 0, 0],
                       [1, 0, 1],
                       [0, 0, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            grid('yz'),
            np.array([[[0, 0, 0],
                       [0, 1, 0],
                       [0, 1, 1],
                       [0, 0, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            grid('xy',
                 origin=np.array([0.2, 0.4]),
                 width=0.2,
                 height=0.4,
                 depth=0.6,
                 width_segments=3,
                 height_segments=3),
            np.array([[[0.20000000, 0.40000000, 0.60000000],
                       [0.26666667, 0.40000000, 0.60000000],
                       [0.26666667, 0.53333333, 0.60000000],
                       [0.20000000, 0.53333333, 0.60000000]],
                      [[0.20000000, 0.53333333, 0.60000000],
                       [0.26666667, 0.53333333, 0.60000000],
                       [0.26666667, 0.66666667, 0.60000000],
                       [0.20000000, 0.66666667, 0.60000000]],
                      [[0.20000000, 0.66666667, 0.60000000],
                       [0.26666667, 0.66666667, 0.60000000],
                       [0.26666667, 0.80000000, 0.60000000],
                       [0.20000000, 0.80000000, 0.60000000]],
                      [[0.26666667, 0.40000000, 0.60000000],
                       [0.33333333, 0.40000000, 0.60000000],
                       [0.33333333, 0.53333333, 0.60000000],
                       [0.26666667, 0.53333333, 0.60000000]],
                      [[0.26666667, 0.53333333, 0.60000000],
                       [0.33333333, 0.53333333, 0.60000000],
                       [0.33333333, 0.66666667, 0.60000000],
                       [0.26666667, 0.66666667, 0.60000000]],
                      [[0.26666667, 0.66666667, 0.60000000],
                       [0.33333333, 0.66666667, 0.60000000],
                       [0.33333333, 0.80000000, 0.60000000],
                       [0.26666667, 0.80000000, 0.60000000]],
                      [[0.33333333, 0.40000000, 0.60000000],
                       [0.40000000, 0.40000000, 0.60000000],
                       [0.40000000, 0.53333333, 0.60000000],
                       [0.33333333, 0.53333333, 0.60000000]],
                      [[0.33333333, 0.53333333, 0.60000000],
                       [0.40000000, 0.53333333, 0.60000000],
                       [0.40000000, 0.66666667, 0.60000000],
                       [0.33333333, 0.66666667, 0.60000000]],
                      [[0.33333333, 0.66666667, 0.60000000],
                       [0.40000000, 0.66666667, 0.60000000],
                       [0.40000000, 0.80000000, 0.60000000],
                       [0.33333333, 0.80000000, 0.60000000]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            grid('xy',
                 origin=np.array([-0.2, -0.4]),
                 width=-0.2,
                 height=-0.4,
                 depth=-0.6,
                 width_segments=3,
                 height_segments=3),
            np.array([[[-0.20000000, -0.40000000, -0.60000000],
                       [-0.26666667, -0.40000000, -0.60000000],
                       [-0.26666667, -0.53333333, -0.60000000],
                       [-0.20000000, -0.53333333, -0.60000000]],
                      [[-0.20000000, -0.53333333, -0.60000000],
                       [-0.26666667, -0.53333333, -0.60000000],
                       [-0.26666667, -0.66666667, -0.60000000],
                       [-0.20000000, -0.66666667, -0.60000000]],
                      [[-0.20000000, -0.66666667, -0.60000000],
                       [-0.26666667, -0.66666667, -0.60000000],
                       [-0.26666667, -0.80000000, -0.60000000],
                       [-0.20000000, -0.80000000, -0.60000000]],
                      [[-0.26666667, -0.40000000, -0.60000000],
                       [-0.33333333, -0.40000000, -0.60000000],
                       [-0.33333333, -0.53333333, -0.60000000],
                       [-0.26666667, -0.53333333, -0.60000000]],
                      [[-0.26666667, -0.53333333, -0.60000000],
                       [-0.33333333, -0.53333333, -0.60000000],
                       [-0.33333333, -0.66666667, -0.60000000],
                       [-0.26666667, -0.66666667, -0.60000000]],
                      [[-0.26666667, -0.66666667, -0.60000000],
                       [-0.33333333, -0.66666667, -0.60000000],
                       [-0.33333333, -0.80000000, -0.60000000],
                       [-0.26666667, -0.80000000, -0.60000000]],
                      [[-0.33333333, -0.40000000, -0.60000000],
                       [-0.40000000, -0.40000000, -0.60000000],
                       [-0.40000000, -0.53333333, -0.60000000],
                       [-0.33333333, -0.53333333, -0.60000000]],
                      [[-0.33333333, -0.53333333, -0.60000000],
                       [-0.40000000, -0.53333333, -0.60000000],
                       [-0.40000000, -0.66666667, -0.60000000],
                       [-0.33333333, -0.66666667, -0.60000000]],
                      [[-0.33333333, -0.66666667, -0.60000000],
                       [-0.40000000, -0.66666667, -0.60000000],
                       [-0.40000000, -0.80000000, -0.60000000],
                       [-0.33333333, -0.80000000, -0.60000000]]]),
            decimal=7)


class TestCube(unittest.TestCase):
    """
    Defines :func:`colour.plotting.geometry.cube` definition unit tests
    methods.
    """

    def test_cube(self):
        """
        Tests :func:`colour.plotting.geometry.cube` definition.
        """

        np.testing.assert_almost_equal(
            cube(),
            np.array([[[0, 0, 0],
                       [1, 0, 0],
                       [1, 1, 0],
                       [0, 1, 0]],
                      [[0, 0, 1],
                       [1, 0, 1],
                       [1, 1, 1],
                       [0, 1, 1]],
                      [[0, 0, 0],
                       [1, 0, 0],
                       [1, 0, 1],
                       [0, 0, 1]],
                      [[0, 1, 0],
                       [1, 1, 0],
                       [1, 1, 1],
                       [0, 1, 1]],
                      [[0, 0, 0],
                       [0, 1, 0],
                       [0, 1, 1],
                       [0, 0, 1]],
                      [[1, 0, 0],
                       [1, 1, 0],
                       [1, 1, 1],
                       [1, 0, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            cube(('+x',)),
            np.array([[[1, 0, 0],
                       [1, 1, 0],
                       [1, 1, 1],
                       [1, 0, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            cube(('-x',)),
            np.array([[[0, 0, 0],
                       [0, 1, 0],
                       [0, 1, 1],
                       [0, 0, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            cube(('+y',)),
            np.array([[[0, 1, 0],
                       [1, 1, 0],
                       [1, 1, 1],
                       [0, 1, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            cube(('-y',)),
            np.array([[[0, 0, 0],
                       [1, 0, 0],
                       [1, 0, 1],
                       [0, 0, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            cube(('+z',)),
            np.array([[[0, 0, 1],
                       [1, 0, 1],
                       [1, 1, 1],
                       [0, 1, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            cube(('-z',)),
            np.array([[[0, 0, 0],
                       [1, 0, 0],
                       [1, 1, 0],
                       [0, 1, 0]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            cube(origin=np.array([0.2, 0.4, 0.6]),
                 width=0.2,
                 height=0.4,
                 depth=0.6,
                 width_segments=3,
                 height_segments=3,
                 depth_segments=3),
            np.array([[[0.20000000, 0.60000000, 0.40000000],
                       [0.26666667, 0.60000000, 0.40000000],
                       [0.26666667, 0.80000000, 0.40000000],
                       [0.20000000, 0.80000000, 0.40000000]],
                      [[0.20000000, 0.80000000, 0.40000000],
                       [0.26666667, 0.80000000, 0.40000000],
                       [0.26666667, 1.00000000, 0.40000000],
                       [0.20000000, 1.00000000, 0.40000000]],
                      [[0.20000000, 1.00000000, 0.40000000],
                       [0.26666667, 1.00000000, 0.40000000],
                       [0.26666667, 1.20000000, 0.40000000],
                       [0.20000000, 1.20000000, 0.40000000]],
                      [[0.26666667, 0.60000000, 0.40000000],
                       [0.33333333, 0.60000000, 0.40000000],
                       [0.33333333, 0.80000000, 0.40000000],
                       [0.26666667, 0.80000000, 0.40000000]],
                      [[0.26666667, 0.80000000, 0.40000000],
                       [0.33333333, 0.80000000, 0.40000000],
                       [0.33333333, 1.00000000, 0.40000000],
                       [0.26666667, 1.00000000, 0.40000000]],
                      [[0.26666667, 1.00000000, 0.40000000],
                       [0.33333333, 1.00000000, 0.40000000],
                       [0.33333333, 1.20000000, 0.40000000],
                       [0.26666667, 1.20000000, 0.40000000]],
                      [[0.33333333, 0.60000000, 0.40000000],
                       [0.40000000, 0.60000000, 0.40000000],
                       [0.40000000, 0.80000000, 0.40000000],
                       [0.33333333, 0.80000000, 0.40000000]],
                      [[0.33333333, 0.80000000, 0.40000000],
                       [0.40000000, 0.80000000, 0.40000000],
                       [0.40000000, 1.00000000, 0.40000000],
                       [0.33333333, 1.00000000, 0.40000000]],
                      [[0.33333333, 1.00000000, 0.40000000],
                       [0.40000000, 1.00000000, 0.40000000],
                       [0.40000000, 1.20000000, 0.40000000],
                       [0.33333333, 1.20000000, 0.40000000]],
                      [[0.20000000, 0.60000000, 0.80000000],
                       [0.26666667, 0.60000000, 0.80000000],
                       [0.26666667, 0.80000000, 0.80000000],
                       [0.20000000, 0.80000000, 0.80000000]],
                      [[0.20000000, 0.80000000, 0.80000000],
                       [0.26666667, 0.80000000, 0.80000000],
                       [0.26666667, 1.00000000, 0.80000000],
                       [0.20000000, 1.00000000, 0.80000000]],
                      [[0.20000000, 1.00000000, 0.80000000],
                       [0.26666667, 1.00000000, 0.80000000],
                       [0.26666667, 1.20000000, 0.80000000],
                       [0.20000000, 1.20000000, 0.80000000]],
                      [[0.26666667, 0.60000000, 0.80000000],
                       [0.33333333, 0.60000000, 0.80000000],
                       [0.33333333, 0.80000000, 0.80000000],
                       [0.26666667, 0.80000000, 0.80000000]],
                      [[0.26666667, 0.80000000, 0.80000000],
                       [0.33333333, 0.80000000, 0.80000000],
                       [0.33333333, 1.00000000, 0.80000000],
                       [0.26666667, 1.00000000, 0.80000000]],
                      [[0.26666667, 1.00000000, 0.80000000],
                       [0.33333333, 1.00000000, 0.80000000],
                       [0.33333333, 1.20000000, 0.80000000],
                       [0.26666667, 1.20000000, 0.80000000]],
                      [[0.33333333, 0.60000000, 0.80000000],
                       [0.40000000, 0.60000000, 0.80000000],
                       [0.40000000, 0.80000000, 0.80000000],
                       [0.33333333, 0.80000000, 0.80000000]],
                      [[0.33333333, 0.80000000, 0.80000000],
                       [0.40000000, 0.80000000, 0.80000000],
                       [0.40000000, 1.00000000, 0.80000000],
                       [0.33333333, 1.00000000, 0.80000000]],
                      [[0.33333333, 1.00000000, 0.80000000],
                       [0.40000000, 1.00000000, 0.80000000],
                       [0.40000000, 1.20000000, 0.80000000],
                       [0.33333333, 1.20000000, 0.80000000]],
                      [[0.20000000, 0.60000000, 0.40000000],
                       [0.26666667, 0.60000000, 0.40000000],
                       [0.26666667, 0.60000000, 0.53333333],
                       [0.20000000, 0.60000000, 0.53333333]],
                      [[0.20000000, 0.60000000, 0.53333333],
                       [0.26666667, 0.60000000, 0.53333333],
                       [0.26666667, 0.60000000, 0.66666667],
                       [0.20000000, 0.60000000, 0.66666667]],
                      [[0.20000000, 0.60000000, 0.66666667],
                       [0.26666667, 0.60000000, 0.66666667],
                       [0.26666667, 0.60000000, 0.80000000],
                       [0.20000000, 0.60000000, 0.80000000]],
                      [[0.26666667, 0.60000000, 0.40000000],
                       [0.33333333, 0.60000000, 0.40000000],
                       [0.33333333, 0.60000000, 0.53333333],
                       [0.26666667, 0.60000000, 0.53333333]],
                      [[0.26666667, 0.60000000, 0.53333333],
                       [0.33333333, 0.60000000, 0.53333333],
                       [0.33333333, 0.60000000, 0.66666667],
                       [0.26666667, 0.60000000, 0.66666667]],
                      [[0.26666667, 0.60000000, 0.66666667],
                       [0.33333333, 0.60000000, 0.66666667],
                       [0.33333333, 0.60000000, 0.80000000],
                       [0.26666667, 0.60000000, 0.80000000]],
                      [[0.33333333, 0.60000000, 0.40000000],
                       [0.40000000, 0.60000000, 0.40000000],
                       [0.40000000, 0.60000000, 0.53333333],
                       [0.33333333, 0.60000000, 0.53333333]],
                      [[0.33333333, 0.60000000, 0.53333333],
                       [0.40000000, 0.60000000, 0.53333333],
                       [0.40000000, 0.60000000, 0.66666667],
                       [0.33333333, 0.60000000, 0.66666667]],
                      [[0.33333333, 0.60000000, 0.66666667],
                       [0.40000000, 0.60000000, 0.66666667],
                       [0.40000000, 0.60000000, 0.80000000],
                       [0.33333333, 0.60000000, 0.80000000]],
                      [[0.20000000, 1.20000000, 0.40000000],
                       [0.26666667, 1.20000000, 0.40000000],
                       [0.26666667, 1.20000000, 0.53333333],
                       [0.20000000, 1.20000000, 0.53333333]],
                      [[0.20000000, 1.20000000, 0.53333333],
                       [0.26666667, 1.20000000, 0.53333333],
                       [0.26666667, 1.20000000, 0.66666667],
                       [0.20000000, 1.20000000, 0.66666667]],
                      [[0.20000000, 1.20000000, 0.66666667],
                       [0.26666667, 1.20000000, 0.66666667],
                       [0.26666667, 1.20000000, 0.80000000],
                       [0.20000000, 1.20000000, 0.80000000]],
                      [[0.26666667, 1.20000000, 0.40000000],
                       [0.33333333, 1.20000000, 0.40000000],
                       [0.33333333, 1.20000000, 0.53333333],
                       [0.26666667, 1.20000000, 0.53333333]],
                      [[0.26666667, 1.20000000, 0.53333333],
                       [0.33333333, 1.20000000, 0.53333333],
                       [0.33333333, 1.20000000, 0.66666667],
                       [0.26666667, 1.20000000, 0.66666667]],
                      [[0.26666667, 1.20000000, 0.66666667],
                       [0.33333333, 1.20000000, 0.66666667],
                       [0.33333333, 1.20000000, 0.80000000],
                       [0.26666667, 1.20000000, 0.80000000]],
                      [[0.33333333, 1.20000000, 0.40000000],
                       [0.40000000, 1.20000000, 0.40000000],
                       [0.40000000, 1.20000000, 0.53333333],
                       [0.33333333, 1.20000000, 0.53333333]],
                      [[0.33333333, 1.20000000, 0.53333333],
                       [0.40000000, 1.20000000, 0.53333333],
                       [0.40000000, 1.20000000, 0.66666667],
                       [0.33333333, 1.20000000, 0.66666667]],
                      [[0.33333333, 1.20000000, 0.66666667],
                       [0.40000000, 1.20000000, 0.66666667],
                       [0.40000000, 1.20000000, 0.80000000],
                       [0.33333333, 1.20000000, 0.80000000]],
                      [[0.20000000, 0.60000000, 0.40000000],
                       [0.20000000, 0.80000000, 0.40000000],
                       [0.20000000, 0.80000000, 0.53333333],
                       [0.20000000, 0.60000000, 0.53333333]],
                      [[0.20000000, 0.60000000, 0.53333333],
                       [0.20000000, 0.80000000, 0.53333333],
                       [0.20000000, 0.80000000, 0.66666667],
                       [0.20000000, 0.60000000, 0.66666667]],
                      [[0.20000000, 0.60000000, 0.66666667],
                       [0.20000000, 0.80000000, 0.66666667],
                       [0.20000000, 0.80000000, 0.80000000],
                       [0.20000000, 0.60000000, 0.80000000]],
                      [[0.20000000, 0.80000000, 0.40000000],
                       [0.20000000, 1.00000000, 0.40000000],
                       [0.20000000, 1.00000000, 0.53333333],
                       [0.20000000, 0.80000000, 0.53333333]],
                      [[0.20000000, 0.80000000, 0.53333333],
                       [0.20000000, 1.00000000, 0.53333333],
                       [0.20000000, 1.00000000, 0.66666667],
                       [0.20000000, 0.80000000, 0.66666667]],
                      [[0.20000000, 0.80000000, 0.66666667],
                       [0.20000000, 1.00000000, 0.66666667],
                       [0.20000000, 1.00000000, 0.80000000],
                       [0.20000000, 0.80000000, 0.80000000]],
                      [[0.20000000, 1.00000000, 0.40000000],
                       [0.20000000, 1.20000000, 0.40000000],
                       [0.20000000, 1.20000000, 0.53333333],
                       [0.20000000, 1.00000000, 0.53333333]],
                      [[0.20000000, 1.00000000, 0.53333333],
                       [0.20000000, 1.20000000, 0.53333333],
                       [0.20000000, 1.20000000, 0.66666667],
                       [0.20000000, 1.00000000, 0.66666667]],
                      [[0.20000000, 1.00000000, 0.66666667],
                       [0.20000000, 1.20000000, 0.66666667],
                       [0.20000000, 1.20000000, 0.80000000],
                       [0.20000000, 1.00000000, 0.80000000]],
                      [[0.40000000, 0.60000000, 0.40000000],
                       [0.40000000, 0.80000000, 0.40000000],
                       [0.40000000, 0.80000000, 0.53333333],
                       [0.40000000, 0.60000000, 0.53333333]],
                      [[0.40000000, 0.60000000, 0.53333333],
                       [0.40000000, 0.80000000, 0.53333333],
                       [0.40000000, 0.80000000, 0.66666667],
                       [0.40000000, 0.60000000, 0.66666667]],
                      [[0.40000000, 0.60000000, 0.66666667],
                       [0.40000000, 0.80000000, 0.66666667],
                       [0.40000000, 0.80000000, 0.80000000],
                       [0.40000000, 0.60000000, 0.80000000]],
                      [[0.40000000, 0.80000000, 0.40000000],
                       [0.40000000, 1.00000000, 0.40000000],
                       [0.40000000, 1.00000000, 0.53333333],
                       [0.40000000, 0.80000000, 0.53333333]],
                      [[0.40000000, 0.80000000, 0.53333333],
                       [0.40000000, 1.00000000, 0.53333333],
                       [0.40000000, 1.00000000, 0.66666667],
                       [0.40000000, 0.80000000, 0.66666667]],
                      [[0.40000000, 0.80000000, 0.66666667],
                       [0.40000000, 1.00000000, 0.66666667],
                       [0.40000000, 1.00000000, 0.80000000],
                       [0.40000000, 0.80000000, 0.80000000]],
                      [[0.40000000, 1.00000000, 0.40000000],
                       [0.40000000, 1.20000000, 0.40000000],
                       [0.40000000, 1.20000000, 0.53333333],
                       [0.40000000, 1.00000000, 0.53333333]],
                      [[0.40000000, 1.00000000, 0.53333333],
                       [0.40000000, 1.20000000, 0.53333333],
                       [0.40000000, 1.20000000, 0.66666667],
                       [0.40000000, 1.00000000, 0.66666667]],
                      [[0.40000000, 1.00000000, 0.66666667],
                       [0.40000000, 1.20000000, 0.66666667],
                       [0.40000000, 1.20000000, 0.80000000],
                       [0.40000000, 1.00000000, 0.80000000]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            cube(origin=np.array([-0.2, -0.4, -0.6]),
                 width=-0.2,
                 height=-0.4,
                 depth=-0.6,
                 width_segments=3,
                 height_segments=3,
                 depth_segments=3),
            np.array([[[-0.20000000, -0.60000000, -0.40000000],
                       [-0.26666667, -0.60000000, -0.40000000],
                       [-0.26666667, -0.80000000, -0.40000000],
                       [-0.20000000, -0.80000000, -0.40000000]],
                      [[-0.20000000, -0.80000000, -0.40000000],
                       [-0.26666667, -0.80000000, -0.40000000],
                       [-0.26666667, -1.00000000, -0.40000000],
                       [-0.20000000, -1.00000000, -0.40000000]],
                      [[-0.20000000, -1.00000000, -0.40000000],
                       [-0.26666667, -1.00000000, -0.40000000],
                       [-0.26666667, -1.20000000, -0.40000000],
                       [-0.20000000, -1.20000000, -0.40000000]],
                      [[-0.26666667, -0.60000000, -0.40000000],
                       [-0.33333333, -0.60000000, -0.40000000],
                       [-0.33333333, -0.80000000, -0.40000000],
                       [-0.26666667, -0.80000000, -0.40000000]],
                      [[-0.26666667, -0.80000000, -0.40000000],
                       [-0.33333333, -0.80000000, -0.40000000],
                       [-0.33333333, -1.00000000, -0.40000000],
                       [-0.26666667, -1.00000000, -0.40000000]],
                      [[-0.26666667, -1.00000000, -0.40000000],
                       [-0.33333333, -1.00000000, -0.40000000],
                       [-0.33333333, -1.20000000, -0.40000000],
                       [-0.26666667, -1.20000000, -0.40000000]],
                      [[-0.33333333, -0.60000000, -0.40000000],
                       [-0.40000000, -0.60000000, -0.40000000],
                       [-0.40000000, -0.80000000, -0.40000000],
                       [-0.33333333, -0.80000000, -0.40000000]],
                      [[-0.33333333, -0.80000000, -0.40000000],
                       [-0.40000000, -0.80000000, -0.40000000],
                       [-0.40000000, -1.00000000, -0.40000000],
                       [-0.33333333, -1.00000000, -0.40000000]],
                      [[-0.33333333, -1.00000000, -0.40000000],
                       [-0.40000000, -1.00000000, -0.40000000],
                       [-0.40000000, -1.20000000, -0.40000000],
                       [-0.33333333, -1.20000000, -0.40000000]],
                      [[-0.20000000, -0.60000000, -0.80000000],
                       [-0.26666667, -0.60000000, -0.80000000],
                       [-0.26666667, -0.80000000, -0.80000000],
                       [-0.20000000, -0.80000000, -0.80000000]],
                      [[-0.20000000, -0.80000000, -0.80000000],
                       [-0.26666667, -0.80000000, -0.80000000],
                       [-0.26666667, -1.00000000, -0.80000000],
                       [-0.20000000, -1.00000000, -0.80000000]],
                      [[-0.20000000, -1.00000000, -0.80000000],
                       [-0.26666667, -1.00000000, -0.80000000],
                       [-0.26666667, -1.20000000, -0.80000000],
                       [-0.20000000, -1.20000000, -0.80000000]],
                      [[-0.26666667, -0.60000000, -0.80000000],
                       [-0.33333333, -0.60000000, -0.80000000],
                       [-0.33333333, -0.80000000, -0.80000000],
                       [-0.26666667, -0.80000000, -0.80000000]],
                      [[-0.26666667, -0.80000000, -0.80000000],
                       [-0.33333333, -0.80000000, -0.80000000],
                       [-0.33333333, -1.00000000, -0.80000000],
                       [-0.26666667, -1.00000000, -0.80000000]],
                      [[-0.26666667, -1.00000000, -0.80000000],
                       [-0.33333333, -1.00000000, -0.80000000],
                       [-0.33333333, -1.20000000, -0.80000000],
                       [-0.26666667, -1.20000000, -0.80000000]],
                      [[-0.33333333, -0.60000000, -0.80000000],
                       [-0.40000000, -0.60000000, -0.80000000],
                       [-0.40000000, -0.80000000, -0.80000000],
                       [-0.33333333, -0.80000000, -0.80000000]],
                      [[-0.33333333, -0.80000000, -0.80000000],
                       [-0.40000000, -0.80000000, -0.80000000],
                       [-0.40000000, -1.00000000, -0.80000000],
                       [-0.33333333, -1.00000000, -0.80000000]],
                      [[-0.33333333, -1.00000000, -0.80000000],
                       [-0.40000000, -1.00000000, -0.80000000],
                       [-0.40000000, -1.20000000, -0.80000000],
                       [-0.33333333, -1.20000000, -0.80000000]],
                      [[-0.20000000, -0.60000000, -0.40000000],
                       [-0.26666667, -0.60000000, -0.40000000],
                       [-0.26666667, -0.60000000, -0.53333333],
                       [-0.20000000, -0.60000000, -0.53333333]],
                      [[-0.20000000, -0.60000000, -0.53333333],
                       [-0.26666667, -0.60000000, -0.53333333],
                       [-0.26666667, -0.60000000, -0.66666667],
                       [-0.20000000, -0.60000000, -0.66666667]],
                      [[-0.20000000, -0.60000000, -0.66666667],
                       [-0.26666667, -0.60000000, -0.66666667],
                       [-0.26666667, -0.60000000, -0.80000000],
                       [-0.20000000, -0.60000000, -0.80000000]],
                      [[-0.26666667, -0.60000000, -0.40000000],
                       [-0.33333333, -0.60000000, -0.40000000],
                       [-0.33333333, -0.60000000, -0.53333333],
                       [-0.26666667, -0.60000000, -0.53333333]],
                      [[-0.26666667, -0.60000000, -0.53333333],
                       [-0.33333333, -0.60000000, -0.53333333],
                       [-0.33333333, -0.60000000, -0.66666667],
                       [-0.26666667, -0.60000000, -0.66666667]],
                      [[-0.26666667, -0.60000000, -0.66666667],
                       [-0.33333333, -0.60000000, -0.66666667],
                       [-0.33333333, -0.60000000, -0.80000000],
                       [-0.26666667, -0.60000000, -0.80000000]],
                      [[-0.33333333, -0.60000000, -0.40000000],
                       [-0.40000000, -0.60000000, -0.40000000],
                       [-0.40000000, -0.60000000, -0.53333333],
                       [-0.33333333, -0.60000000, -0.53333333]],
                      [[-0.33333333, -0.60000000, -0.53333333],
                       [-0.40000000, -0.60000000, -0.53333333],
                       [-0.40000000, -0.60000000, -0.66666667],
                       [-0.33333333, -0.60000000, -0.66666667]],
                      [[-0.33333333, -0.60000000, -0.66666667],
                       [-0.40000000, -0.60000000, -0.66666667],
                       [-0.40000000, -0.60000000, -0.80000000],
                       [-0.33333333, -0.60000000, -0.80000000]],
                      [[-0.20000000, -1.20000000, -0.40000000],
                       [-0.26666667, -1.20000000, -0.40000000],
                       [-0.26666667, -1.20000000, -0.53333333],
                       [-0.20000000, -1.20000000, -0.53333333]],
                      [[-0.20000000, -1.20000000, -0.53333333],
                       [-0.26666667, -1.20000000, -0.53333333],
                       [-0.26666667, -1.20000000, -0.66666667],
                       [-0.20000000, -1.20000000, -0.66666667]],
                      [[-0.20000000, -1.20000000, -0.66666667],
                       [-0.26666667, -1.20000000, -0.66666667],
                       [-0.26666667, -1.20000000, -0.80000000],
                       [-0.20000000, -1.20000000, -0.80000000]],
                      [[-0.26666667, -1.20000000, -0.40000000],
                       [-0.33333333, -1.20000000, -0.40000000],
                       [-0.33333333, -1.20000000, -0.53333333],
                       [-0.26666667, -1.20000000, -0.53333333]],
                      [[-0.26666667, -1.20000000, -0.53333333],
                       [-0.33333333, -1.20000000, -0.53333333],
                       [-0.33333333, -1.20000000, -0.66666667],
                       [-0.26666667, -1.20000000, -0.66666667]],
                      [[-0.26666667, -1.20000000, -0.66666667],
                       [-0.33333333, -1.20000000, -0.66666667],
                       [-0.33333333, -1.20000000, -0.80000000],
                       [-0.26666667, -1.20000000, -0.80000000]],
                      [[-0.33333333, -1.20000000, -0.40000000],
                       [-0.40000000, -1.20000000, -0.40000000],
                       [-0.40000000, -1.20000000, -0.53333333],
                       [-0.33333333, -1.20000000, -0.53333333]],
                      [[-0.33333333, -1.20000000, -0.53333333],
                       [-0.40000000, -1.20000000, -0.53333333],
                       [-0.40000000, -1.20000000, -0.66666667],
                       [-0.33333333, -1.20000000, -0.66666667]],
                      [[-0.33333333, -1.20000000, -0.66666667],
                       [-0.40000000, -1.20000000, -0.66666667],
                       [-0.40000000, -1.20000000, -0.80000000],
                       [-0.33333333, -1.20000000, -0.80000000]],
                      [[-0.20000000, -0.60000000, -0.40000000],
                       [-0.20000000, -0.80000000, -0.40000000],
                       [-0.20000000, -0.80000000, -0.53333333],
                       [-0.20000000, -0.60000000, -0.53333333]],
                      [[-0.20000000, -0.60000000, -0.53333333],
                       [-0.20000000, -0.80000000, -0.53333333],
                       [-0.20000000, -0.80000000, -0.66666667],
                       [-0.20000000, -0.60000000, -0.66666667]],
                      [[-0.20000000, -0.60000000, -0.66666667],
                       [-0.20000000, -0.80000000, -0.66666667],
                       [-0.20000000, -0.80000000, -0.80000000],
                       [-0.20000000, -0.60000000, -0.80000000]],
                      [[-0.20000000, -0.80000000, -0.40000000],
                       [-0.20000000, -1.00000000, -0.40000000],
                       [-0.20000000, -1.00000000, -0.53333333],
                       [-0.20000000, -0.80000000, -0.53333333]],
                      [[-0.20000000, -0.80000000, -0.53333333],
                       [-0.20000000, -1.00000000, -0.53333333],
                       [-0.20000000, -1.00000000, -0.66666667],
                       [-0.20000000, -0.80000000, -0.66666667]],
                      [[-0.20000000, -0.80000000, -0.66666667],
                       [-0.20000000, -1.00000000, -0.66666667],
                       [-0.20000000, -1.00000000, -0.80000000],
                       [-0.20000000, -0.80000000, -0.80000000]],
                      [[-0.20000000, -1.00000000, -0.40000000],
                       [-0.20000000, -1.20000000, -0.40000000],
                       [-0.20000000, -1.20000000, -0.53333333],
                       [-0.20000000, -1.00000000, -0.53333333]],
                      [[-0.20000000, -1.00000000, -0.53333333],
                       [-0.20000000, -1.20000000, -0.53333333],
                       [-0.20000000, -1.20000000, -0.66666667],
                       [-0.20000000, -1.00000000, -0.66666667]],
                      [[-0.20000000, -1.00000000, -0.66666667],
                       [-0.20000000, -1.20000000, -0.66666667],
                       [-0.20000000, -1.20000000, -0.80000000],
                       [-0.20000000, -1.00000000, -0.80000000]],
                      [[-0.40000000, -0.60000000, -0.40000000],
                       [-0.40000000, -0.80000000, -0.40000000],
                       [-0.40000000, -0.80000000, -0.53333333],
                       [-0.40000000, -0.60000000, -0.53333333]],
                      [[-0.40000000, -0.60000000, -0.53333333],
                       [-0.40000000, -0.80000000, -0.53333333],
                       [-0.40000000, -0.80000000, -0.66666667],
                       [-0.40000000, -0.60000000, -0.66666667]],
                      [[-0.40000000, -0.60000000, -0.66666667],
                       [-0.40000000, -0.80000000, -0.66666667],
                       [-0.40000000, -0.80000000, -0.80000000],
                       [-0.40000000, -0.60000000, -0.80000000]],
                      [[-0.40000000, -0.80000000, -0.40000000],
                       [-0.40000000, -1.00000000, -0.40000000],
                       [-0.40000000, -1.00000000, -0.53333333],
                       [-0.40000000, -0.80000000, -0.53333333]],
                      [[-0.40000000, -0.80000000, -0.53333333],
                       [-0.40000000, -1.00000000, -0.53333333],
                       [-0.40000000, -1.00000000, -0.66666667],
                       [-0.40000000, -0.80000000, -0.66666667]],
                      [[-0.40000000, -0.80000000, -0.66666667],
                       [-0.40000000, -1.00000000, -0.66666667],
                       [-0.40000000, -1.00000000, -0.80000000],
                       [-0.40000000, -0.80000000, -0.80000000]],
                      [[-0.40000000, -1.00000000, -0.40000000],
                       [-0.40000000, -1.20000000, -0.40000000],
                       [-0.40000000, -1.20000000, -0.53333333],
                       [-0.40000000, -1.00000000, -0.53333333]],
                      [[-0.40000000, -1.00000000, -0.53333333],
                       [-0.40000000, -1.20000000, -0.53333333],
                       [-0.40000000, -1.20000000, -0.66666667],
                       [-0.40000000, -1.00000000, -0.66666667]],
                      [[-0.40000000, -1.00000000, -0.66666667],
                       [-0.40000000, -1.20000000, -0.66666667],
                       [-0.40000000, -1.20000000, -0.80000000],
                       [-0.40000000, -1.00000000, -0.80000000]]]),
            decimal=7)


if __name__ == '__main__':
    unittest.main()
