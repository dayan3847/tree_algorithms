import unittest

from src.tree import Tree


class TestTree(unittest.TestCase):

    def test_tree_insert(self):
        tree = Tree(
            12,
            Tree(
                6,
                Tree(
                    2,
                    None,
                    Tree(4)
                ),
                Tree(
                    8,
                    None,
                    Tree(10)
                )
            ),
            Tree(
                14,
                None,
                Tree(
                    18,
                    Tree(16),
                    Tree(20)
                ),
            )
        )

        tree2: Tree = Tree(12)
        tree2.insert(6)
        tree2.insert(2)
        tree2.insert(14)
        tree2.insert(8)
        tree2.insert(10)
        tree2.insert(4)
        tree2.insert(18)
        tree2.insert(16)
        tree2.insert(20)

        print('Tree:')
        print(tree)
        print('Tree2:')
        print(tree2)

        self.assertEqual(tree, tree2)


if __name__ == '__main__':
    unittest.main()
