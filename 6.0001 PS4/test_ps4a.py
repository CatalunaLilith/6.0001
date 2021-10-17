# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 19:12:41 2021

@author: catal
"""

import unittest
import ps4a


class Testps4a(unittest.TestCase):

    def test_get_permutations(self):
        self.assertEqual(ps4a.get_permutations(""), [])
        self.assertEqual(ps4a.get_permutations("a"), ["a"])
        self.assertEqual(ps4a.get_permutations("123").sort(),
                         ['123', '213', '231', '132', '312', '321'].sort())
        # sequen len=1
        # numbers
        # letters
        # space
        # special characters


if __name__ == "__main__":
    unittest.main()

# TODO plan tests
# TODO plan values for tests
# TODO write unittests
