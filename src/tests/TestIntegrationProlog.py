import unittest
from pyswip import Prolog


class TestTree(unittest.TestCase):

    def test_tree1(self):
        prolog = Prolog()
        prolog.assertz("father(michael,john)")

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
