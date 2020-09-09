
"""
Graph, 
relationships between parents and children: 
            edd vertice/nodes to graph
            add edges to graph, child, parent direction

Data set and Id return earlier ancestor
            queu add path from starting node to queue

directions:
a parent may have any number of children          
queue not empty, 
dequeue 1st path
last vertex from path """

def earliest_ancestor(ancestors, starting_node, parent=None):
    if starting_node in [tree[1] for tree in ancestors]:
        for i in ancestors:                                             # Tree
            if starting_node == i[1]:                                   # Node
                return earliest_ancestor(ancestors, i[0], parent=True)  # Starting node - iterate up tree
    elif parent == True:
        return starting_node
    else:
        return -1
if __name__ == '__main__':
        test_ancestors = [(1, 3), (2, 3), (3, 6), 
                            (5, 6), (5, 7), (4, 5), 
                            (4, 8), (8, 9), (11, 8), 
                            (10, 1)]
        print(earliest_ancestor(test_ancestors, 1))
        print(earliest_ancestor(test_ancestors, 1))
        print(earliest_ancestor(test_ancestors, 2))
        print(earliest_ancestor(test_ancestors, 3))
        print(earliest_ancestor(test_ancestors, 4))
        print(earliest_ancestor(test_ancestors, 5))
        print(earliest_ancestor(test_ancestors, 6))
        print(earliest_ancestor(test_ancestors, 7))
        print(earliest_ancestor(test_ancestors, 8))
        print(earliest_ancestor(test_ancestors, 9))
        print(earliest_ancestor(test_ancestors, 10))
        print(earliest_ancestor(test_ancestors, 11))