from copy import deepcopy

from pyswip import Prolog

from src.tree import Tree


def my_main():
    tree = Tree(12, Tree(6, Tree(2, None, Tree(4)), Tree(8, None, Tree(10))),
                Tree(14, None, Tree(18, Tree(16), Tree(20)), ))

    print('Tree:')
    print(tree)

    tree_prolog = str(tree)
    prolog = Prolog()
    prolog.consult("./prolog/prolog_knowledge_base.pl")

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
    my_main()
