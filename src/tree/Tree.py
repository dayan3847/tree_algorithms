class Tree:
    data: float
    left: 'Tree'
    right: 'Tree'
    parent: 'Tree'

    def __init__(self, data: float, left: 'Tree' = None, right: 'Tree' = None, parent: 'Tree' = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self) -> str:
        tree_str = f'tree({str(self.data)}, '
        # left
        if self.left is not None:
            tree_str += str(self.left)
        else:
            tree_str += 'nil'
        tree_str += ', '
        # right
        if self.right is not None:
            tree_str += str(self.right)
        else:
            tree_str += 'nil'
        tree_str += ')'

        return tree_str

    def __gt__(self, other: 'Tree'):
        return self.data > other.data

    def __lt__(self, other: 'Tree'):
        return self.data < other.data

    def __eq__(self, other: 'Tree'):
        return self.data == other.data

    def __ge__(self, other: 'Tree'):
        return self.data >= other.data

    def __le__(self, other: 'Tree'):
        return self.data <= other.data

    def __ne__(self, other: 'Tree'):
        return self.data != other.data

    # add_new_vertex
    def insert(self, new_data: float):
        if new_data < self.data:
            if self.left is None:
                self.left = Tree(new_data)
                self.left.parent = self
                return
            else:
                self.left.insert(new_data)
        else:
            if self.right is None:
                self.right = Tree(new_data)
                self.right.parent = self
                return
            else:
                self.right.insert(new_data)

    def in_order_tour(self):
        if None is not self.left:
            self.left.in_order_tour()
        print(self.data, end=", ")
        if None is not self.right:
            self.right.in_order_tour()

    def preorder_tour(self, tree: 'Tree'):
        if tree:
            print(tree.data, end=", ")
            self.preorder_tour(tree.left)
            self.preorder_tour(tree.right)

    def exists_vertex(self, vertex: 'Tree', tree: 'Tree') -> 'bool':
        if not tree:
            return False
        elif tree == vertex:
            return True
        elif vertex < tree:
            return self.exists_vertex(vertex, tree.left)
        else:
            return self.exists_vertex(vertex, tree.right)

    def get_vertex(self, vertex: 'Tree', tree: 'Tree') -> 'Tree':
        if not tree:
            return None
        elif tree == vertex:
            return tree
        elif vertex < tree:
            return self.get_vertex(vertex, tree.left)
        else:
            return self.get_vertex(vertex, tree.right)

    def adjacent_vertexes(self, vertex: 'Tree', tree: 'Tree') -> list['Tree']:
        if not tree:
            return []
        elif tree == vertex:
            return [tree.left, tree.right, tree.parent]
        elif vertex < tree:
            return self.adjacent_vertexes(vertex, tree.left)
        else:
            return self.adjacent_vertexes(vertex, tree.right)

    def depth_tour(self, tree: 'Tree'):
        if tree:
            self.depth_tour(tree.left)
            self.depth_tour(tree.right)
            print(tree.data, end=", ")

    def broad_tour(self, nodes: list['Tree']):

        if len(nodes) == 0:
            return

        for node in nodes:
            if node is not None:
                print(node.data, end=", ")
        print()

        children = []
        for node in nodes:
            if node is not None:
                children.append(node.left)
                children.append(node.right)

        self.broad_tour(children)

    def get_level(self) -> int:
        left_level: int = 0 if self.left is None else self.left.get_level()
        right_level: int = 0 if self.right is None else self.right.get_level()
        return max(left_level, right_level) + 1

    def is_leaf(self, vertex: 'Tree') -> bool:
        found = self.get_vertex(vertex, self)
        if found:
            if found.right is None and found.left is None:
                return True
            else:
                return False
