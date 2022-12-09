from copy import deepcopy

from pyswip import Prolog


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


def test_tree_insert():
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


def test_tree():
    tree = Tree(12, Tree(6, Tree(2, None, Tree(4)), Tree(8, None, Tree(10))),
                Tree(14, None, Tree(18, Tree(16), Tree(20)), ))

    print('Tree:')
    print(tree)

    tree_prolog = str(tree)
    prolog = Prolog()
    prolog.consult("../prolog/prolog_knowledge_base.pl")

    close_menu = False
    while not close_menu:
        print("1. Añadir un vértice.")
        print("2. Buscar un vértices.")
        print("3. Buscar adyacentes a un vértices.")
        print("4. Recorrer en orden.")
        print("5. Recorrer en preorden.")
        print("6. Recorrer en profundidad.")
        print("7. Recorrer a lo ancho.")
        print("8. Determinar si un nodo es padre de otro.")
        print("9. Determinar si un nodo es hoja.")
        print("10. Determinar si un nodo es predecesor de otro.")
        print("11. Determinar el nivel del árbol.")
        print("Other. Exit.")
        option = int(input("Seleccione una opcion: "))

        if option == 1:
            value = int(input("Introduzca un valor para el vértice: "))

            print("Via Python:")
            tree_clone: Tree = deepcopy(tree)
            tree_clone.insert(value)
            print("[{'NewTree': '" + str(tree_clone) + "'}]")

            print("Via Prolog:")
            prolog_query = f"insert({value}, {str(tree_prolog)}, NewTree)"
            prolog_result = list(prolog.query(prolog_query))
            print(prolog_result)

        elif option == 2:
            print("1. Usar Python.")
            print("2. Usar Prolog.")
            option = int(input("Selecicone una opcion: "))
            if option == 1:
                value = int(input("Introduzca el valor del vértice: "))
                print(tree.exists_vertex(Tree(value), tree))
            elif option == 2:
                value = input("Introduzca un valor para el vértice: ")
                prolog_query = f"find({value},{tree_prolog}, SubTree)"
                result = bool(list(prolog.query(prolog_query)))
                print(result)

        # elif option == 3:
        #     character = input("Introduzca la letra del vértice: ")
        #     value = int(input("Introduzca el valor del vértice: "))
        #     tree_clone = deepcopy(tree)
        #     tree_clone.delete_vertex(Tree(TreeObject(character, value)), tree_clone)
        #     print(tree_clone)

        elif option == 3:
            value = int(input("Introduzca el valor del vértice: "))
            result = tree.adjacent_vertexes(Tree(value), tree)
            for i in result:
                if i is not None:
                    print(i.data)

        elif option == 4:
            print("1. Usar Python.")
            print("2. Usar Prolog.")
            option = int(input("Selecicone una opcion: "))
            if option == 1:
                tree.in_order_tour()
                print()
            elif option == 2:
                result = list(prolog.query(f"inorder({tree_prolog}, List)"))
                print(result)

        elif option == 5:
            print("1. Usar Python.")
            print("2. Usar Prolog.")
            option = int(input("Selecicone una opcion: "))
            if option == 1:
                tree.preorder_tour(tree)
                print()
            elif option == 2:
                result = list(prolog.query(f"preorder({tree_prolog}, List)"))
                print(result)

        elif option == 6:
            print("1. Usar Python.")
            print("2. Usar Prolog.")
            option = int(input("Selecicone una opcion: "))
            if option == 1:
                tree.depth_tour(tree)
                print()
            elif option == 2:
                result = list(prolog.query(f"postorder({tree_prolog}, List)"))
                print(result)

        elif option == 7:
            tree.broad_tour([tree])

        elif option == 8:
            value_1 = input("Introduzca un valor para el vértice hijo: ")
            value_2 = input("Introduzca un valor para el vértice padre: ")
            prolog_query = f"parent({value_2},{value_1},{tree_prolog})"
            result = bool(list(prolog.query(prolog_query)))
            print(result)

        elif option == 9:
            print("1. Usar Python.")
            print("2. Usar Prolog.")
            option = int(input("Selecicone una opcion: "))
            if option == 1:
                value = int(input("Introduzca el valor del vértice: "))
                print(tree.is_leaf(Tree(value)))
            elif option == 2:
                value = input("Introduzca un valor para el vértice: ")
                result = bool(list(prolog.query(f"leaf({value}, {tree_prolog})")))
                print(result)

        elif option == 10:
            value_1 = input("Introduzca un valor para el vértice hijo: ")
            value_2 = input("Introduzca un valor para el vértice predecesor: ")
            prolog_query = f"predecessor({value_2},{value_1},{tree_prolog})"
            result = bool(list(prolog.query(prolog_query)))
            print(result)

        elif option == 11:
            print("1. Usar Python.")
            print("2. Usar Prolog.")
            option = int(input("Selecicone una opcion: "))
            if option == 1:
                print(tree.get_level())
            elif option == 2:
                result = list(prolog.query(f"level(Level, {tree_prolog})"))
                print(result)

        else:
            close_menu = True

        print()


if __name__ == '__main__':
    test_tree()
