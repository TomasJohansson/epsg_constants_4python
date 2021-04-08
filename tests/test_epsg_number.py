#!/usr/bin/env python

# Run the tests as below from the root folder of this python project:
# cd [THE_ROOT_FOLDER]
# python -m unittest discover -s tests

"""Tests for `epsg_constants` package."""


import unittest

from epsg_constants.epsg_number import EpsgNumber

class TestEpsg_constants(unittest.TestCase):
    """Tests for `epsg_constants` package."""

    def test_someConstants(self):
        self.assertEqual(
            EpsgNumber.WORLD__WGS_84__4326,
            4326
        )

        self.assertEqual(
            EpsgNumber.SWEDEN__SWEREF99_TM__3006,
            3006
        )

        self.assertEqual(
            EpsgNumber.SWEDEN__12_00__SWEREF99_12_00__3007,
            3007
        )
