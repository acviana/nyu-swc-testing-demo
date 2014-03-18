#!/usr/bin/env python

"""This is the nosetest module for the coordinates2region.py"""

from coordinates2region import coordinates2region

def test_coordinates2region():
    """This function tests the functionality for the 
    coordinates2region function."""
    assert coordinates2region({'x':0, 'y':0}) == [1], 'Something failed.'
    assert coordinates2region({'x':0, 'y':0}) == [1, 2], 'Something failed.'
    assert coordinates2region({'x':0, 'y':0}) == [1], 'Something failed.'
    assert coordinates2region({'x':0, 'y':0}) == [1], 'Something failed.'
    assert coordinates2region({'x':0, 'y':0}) == [1], 'Something failed.'